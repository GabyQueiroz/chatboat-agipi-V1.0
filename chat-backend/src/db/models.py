from datetime import datetime, timezone
from sqlalchemy import String, Integer, Text, ForeignKey, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.database import Base

class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    user_name: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    interactions: Mapped[list["Interaction"]] = relationship(back_populates="session", cascade="all, delete-orphan")


class Interaction(Base):
    __tablename__ = "interactions"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("chat_sessions.id"))
    question: Mapped[str] = mapped_column(Text)
    request_timestamp: Mapped[str] = mapped_column(String)
    response_timestamp: Mapped[str] = mapped_column(String)
    response_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    error: Mapped[str | None] = mapped_column(String, nullable=True)

    feedback_relevance: Mapped[int] = mapped_column(Integer, default=0)
    feedback_comment: Mapped[str] = mapped_column(String, default="")

    session: Mapped[ChatSession] = relationship(back_populates="interactions")


class GeneralFeedback(Base):
    __tablename__ = "general_feedbacks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(ForeignKey("chat_sessions.id"))
    feedback_data: Mapped[dict] = mapped_column(JSON)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now(timezone.utc))