import os
from datetime import datetime
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.db.models import User, Session, Interaction, Source, InteractionSource, DocType, SessionFile, File, SourceCategory, IndividualFeedback, GeneralFeedback

async def sync_database_with_chunks(db: AsyncSession, docs: list[dict[str, Any]]) -> None:
    print("[BOOT] Sincronizando base documental com o banco de dados...")

    result_chunks = await db.execute(select(Source.chunk_id))
    seen_chunk_ids: set[str] = {row[0] for row in result_chunks}

    sources_map: dict[str, list[dict[str, Any]]] = {}
    for doc in docs:
        sources_map.setdefault(doc["source"], []).append(doc)

    result = await db.execute(select(File.location))
    existing_locations: set[str] = {row[0] for row in result}

    new_labels = set(sources_map.keys()).difference(existing_locations)
    if not new_labels:
        print("[BOOT] Base documental já sincronizada. Nenhum arquivo novo.")
        return
    
    needed_categories = {
        doc.get("category", "")
        for label in new_labels
        for doc in sources_map[label]
        if doc.get("category")
    }

    result = await db.execute(
        select(SourceCategory).where(SourceCategory.name.in_(needed_categories))
    )
    category_map: dict[str, SourceCategory] = {cat.name: cat for cat in result.scalars()}

    for name in needed_categories:
        if name not in category_map:
            cat = SourceCategory(name=name)
            db.add(cat)
            category_map[name] = cat

    await db.flush()

    new_files = 0
    new_chunks = 0

    for source_label in new_labels:
        chunks = sources_map[source_label]

        file = File(
            name=source_label.split("/")[-1],
            location=source_label,
        )
        db.add(file)
        await db.flush()
    
        for chunk in chunks:
            chunk_id = chunk["id"]

            if chunk_id in seen_chunk_ids:
                print(f"[BOOT] Aviso: chunk_id '{chunk_id}' duplicado ignorado para o arquivo '{source_label}'.")
                continue

            seen_chunk_ids.add(chunk_id)

            cat = category_map.get(chunk.get("category", ""))
            db.add(Source(
                file_id=file.id,
                chunk_id=chunk["id"],
                title=chunk["title"],
                score=0.0,
                excerpt=chunk["text"],
                category_id=cat.id if cat else None,
                doc_type=DocType[chunk["doc_type"]],
            ))
            new_chunks += 1
        new_files += 1

    await db.commit()
    print(f"[BOOT] Sincronizados {new_files} arquivo(s) e {new_chunks} chunk(s).")


async def save_session_log(
        db: AsyncSession, 
        session_id: str, 
        # user_id: str,
        username: str,
        interaction_id: str,
        question: str,
        requested_at: datetime,
        responded_at: datetime,
        response: dict | None = None,
        error: str | None = None,
):
    # Gera o usuário com base no nome
    user_obj = User(username=username)
    db.add(user_obj)
    await db.flush()

    # Garante a existência da Sessão
    session_obj = await db.scalar(select(Session).where(Session.id == session_id))
    if not session_obj:
        session_obj = Session(id=session_id, user_id=user_obj.id)
        db.add(session_obj)
        await db.flush()

    answer = None
    mode = "error"
    resolved_q = None
    t_embed = t_retrieve = t_answer = None
    warnings = [error] if error else []

    if response:
        answer = response.get("answer")
        mode = response.get("mode", "unknown")
        resolved_q = response.get("resolved_question")
        
        timings = response.get("timings", {})
        t_embed = timings.get("embedding_ms")
        t_retrieve = timings.get("retrieval_ms")
        t_answer = timings.get("answer_ms")
        
        if response.get("warnings"):
            warnings.extend(response.get("warnings"))

    interaction = Interaction(
        id=interaction_id,
        session_id=session_id,
        question=question,
        answer=answer,
        mode=mode,
        resolved_question=resolved_q,
        embedding_time_ms=t_embed,
        retrieval_time_ms=t_retrieve,
        answer_time_ms=t_answer,
        warning=" | ".join(warnings) if warnings else None,
        requested_at=requested_at,
        responded_at=responded_at
    )
    db.add(interaction)

    if response and "sources" in response:
        for src_data in response["sources"]:
            rag_chunk_id = src_data.get("id")
            
            # Verifica se a fonte já está cacheada no banco
            source_obj = await db.scalar(select(Source).where(Source.chunk_id == rag_chunk_id))
            
            if not source_obj:
                file_location = src_data.get("source", "Desconhecido")

                file_obj = await db.scalar(select(File).where(File.location == file_location))

                if not file_obj:
                    file_name = file_location.split("/")[-1] if "/" in file_location else file_location
                    file_obj = File(name=file_name, location=file_location)
                    db.add(file_obj)
                    await db.flush()

                doc_type_enum = DocType.faq if src_data.get("doc_type") == "faq" else DocType.document
                source_obj = Source(
                    chunk_id=rag_chunk_id,
                    file_id=file_obj.id,
                    title=src_data.get("title", "Sem título"),
                    score=src_data.get("score", 0.0),
                    excerpt=src_data.get("excerpt", ""),
                    doc_type=doc_type_enum
                )
                db.add(source_obj)
                await db.flush()
            
            # Vincula a fonte à interação atual
            interaction_source = InteractionSource(
                interaction_id=interaction_id,
                source_id=source_obj.id
            )
            db.add(interaction_source)

    await db.commit()


async def update_interaction_feedback(db: AsyncSession, session_id: str, interaction_id: str, relevance: int, comment: str) -> dict:
    if relevance not in (-1, 0, 1):
        raise ValueError(f"Relevância inválida: {relevance}. Deve ser -1, 0 ou 1.")
    
    result = await db.execute(select(Interaction).where(Interaction.id == interaction_id, Interaction.session_id == session_id))
    interaction = result.scalar_one_or_none()

    if not interaction:
        raise ValueError(f"Interaction {interaction_id} não encontrada na sessão {session_id}.")
    
    
    result = await db.execute(
        select(IndividualFeedback).where(
            IndividualFeedback.interaction_id == interaction_id
        )
    )
    feedback = result.scalar_one_or_none()

    if feedback:
        feedback.relevance = relevance
        feedback.comment = comment[:5000]
    else:
        feedback = IndividualFeedback(
            interaction_id=interaction_id,
            relevance=relevance,
            comment=comment[:5000],
        )
        db.add(feedback)

    await db.commit()
    await db.refresh(feedback)

    return {"relevance": feedback.relevance, "comment": feedback.comment}


async def save_general_feedback(db: AsyncSession, session_id: str, feedback_data: dict) -> None:
    result = await db.execute(
        select(Session).where(Session.id == session_id)
    )
    session = result.scalar_one_or_none()

    if not session:
        raise ValueError(f"Sessão {session_id} não encontrada.")
    
    feedback = GeneralFeedback(
        user_id=session.user_id,
        form_data=feedback_data,
    )

    db.add(feedback)
    await db.commit()