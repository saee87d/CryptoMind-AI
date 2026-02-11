# Contributing to Crypto Sentiment Analyzer

First off, thank you for considering contributing to Crypto Sentiment Analyzer! 🎉

It's people like you that make this project such a great tool for the crypto community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [How to Contribute](#how-to-contribute)
- [Style Guidelines](#style-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community](#community)

---

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of:
- Age, body size, disability
- Ethnicity, gender identity
- Level of experience
- Nationality, personal appearance
- Race, religion
- Sexual identity and orientation

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy towards others

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct which could reasonably be considered inappropriate

---

## Getting Started

### Prerequisites

Before you begin, ensure you have:

- **Python 3.9+** installed
- **Git** installed
- **Ollama** installed and running
- A **GitHub account**
- Basic knowledge of Python and async programming
- Familiarity with Git workflow

### Setting Up Development Environment

1. **Fork the Repository**

   Click the "Fork" button at the top right of the repository page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/YOUR-USERNAME/crypto-sentiment-analyzer.git
   cd crypto-sentiment-analyzer
   ```

3. **Add Upstream Remote**

   ```bash
   git remote add upstream https://github.com/original-owner/crypto-sentiment-analyzer.git
   ```

4. **Create Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

5. **Install Dependencies**

   ```bash
   # Install main dependencies
   pip install -r requirements.txt
   
   # Install development dependencies
   pip install -r requirements-dev.txt
   ```

6. **Install Pre-commit Hooks**

   ```bash
   pre-commit install
   ```

7. **Setup Ollama**

   ```bash
   # Pull test model
   ollama pull llama3.2:3b
   ```

8. **Configure Environment**

   ```bash
   cp .env.example .env
   # Edit .env with your test API keys
   ```

9. **Initialize Database**

   ```bash
   python -m storage.init_db
   ```

10. **Run Tests**

    ```bash
    pytest tests/ -v
    ```

If all tests pass, you're ready to contribute! 🎉

---

## Development Process

### Branching Strategy

We use a simple branching model:

```
main (production-ready code)
  ├── develop (integration branch)
  │   ├── feature/your-feature
  │   ├── fix/bug-description
  │   └── docs/documentation-update
```

### Creating a Feature Branch

```bash
# Update your local main
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/amazing-feature

# Or for bug fixes
git checkout -b fix/bug-description

# Or for documentation
git checkout -b docs/update-installation
```

### Making Changes

1. **Write Code**
   - Follow our style guidelines
   - Add type hints
   - Write docstrings
   - Keep functions focused and small

2. **Add Tests**
   - Write unit tests for new features
   - Ensure existing tests still pass
   - Aim for >80% code coverage

3. **Update Documentation**
   - Update README if needed
   - Add docstrings
   - Update relevant docs in `docs/`

4. **Run Checks**
   ```bash
   # Format code
   black .
   isort .
   
   # Run linters
   flake8 .
   mypy .
   
   # Run tests
   pytest tests/ --cov
   ```

### Committing Changes

We follow [Conventional Commits](https://www.conventionalcommits.org/).

**Format:**
```
type(scope): subject

body (optional)

footer (optional)
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements

**Examples:**
```bash
git commit -m "feat(collectors): add Reddit rate limiting"
git commit -m "fix(analyzer): resolve caching bug in sentiment analysis"
git commit -m "docs(readme): update installation instructions for Windows"
git commit -m "test(aggregator): add unit tests for daily stats"
```

**Good commit messages:**
```
✅ feat(cli): add --verbose flag for detailed output
✅ fix(database): prevent duplicate entries in NewsArticle table
✅ docs(api): add examples for SentimentAnalyzer usage
✅ refactor(collectors): extract rate limiting to utility class
```

**Bad commit messages:**
```
❌ fix stuff
❌ update
❌ changes
❌ WIP
```

### Pushing Changes

```bash
# Push to your fork
git push origin feature/amazing-feature
```

---

## How to Contribute

### 🐛 Reporting Bugs

Before creating a bug report:
- Check if the bug has already been reported
- Verify you're using the latest version
- Try to reproduce with minimal code

**Bug Report Template:**

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. See error '...'

**Expected behavior**
What you expected to happen.

**Actual behavior**
What actually happened.

**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.9.7]
- Ollama version: [e.g., 0.1.14]
- Project version: [e.g., 1.0.0]

**Additional context**
- Error logs
- Screenshots
- Stack traces
```

### 💡 Suggesting Features

**Feature Request Template:**

```markdown
**Is your feature request related to a problem?**
A clear description of the problem. Ex. I'm frustrated when [...]

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Other approaches you've thought about.

**Benefits**
Why is this feature valuable? Who benefits from it?

**Additional context**
- Screenshots
- Examples from other projects
- Implementation ideas
```

### 🔧 Contributing Code

#### Finding an Issue

Look for issues labeled:
- `good-first-issue` - Great for newcomers
- `help-wanted` - We need help!
- `bug` - Bug fixes needed
- `enhancement` - New features
- `documentation` - Docs improvements

#### Pull Request Process

1. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Fill out the PR template

2. **PR Template**

   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Related Issue
   Fixes #123
   
   ## Changes Made
   - Added X feature
   - Fixed Y bug
   - Updated Z documentation
   
   ## Testing
   - [ ] All tests pass
   - [ ] Added new tests
   - [ ] Manual testing completed
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Comments added for complex code
   - [ ] Documentation updated
   - [ ] No new warnings
   
   ## Screenshots (if applicable)
   ```

