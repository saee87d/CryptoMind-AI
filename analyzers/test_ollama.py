"""Simple connectivity test for the local Ollama service using `llama3`.

Run this script to quickly verify that Ollama is running and reachable.
"""

from __future__ import annotations

import sys

import ollama


def test_ollama_llama3() -> int:
    """Return 0 on success, non-zero on failure."""
    prompt = "Say 'Ollama is online for the Crypto Sentiment Analyzer.'"

    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}],
        )
        message = response.get("message", {}).get("content") or str(response)

        print("Ollama llama3 response:")
        print(message)
        return 0
    except Exception as exc:  # noqa: BLE001
        print("Failed to reach Ollama service or run `llama3`.", file=sys.stderr)
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(test_ollama_llama3())

