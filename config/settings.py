"""Environment configuration for the Crypto Sentiment Analyzer.

Uses `python-dotenv` to load local environment variables from the `.env`
file at the project root and exposes a small, typed `Settings` object.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Load environment variables from the `.env` file if it exists.
if ENV_FILE.exists():
    load_dotenv(ENV_FILE)


@dataclass
class Settings:
    """Core application settings."""

    database_url: str
    coingecko_api_key: str


@lru_cache
def get_settings() -> Settings:
    """Return a cached `Settings` instance built from environment variables."""
    return Settings(
        database_url=os.getenv("DATABASE_URL", "sqlite:///./crypto_sentiment.db"),
        coingecko_api_key=os.getenv("COINGECKO_API_KEY", "your_key_here"),
    )


__all__ = ["Settings", "get_settings"]

