"""Database model for a user's content generation request."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.models.generation_job import utc_now


class ContentGeneration(Base):
    """Searchable record of the request/configuration used to create content."""

    __tablename__ = "content_generations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    job_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("generation_jobs.id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False,
    )
    topic: Mapped[str] = mapped_column(String(200), nullable=False)
    content_type: Mapped[str] = mapped_column(String(50), index=True, nullable=False)
    audience: Mapped[str | None] = mapped_column(String(200), nullable=True)
    tone: Mapped[str] = mapped_column(String(50), nullable=False)
    brief: Mapped[str | None] = mapped_column(Text, nullable=True)
    reference_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    max_tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    status: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        onupdate=utc_now,
        nullable=False,
    )