3. **Review Process**
   - Maintainers will review your PR
   - Address any feedback
   - Make requested changes
   - PR will be merged when approved

4. **After Merge**
   - Delete your feature branch
   - Update your local main
   - Celebrate! 🎉

---

## Style Guidelines

### Python Style

We follow **PEP 8** with some customizations:

- **Line length**: 88 characters (Black default)
- **Indentation**: 4 spaces
- **Quotes**: Double quotes for strings
- **Imports**: Sorted with isort

### Code Formatting

We use **Black** for formatting:

```bash
# Format all files
black .

# Check without formatting
black --check .

# Format specific file
black collectors/coingecko.py
```

### Import Organization

We use **isort** for import sorting:

```python
# Standard library imports
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Third-party imports
import pandas as pd
from sqlalchemy import create_engine

# Local imports
from collectors.coingecko import CoinGeckoCollector
from storage.models import Cryptocurrency
from utils.helpers import format_date
```

### Naming Conventions

```python
# Classes: PascalCase
class SentimentAnalyzer:
    pass

# Functions and variables: snake_case
def analyze_sentiment(text: str) -> dict:
    sentiment_score = 0.5
    return {"score": sentiment_score}

# Constants: UPPER_SNAKE_CASE
MAX_RETRIES = 3
API_BASE_URL = "https://api.coingecko.com"

# Private methods/variables: _leading_underscore
def _internal_helper():
    pass

_cache = {}
```

### Type Hints

Always use type hints:

```python
# Good ✅
def analyze_text(
    text: str,
    model: str = "llama3.2:3b",
    cache: bool = True
) -> Dict[str, Any]:
    pass

# Bad ❌
def analyze_text(text, model="llama3.2:3b", cache=True):
    pass
```

### Docstrings

Use Google-style docstrings:

```python
def collect_coin_data(coin_id: str, include_market: bool = True) -> dict:
    """
    Collect comprehensive data for a cryptocurrency.
    
    Fetches coin information from CoinGecko API including market data,
    community stats, and sentiment votes.
    
    Args:
        coin_id: CoinGecko coin identifier (e.g., 'bitcoin')
        include_market: Whether to include market data
        
    Returns:
        Dictionary containing coin data with keys:
            - symbol: Ticker symbol (e.g., 'BTC')
            - name: Full name (e.g., 'Bitcoin')
            - market_data: Current market information
            - sentiment_votes: Community sentiment
            
    Raises:
        ValueError: If coin_id is empty or invalid
        APIError: If API request fails
        
    Example:
        >>> collector = CoinGeckoCollector()
        >>> data = await collector.collect_coin_data('bitcoin')
        >>> print(data['symbol'])
        'BTC'
        
    Note:
        This method uses caching to reduce API calls. Cache TTL is 5 minutes.
    """
    pass
```

### Error Handling

```python
# Good ✅
def get_coin_data(coin_id: str) -> dict:
    """Get coin data with proper error handling."""
    if not coin_id:
        raise ValueError("coin_id cannot be empty")
    
    try:
        response = requests.get(f"{API_URL}/coins/{coin_id}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Failed to fetch coin data: {e}")
        raise APIError(f"Could not fetch data for {coin_id}") from e

# Bad ❌
def get_coin_data(coin_id):
    response = requests.get(f"{API_URL}/coins/{coin_id}")
    return response.json()  # No error handling!
```

### Logging

```python
import logging

logger = logging.getLogger(__name__)

# Good ✅
logger.info(f"Collecting data for {coin_id}")
logger.warning(f"Rate limit approaching: {remaining} calls left")
logger.error(f"Failed to analyze sentiment: {error}", exc_info=True)

# Bad ❌
print(f"Collecting data for {coin_id}")  # Don't use print!
```

---

## Testing

### Test Structure

```
tests/
├── unit/                  # Unit tests
│   ├── test_collectors.py
│   ├── test_analyzers.py
│   ├── test_aggregators.py
│   └── test_database.py
├── integration/           # Integration tests
│   ├── test_pipeline.py
│   └── test_api_integration.py
├── fixtures/              # Test data
│   ├── sample_data.json
│   └── mock_responses.py
└── conftest.py           # Pytest configuration
```

### Writing Tests

