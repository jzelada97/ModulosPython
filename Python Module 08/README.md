# Module 08 — The Matrix: Environment Management

## Overview

This module covers the real-world infrastructure of Python development: virtual
environments, dependency management, and configuration. These aren't glamorous topics,
but they're what separate hobby scripts from professional, reproducible software.

## Exercises & Learning Objectives

### ex0 — `construct.py`
**Concept:** Virtual environments — detection, creation, purpose.
The program detects whether it's running inside a venv and displays environment details.
Demonstrates `sys.prefix`, `sys.base_prefix`, `site.getsitepackages()`, and why
isolation matters.

**Why it matters:** Without venvs, installing a package for one project can break another.
Virtual environments give each project its own isolated set of dependencies. Understanding
this is the first step to reproducible Python projects.

### ex1 — `loading.py` + `requirements.txt` + `pyproject.toml`
**Concept:** Package management (pip vs Poetry), dependency declaration.
Checks which packages are available, handles missing dependencies gracefully, and
demonstrates data analysis with numpy/pandas/matplotlib. Provides both `requirements.txt`
(pip) and `pyproject.toml` (Poetry) for the same dependencies.

**Why it matters:** Every team project needs a way to declare "these are the packages
you need." `requirements.txt` is the traditional approach; `pyproject.toml` is the modern
standard. Understanding both means you can work on any Python project.

### ex2 — `oracle.py` + `.env.example` + `.gitignore`
**Concept:** Environment variables, `.env` files, secrets management.
Loads configuration from environment variables using `python-dotenv`. Demonstrates
different behavior for development vs production modes. Includes `.env.example` (safe
to commit) and `.gitignore` rules to prevent leaking secrets.

**Why it matters:** Hardcoding database passwords or API keys in source code is a
security disaster. Environment variables separate configuration from code. The 12-Factor
App methodology considers this essential for any deployable application.

## Key Takeaways

- **Virtual environments** isolate project dependencies — always use one.
- **`requirements.txt`** pins versions for pip; **`pyproject.toml`** is the modern standard.
- **Environment variables** keep secrets out of source code.
- **`.env` files** provide development defaults; `.gitignore` prevents committing real secrets.
- These practices are non-negotiable in professional Python development.
- Understanding your environment (Python path, site-packages, active venv) helps debug
  import issues and version conflicts.
