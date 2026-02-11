"""Database engine and initialization utilities for SQLite."""

from __future__ import annotations

from typing import Any, Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import get_settings
from .models import Base


settings = get_settings()

connect_args: Dict[str, Any] = {}
if settings.database_url.startswith("sqlite"):
    # Required for SQLite when using the same connection in multiple threads.
    connect_args["check_same_thread"] = False

engine = create_engine(settings.database_url, connect_args=connect_args, future=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)


def init_db() -> None:
    """Create all tables in the configured SQLite database."""
    Base.metadata.create_all(bind=engine)


__all__ = ["engine", "SessionLocal", "init_db"]