```python
import pytest
from collectors.coingecko import CoinGeckoCollector

@pytest.fixture
def collector():
    """Provide a test collector instance."""
    return CoinGeckoCollector(api_key="test_key")

@pytest.mark.asyncio
async def test_collect_valid_coin(collector, mock_api):
    """Test collecting data for a valid coin."""
    # Arrange
    coin_id = "bitcoin"
    expected_symbol = "BTC"
    
    # Act
    result = await collector.get_coin_data(coin_id)
    
    # Assert
    assert result is not None
    assert result['symbol'] == expected_symbol
    assert 'market_data' in result

@pytest.mark.asyncio
async def test_collect_invalid_coin(collector):
    """Test error handling for invalid coin ID."""
    # Arrange
    invalid_id = "not-a-real-coin"
    
    # Act & Assert
    with pytest.raises(ValueError):
        await collector.get_coin_data(invalid_id)

def test_rate_limiting(collector, mock_api):
    """Test rate limiting prevents excessive calls."""
    # Test implementation
    pass

@pytest.mark.parametrize("coin_id,expected", [
    ("bitcoin", "BTC"),
    ("ethereum", "ETH"),
    ("cardano", "ADA"),
])
async def test_multiple_coins(collector, coin_id, expected):
    """Test collection for multiple coins."""
    result = await collector.get_coin_data(coin_id)
    assert result['symbol'] == expected
```

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/unit/test_collectors.py -v

# Run specific test
pytest tests/unit/test_collectors.py::test_collect_valid_coin -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run only unit tests
pytest tests/unit/ -v

# Run only integration tests
pytest tests/integration/ -v

# Run tests matching pattern
pytest -k "collector" -v
```

### Test Coverage

Aim for these coverage targets:

- **Overall**: >85%
- **Critical modules**: >95%
  - collectors/
  - analyzers/
  - storage/
- **UI modules**: >75%
- **Utilities**: >80%

View coverage report:
```bash
pytest tests/ --cov=. --cov-report=html
open htmlcov/index.html  # On Mac
```

---

## Documentation

### Documentation Structure

```
docs/
├── API.md                 # API reference
├── INSTALLATION.md        # Installation guide
├── USAGE.md              # Usage examples
├── CONTRIBUTING.md       # This file
├── DEPLOYMENT.md         # Deployment guide
├── TROUBLESHOOTING.md    # Common issues
└── FAQ.md                # Frequently asked questions
```

### Writing Documentation

**Good documentation:**
- Is clear and concise
- Includes examples
- Is kept up-to-date
- Uses proper formatting
- Has screenshots (when applicable)

**Example:**

```markdown
## Analyzing Sentiment

The sentiment analyzer uses Ollama to classify text as positive, negative, or neutral.

### Basic Usage

```python
from analyzers.sentiment import SentimentAnalyzer

# Initialize analyzer
analyzer = SentimentAnalyzer(model="llama3.2:3b")

# Analyze text
result = await analyzer.analyze_text(
    "Bitcoin is showing strong bullish momentum!"
)

print(result)
# Output: {
#   'sentiment': 'positive',
#   'score': 0.82,
#   'confidence': 0.95
# }
```

### Advanced Options

You can customize the analysis:

```python
# Use different model
analyzer = SentimentAnalyzer(model="mistral:7b")

# Disable caching
result = await analyzer.analyze_text(text, cache=False)

# Batch processing
results = await analyzer.analyze_batch(texts, batch_size=50)
```

### Tips

- Use `llama3.2:3b` for speed
- Use `llama3:8b` for accuracy
- Enable caching to save time
```

---

## Community

### Getting Help

- **📚 Documentation**: Read our [docs](docs/)
- **🐛 Issues**: Search [existing issues](https://github.com/yourusername/crypto-sentiment-analyzer/issues)
- **💬 Discussions**: Ask in [GitHub Discussions](https://github.com/yourusername/crypto-sentiment-analyzer/discussions)
- **📧 Email**: Contact maintainers

### Asking Questions

Before asking:
1. Search existing issues and discussions
2. Read relevant documentation
3. Try to solve it yourself

When asking:
- **Be specific**: Include code, errors, versions
- **Be respectful**: Everyone is volunteering their time
- **Be patient**: Responses may take time

### Providing Feedback

We value your feedback! Help us improve by:
- Reporting bugs you encounter
- Suggesting new features
- Improving documentation
- Sharing your use cases

### Recognition

Contributors are recognized:
- In `CONTRIBUTORS.md`
- In release notes
- On our website
- In documentation

---

## Quick Reference

### Common Commands

```bash
# Setup
git clone <fork-url>
cd crypto-sentiment-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
pre-commit install

# Development
git checkout -b feature/my-feature
# ... make changes ...
black .
isort .
flake8 .
pytest tests/ --cov

# Commit
git add .
git commit -m "feat(scope): description"
git push origin feature/my-feature

# Update from upstream
git fetch upstream
git rebase upstream/main
```

### Code Quality Checklist

Before submitting PR:

- [ ] Code formatted with Black
- [ ] Imports sorted with isort
- [ ] No flake8 warnings
- [ ] Type hints added
- [ ] Docstrings written
- [ ] Tests added/updated
- [ ] Tests passing
- [ ] Coverage >80%
- [ ] Documentation updated
- [ ] Commit messages follow convention
- [ ] PR template filled out

---

## Questions?

If you have questions about contributing, feel free to:
- Open a [Discussion](https://github.com/yourusername/crypto-sentiment-analyzer/discussions)
- Ask in an existing issue
- Contact maintainers

---

Thank you for contributing! 🎉

Every contribution, no matter how small, makes this project better.

Happy coding! 💻
