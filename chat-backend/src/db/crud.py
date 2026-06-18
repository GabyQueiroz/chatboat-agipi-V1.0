from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.db.models import ChatSession, Interaction, GeneralFeedback

async def save_session_log(
        db: AsyncSession, 
        session_id: str, 
        user_name: str,
        interaction_id: str,
        question: str,
        request_ts: str,
        response_ts: str,
        response: dict | None = None,
        error: str | None = None,
):
    result = await db.execute(select(ChatSession).where(ChatSession.id == session_id))
    session_obj = result.scalar_one_or_none()

    if not session_obj:
        session_obj = ChatSession(id=session_id, user_name=user_name)
        db.add(session_obj)
        await db.flush()

    interaction = Interaction(
        id=interaction_id,
        session_id=session_id,
        request_timestamp=request_ts,
        question=question,
        response_timestamp=response_ts,
        response_data=response,
        error=error
    )

    db.add(interaction)
    await db.commit()


async def update_interaction_feedback(db: AsyncSession, session_id: str, interaction_id: str, relevance: int, comment: str) -> dict:
    result = await db.execute(select(Interaction).where(Interaction.id == interaction_id, Interaction.session_id == session_id))
    interaction = result.scalar_one_or_none()

    if not interaction:
        raise ValueError(f"Interaction {interaction_id} not found in session {session_id}")
    
    if relevance not in (-1, 0, 1):
        raise ValueError(f"Invalid relevance value: {relevance}. Must be -1, 0, or 1")
    
    interaction.feedback_relevance = relevance
    interaction.feedback_comment = comment[:5000]

    await db.commit()
    return {"relevance": interaction.feedback_relevance, "comment": interaction.feedback_comment}


async def save_general_feedback(db: AsyncSession, session_id: str, feedback_data: dict, timestamp):
    feedback = GeneralFeedback(
        session_id=session_id,
        feedback_data=feedback_data,
        timestamp=timestamp
    )
    db.add(feedback)
    await db.commit()