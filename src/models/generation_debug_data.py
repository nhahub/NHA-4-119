"""Database model for agent debug payloads."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.models.generation_job import utc_now


class GenerationDebugData(Base):
    """Structured agent internals kept separate from clean generated content."""

    __tablename__ = "generation_debug_data"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    generation_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("content_generations.id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False,
    )
    outline_payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    search_payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    draft_payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    critique_payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )
