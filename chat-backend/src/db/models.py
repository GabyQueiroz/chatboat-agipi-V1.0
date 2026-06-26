import enum
from datetime import datetime
from sqlalchemy import String, Integer, Text, ForeignKey, Float, Enum, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base

class DocType(enum.Enum):
    document = "document"
    faq = "faq"

class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String)
    email: Mapped[str | None] = mapped_column(String, unique=True)
    password: Mapped[str | None] = mapped_column(String)
    role: Mapped[str | None] = mapped_column(String)

    sessions: Mapped[list["Session"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    general_feedbacks: Mapped[list["GeneralFeedback"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class Session(Base):
    __tablename__ = "sessions"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="sessions")
    interactions: Mapped[list["Interaction"]] = relationship(back_populates="session", cascade="all, delete-orphan")
    file_associations: Mapped[list["SessionFile"]] = relationship(back_populates="session", cascade="all, delete-orphan")


class Interaction(Base):
    __tablename__ = "interactions"

    session_id: Mapped[str] = mapped_column(ForeignKey("sessions.id"))
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str | None] = mapped_column(Text)
    mode: Mapped[str] = mapped_column(String)
    resolved_question: Mapped[str | None] = mapped_column(Text)
    embedding_time_ms: Mapped[float | None] = mapped_column(Float)
    retrieval_time_ms: Mapped[float | None] = mapped_column(Float)
    answer_time_ms: Mapped[float | None] = mapped_column(Float)
    warning: Mapped[str | None] = mapped_column(Text)
    requested_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    responded_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    session: Mapped["Session"] = relationship(back_populates="interactions")
    individual_feedbacks: Mapped[list["IndividualFeedback"]] = relationship(back_populates="interaction", cascade="all, delete-orphan")
    source_associations: Mapped[list["InteractionSource"]] = relationship(back_populates="interaction", cascade="all, delete-orphan")


class IndividualFeedback(Base):
    __tablename__ = "individual_feedbacks"

    interaction_id: Mapped[str] = mapped_column(ForeignKey("interactions.id"))
    relevance: Mapped[int | None] = mapped_column(Integer)
    comment: Mapped[str | None] = mapped_column(Text)

    interaction: Mapped["Interaction"] = relationship(back_populates="individual_feedbacks")


class GeneralFeedback(Base):
    __tablename__ = "general_feedbacks"

    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    form_data: Mapped[dict] = mapped_column(JSON)

    user: Mapped["User"] = relationship(back_populates="general_feedbacks")


class SourceCategory(Base):
    __tablename__ = "source_categories"

    name: Mapped[str] = mapped_column(String, unique=True)

    sources: Mapped[list["Source"]] = relationship(back_populates="category")


class Source(Base):
    __tablename__ = "sources"

    chunk_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)     # id proveniente do indice
    file_id: Mapped[str] = mapped_column(ForeignKey("files.id"))
    title: Mapped[str] = mapped_column(String)
    score: Mapped[float] = mapped_column(Float, default=0.0)
    excerpt: Mapped[str] = mapped_column(Text)
    category_id: Mapped[str | None] = mapped_column(ForeignKey("source_categories.id"))
    doc_type: Mapped[DocType] = mapped_column(Enum(DocType))

    file: Mapped["File"] = relationship(back_populates="sources")
    category: Mapped["SourceCategory"] = relationship(back_populates="sources")
    interaction_associations: Mapped[list["InteractionSource"]] = relationship(back_populates="source", cascade="all, delete-orphan")

class InteractionSource(Base):
    __tablename__ = "interactions_sources"

    interaction_id: Mapped[str] = mapped_column(ForeignKey("interactions.id"))
    source_id: Mapped[str] = mapped_column(ForeignKey("sources.id"))

    interaction: Mapped["Interaction"] = relationship(back_populates="source_associations")
    source: Mapped["Source"] = relationship(back_populates="interaction_associations")

class File(Base):
    __tablename__ = "files"

    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String, unique=True)

    sources: Mapped[list["Source"]] = relationship(back_populates="file", cascade="all, delete-orphan")
    session_associations: Mapped[list["SessionFile"]] = relationship(back_populates="file", cascade="all, delete-orphan")


class SessionFile(Base):
    __tablename__ = "sessions_files"

    session_id: Mapped[str] = mapped_column(ForeignKey("sessions.id"))
    file_id: Mapped[str] = mapped_column(ForeignKey("files.id"))

    session: Mapped["Session"] = relationship(back_populates="file_associations")
    file: Mapped["File"] = relationship(back_populates="session_associations")