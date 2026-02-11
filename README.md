# Crypto Sentiment Analyzer

The **Crypto Sentiment Analyzer** is a Python-based system designed to collect crypto-related data (prices, news, and social media signals), run LLM-powered sentiment analysis (via Ollama), and store processed insights for further analytics and visualization.

This project is structured as a multi-phase roadmap over 42 days. Each phase focuses on a specific aspect: data collection, analysis, storage, processing, and user-facing interfaces.

## Current Status

- **Phase**: 1 / 5 — Project Initialization
- **Day**: 1 — Basic folder structure, configuration, and environment setup
- **Next Steps**: Implement collectors, analyzers, and storage layers, followed by processors and a rich CLI/terminal UI.

## High-Level Architecture

- `collectors/`: Fetch raw data from APIs (e.g., CoinGecko, Reddit, Twitter/X).
- `analyzers/`: Run LLM-based sentiment analysis using Ollama models.
- `storage/`: Handle PostgreSQL persistence and caching.
- `processors/`: Aggregate and transform raw data into sentiment metrics.
- `ui/`: Provide CLI/terminal interfaces for users.
- `utils/`: Shared helpers, logging, and common utilities.
- `config/`: Settings, environment management, and configuration logic.
- `tests/`: Unit and integration tests.

