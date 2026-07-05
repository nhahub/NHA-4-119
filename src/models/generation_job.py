"""Database model for background generation jobs."""

from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp for job lifecycle fields."""
    return datetime.now(timezone.utc)


class GenerationJob(Base):
    """Persistent record for one agent generation request."""

    __tablename__ = "generation_jobs"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    user_id: Mapped[str | None] = mapped_column(String(255), index=True, nullable=True)
    status: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    progress: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    message: Mapped[str] = mapped_column(Text, nullable=False, default="Job queued")
    request_payload: Mapped[dict] = mapped_column(JSON, nullable=False)
    result_payload: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
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
    completed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
