"""Database model for final generated content."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.models.generation_job import utc_now


class GeneratedContent(Base):
    """Final user-facing content created by the agent pipeline."""

    __tablename__ = "generated_contents"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    generation_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("content_generations.id", ondelete="CASCADE"),
        unique=True,
        index=True,
        nullable=False,
    )
    title: Mapped[str | None] = mapped_column(String(300), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    content_type: Mapped[str | None] = mapped_column(String(50), index=True, nullable=True)
    active_writer: Mapped[str | None] = mapped_column(String(100), nullable=True)
    revision_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    word_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    rating: Mapped[int | None] = mapped_column(Integer, nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column("metadata", JSON, nullable=True)
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
