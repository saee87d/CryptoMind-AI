"""Entry point for the Crypto Sentiment Analyzer."""

from storage.database import init_db


def main() -> None:
    """Initialize the SQLite database and create all tables."""
    init_db()
    print("Database & Tables Created!")


if __name__ == "__main__":
    main()

