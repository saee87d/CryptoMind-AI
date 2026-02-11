"""SQLAlchemy ORM models for the Crypto Sentiment Analyzer."""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all ORM models."""


class Coin(Base):
    """Represents a cryptocurrency asset."""

    __tablename__ = "coins"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    symbol: Mapped[str] = mapped_column(String(32), unique=True, nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    market_data: Mapped[list["MarketData"]] = relationship(
        "MarketData",
        back_populates="coin",
        cascade="all, delete-orphan",
    )
    sentiments: Mapped[list["Sentiment"]] = relationship(
        "Sentiment",
        back_populates="coin",
        cascade="all, delete-orphan",
    )


class MarketData(Base):
    """Market metrics for a given coin at a point in time."""

    __tablename__ = "market_data"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    coin_id: Mapped[int] = mapped_column(ForeignKey("coins.id"), nullable=False, index=True)

    price: Mapped[float] = mapped_column(Float, nullable=False)
    market_cap: Mapped[float] = mapped_column(Float, nullable=True)
    volume: Mapped[float] = mapped_column(Float, nullable=True)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        index=True,
    )

    coin: Mapped[Coin] = relationship("Coin", back_populates="market_data")


class Sentiment(Base):
    """LLM-derived sentiment for a coin from a particular source."""

    __tablename__ = "sentiments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    coin_id: Mapped[int] = mapped_column(ForeignKey("coins.id"), nullable=False, index=True)

    source: Mapped[str] = mapped_column(String(64), nullable=False, index=True)
    raw_text: Mapped[str] = mapped_column(Text, nullable=False)
    sentiment_score: Mapped[float] = mapped_column(Float, nullable=False)
    label: Mapped[str] = mapped_column(String(32), nullable=False)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
        index=True,
    )

    coin: Mapped[Coin] = relationship("Coin", back_populates="sentiments")


__all__ = ["Base", "Coin", "MarketData", "Sentiment"]

