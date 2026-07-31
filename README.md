# ModulosPython

Python learning path — 11 progressive modules covering fundamentals through advanced patterns.

## Modules

| # | Name | Topics |
|---|------|--------|
| 00 | Growing Code | Functions, variables, control flow, type annotations |
| 01 | Code Cultivation | OOP: classes, inheritance, encapsulation, polymorphism |
| 02 | Garden Guardian | Exception handling: try/except, raise, custom errors, finally |
| 03 | Data Quest | Collections: lists, tuples, sets, dicts, generators, comprehensions |
| 04 | Data Archivist | File I/O: read, write, streams, context managers |
| 05 | Code Nexus | Abstract classes, polymorphic dispatch, data pipelines |
| 06 | The Codex | Imports: packages, absolute/relative, circular dependencies |
| 07 | DataDeck | Design patterns: abstract factory, mixins, strategy |
| 08 | The Matrix | Virtual environments, pip/Poetry, environment variables |
| 09 | Cosmic Data | Pydantic v2: BaseModel, validators, nested models |
| 10 | FuncMage | Functional programming: lambdas, closures, decorators, functools |

## Requirements

- Python 3.10+
- pydantic (Module 09)
- numpy, pandas, matplotlib (Module 08)
- python-dotenv (Module 08)

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate           # Windows
pip install pydantic numpy pandas matplotlib python-dotenv
```

## Linting & Type Checking

```bash
flake8 . --exclude=.venv,.mypy_cache
python -m mypy "Python Module XX" --ignore-missing-imports
```

## Project Structure

Each module follows the pattern:
```
Python Module XX/
  ex0/
    ft_exercise_name.py
  ex1/
    ...
```

Module 06 and 07 have scripts at the module root (`ft_*.py`, `battle.py`, `tournament.py`)
that test the package exercises.
