# Module 08 — The Matrix: Environment Management

## Overview

This module covers the real-world infrastructure of Python development: virtual
environments, dependency management, and configuration. These aren't glamorous topics,
but they're what separate hobby scripts from professional, reproducible software.

This README also doubles as a grading reference: it mirrors the official 42 School
evaluation scale for `Python Module 08` (repository: `ex0/`, `ex1/`, `ex2/`) so each
exercise's checklist can be verified directly against the code.

## Preliminaries (checked before grading starts)

- [x] `ex0/`, `ex1/`, `ex2/` directories exist in the repository.
- [x] Each directory contains the files required by the subject (listed per exercise below).
- [x] No `.env` file with real secrets is committed (`ex2/` only ships `.env.example`;
      `.env` itself is git-ignored).

## Exercises & Learning Objectives

### ex0 — `construct.py` ("The Construct")

**What this exercise wants you to teach you:** why Python projects must isolate their
dependencies from each other, and how to detect and prove that isolation programmatically
rather than just taking it on faith.

**Concept:** Virtual environments — detection, creation, purpose.
The program detects whether it's running inside a venv and displays environment details.
Demonstrates `sys.prefix`, `sys.base_prefix`, `VIRTUAL_ENV`, and `sys.path` inspection for
`site-packages`, and why isolation matters.

**Why it matters:** Without venvs, installing a package for one project can break another.
Virtual environments give each project its own isolated set of dependencies. Understanding
this is the first step to reproducible Python projects.

**Evaluation checklist (Exercise 0):**

- [x] Required file present: `construct.py`.
- [x] Correctly detects whether it's running in a virtual environment
      (`in_virtualenv()` checks `sys.base_prefix != sys.prefix`, `sys.real_prefix`, and
      `VIRTUAL_ENV`).
- [x] Displays different output for each scenario ("You're still plugged in" vs.
      "You're in the construct").
- [x] Provides clear instructions for creating a virtual environment
      (`python -m venv matrix_env` + activation commands for Unix and Windows).
- [x] Shows relevant path information: `sys.executable`, the venv's name/path, and the
      resolved `site-packages` directory (`find_site_packages()`).

> Verified: running `construct.py` outside a venv prints the "plugged in" warning path;
> running it after `python -m venv` + activation (so `VIRTUAL_ENV` is set) prints the
> "in the construct" path with the correct venv name and `site-packages` path.

**Subject-only audit (against `en.subject.txt` directly, not just the eval sheet):**

- [x] **Fixed** — `find_site_packages()`'s return type used `from typing import Optional`,
      but ex0's subject "Authorized" list is `sys, os, site modules, print()` only —
      `typing` isn't on it. Since the project targets Python 3.10+, the annotation is now
      written as the builtin `str | None`, which needs no import at all.
- [x] **Fixed a real bug**, found while testing "in venv, invoked without activation"
      (`/path/to/venv/bin/python construct.py`, i.e. `VIRTUAL_ENV` unset): the fallback
      `venv = os.environ.get('VIRTUAL_ENV') or os.path.dirname(sys.executable)` resolved to
      the venv's `bin/` (or `Scripts/`) folder, so it printed `Virtual Environment: bin` and
      `Environment Path: /tmp/matrix_env/bin` instead of `matrix_env` / `/tmp/matrix_env`.
      Fixed to fall back to `sys.prefix`, which is already the venv root once
      `in_virtualenv()` has confirmed `sys.prefix != sys.base_prefix`. Verified by running
      the script both via direct venv-python invocation and after `source .../activate` —
      both now report the correct venv name and path.

### ex1 — `loading.py` + `requirements.txt` + `pyproject.toml` ("Loading Programs")

**What this exercise wants you to teach you:** the pip-vs-Poetry dependency-management
landscape, and how to build a program that degrades gracefully instead of crashing when a
dependency isn't installed.

**Concept:** Package management (pip vs Poetry), dependency declaration.
Checks which packages are available, handles missing dependencies gracefully, and
demonstrates data analysis with numpy/pandas/matplotlib. Provides both `requirements.txt`
(pip) and `pyproject.toml` (Poetry) for the same dependencies.

**Why it matters:** Every team project needs a way to declare "these are the packages
you need." `requirements.txt` is the traditional approach; `pyproject.toml` is the modern
standard. Understanding both means you can work on any Python project.

**Evaluation checklist (Exercise 1):**

- [x] Required files present: `loading.py`, `requirements.txt`, `pyproject.toml`.
- [x] Handles missing dependencies gracefully with helpful messages
      (`check_dependencies()` / `print_dependency_report()` report `[OK]`/`[MISSING]` per
      package; `install_instructions()` prints both pip and Poetry commands).
- [x] Uses `pandas`, `numpy`, and `matplotlib` as specified (plus `requests`, declared in
      both dependency files).
- [x] Generates a data analysis/visualization: `run_analysis()` simulates data with
      `np.random.normal` (not hardcoded), builds a cumulative sum with `pandas`, and saves
      a plot (`matrix_analysis.png`) with `matplotlib`.
- [x] Shows package version information (`show_versions()`, plus inline `__version__`
      lookups in the dependency report).
- **Dependency files:**
  - [x] `requirements.txt` now pins exact versions (`numpy==1.25.0`, `pandas==2.1.0`,
        `matplotlib==3.7.2`, `requests==2.31.0`) that mirror the constraints in
        `pyproject.toml` and match the subject's own example output — the checklist's
        "listed with appropriate versions?" question is satisfied.
  - [x] `pyproject.toml` is a valid Poetry file with version constraints
        (`numpy = "^1.25"`, `pandas = "^2.1"`, `matplotlib = "^3.7"`, `requests = "^2.31"`,
        `python = "^3.10"`).

> Verified: running `loading.py` with all four packages installed prints `[OK]` for each
> with a resolved version, then produces `matrix_analysis.png` via a genuine
> `numpy`-driven simulation.

**Subject-only audit (against `en.subject.txt` directly, not just the eval sheet):**

- [x] **Fixed** — `check_dependencies()`/`print_dependency_report()` used
      `from typing import Dict` (not on ex1's `pandas, requests, matplotlib, numpy, sys,
      importlib` authorized list) and imported modules with the builtin `__import__()`,
      leaving the explicitly authorized `importlib` module completely unused. Switched the
      annotations to the builtin `dict[str, bool]` (no import needed on 3.10+) and the
      dynamic imports to `importlib.import_module()`.
- [x] **Fixed a real violation** — `show_versions()` imported `pkg_resources` (part of
      `setuptools`, not on ex1's authorized list, and deprecated upstream) to build the
      "comparison function that shows installed package versions" the subject requires.
      Replaced with `importlib.metadata.version()` — stdlib, already authorized via
      `importlib`, and doesn't depend on `setuptools` being present in the environment.
- [x] Verified with all four packages installed (in a scratch environment) that
      `show_versions()` and `run_analysis()` still work identically after the change.
- [x] Confirmed with mypy (`~/.venvs/lint`, which lacks numpy/pandas/matplotlib/requests)
      that the only errors reported are `import-not-found`/`import-untyped` for those four
      packages — exactly the "import errors" the subject exempts for this exercise. No
      other mypy or flake8 issues.

### ex2 — `oracle.py` + `.env.example` + `.gitignore` ("The Oracle")

**What this exercise wants you to teach you:** why secrets belong in environment
variables/`.env` files and never in source code, and how to design configuration loading
that degrades safely when a value or a package isn't there.

**Concept:** Environment variables, `.env` files, secrets management.
Loads configuration from environment variables using `python-dotenv`. Demonstrates
different behavior for development vs production modes. Includes `.env.example` (safe
to commit) and `.gitignore` rules to prevent leaking secrets.

**Why it matters:** Hardcoding database passwords or API keys in source code is a
security disaster. Environment variables separate configuration from code. The 12-Factor
App methodology considers this essential for any deployable application.

**Evaluation checklist (Exercise 2):**

- [x] Required files present: `oracle.py`, `.env.example`, `.gitignore`.
- [x] `python-dotenv` declared in `requirements.txt` — the eval sheet's exact wording asks
      the learner to "Show that python-dotenv is declared in their requirements.txt (you
      can carry one over from ex1/)". `ex2/requirements.txt` now exists with
      `python-dotenv==1.0.1` (matching the version actually installed/importable in this
      environment, per `pip show python-dotenv`). It intentionally does NOT carry over
      `numpy`/`pandas`/`matplotlib`/`requests` from `ex1/requirements.txt`: `oracle.py`
      only imports `os` and `dotenv`, and ex2's own "Authorized" list
      (`os, sys, python-dotenv modules, file operations`) doesn't include those data-science
      libraries — listing them here would be unused, unauthorized bloat.
- [x] Uses `python-dotenv` to load `.env` files (`try_load_dotenv()` calls
      `load_dotenv()`, wrapped so a missing install degrades gracefully instead of
      crashing).
- [x] Loads configuration from environment variables (`load_config()` reads
      `MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL`, `ZION_ENDPOINT` via
      `os.environ`).
- [x] Handles missing configuration appropriately (every key falls back to a sane
      default: `'development'`, `'Not configured'`, `'No API key'`, `'INFO'`, `'Offline'`).
- [x] Shows loaded configuration without exposing real secrets (`API_KEY` is reported only
      as "Authenticated"/"No API key", never printed in full).
- [x] Demonstrates understanding of environment-based configuration (explicit
      development/production branch in `print_config()`).
- **Security implementation:**
  - [x] `.env.example` contains template/placeholder values only (`API_KEY` is left
        blank, `DATABASE_URL` points at a local sqlite path) — no real secrets.
  - [x] `.gitignore` excludes `.env` (first line), plus `matrix_env/`, `__pycache__/`,
        `*.pyc`.
  - [x] `oracle.py` has no hardcoded secrets — all sensitive values come from
        `os.environ`.
  - [x] `python-dotenv` is used correctly (`load_dotenv()` called before reading
        `os.environ`) and is now declared in `ex2/requirements.txt`.

> Verified: running `oracle.py` with no environment configured prints safe defaults and a
> `[WARNING] No API_KEY provided` notice; no real secret ever appears in the output.

**Subject-only audit (against `en.subject.txt` directly, not just the eval sheet):**

- [x] **Fixed** — `load_config()`/`print_config()` used `from typing import Dict`, which
      is not on ex2's `os, sys, python-dotenv modules, file operations` authorized list
      (the earlier eval-sheet pass only checked that `oracle.py` avoided `pandas`/`numpy`/
      etc., not that `typing` itself was off-list). Switched to the builtin
      `dict[str, str]` annotation, removing the import entirely.
- [x] Confirmed all 5 required configuration variables (`MATRIX_MODE`, `DATABASE_URL`,
      `API_KEY`, `LOG_LEVEL`, `ZION_ENDPOINT`) are read via `os.environ` — no subset.
- [x] Confirmed `.env` is literally listed in `ex2/.gitignore` (first line) and
      `.env.example` contains only placeholder values (blank `API_KEY`, local sqlite URL,
      `localhost` endpoint) — no real secrets.
- [x] Tested all three usage scenarios from the subject in an environment with
      `python-dotenv` installed: no config (safe defaults + `[WARNING] No API_KEY
      provided`), `.env` copied from `.env.example` (values loaded, `Mode: development`),
      and env-var override (`MATRIX_MODE=production API_KEY=... python oracle.py` correctly
      overrides to `Mode: production` / `[OK] Production overrides available`, taking
      precedence over any `.env` value as `load_dotenv()`'s default behavior does not
      override already-set environment variables).
- [x] Tested with `python-dotenv` *not* installed (`~/.venvs/lint`): `oracle.py` prints
      `python-dotenv not available. To enable .env loading, install python-dotenv` and
      still runs to completion with `os.environ`-only configuration — no crash. Confirmed
      with mypy that once `python-dotenv` is resolvable the file is 100% clean (no import
      exemption needed for ex2, unlike ex1).
- [x] **Fixed** — `print_config()` had a 109-character line, failing flake8's real
      default 79-column limit (there is no repo-wide `.flake8` overriding it — every
      module is linted with plain flake8 defaults). Split the single-line conditional
      print into an `if`/`else` block; behavior unchanged, verified by re-running
      `oracle.py`.

## Code Quality and Understanding (applies to all three exercises)

Per the official scale, this section is graded across the whole module, not per exercise:

- [x] Written for Python 3.10+ (`pyproject.toml` pins `python = "^3.10"`; no syntax used
      requires anything newer).
- [x] flake8-clean: `python -m flake8 ex0 ex1 ex2` reports zero errors with plain
      defaults (no config file, no line-length override, no ignored error codes).
- [x] Type hints on every function's parameters and return values across `construct.py`,
      `loading.py`, and `oracle.py` (e.g. `in_virtualenv() -> bool`,
      `load_config() -> dict[str, str]`, `print_dependency_report(statuses: dict[str,
      bool]) -> None`). All three now use builtin generics (`dict[str, str]`, `str | None`)
      rather than `typing.Dict`/`typing.Optional`, since `typing` itself is not on any of
      the three exercises' "Authorized" import lists and Python 3.10+ doesn't need it.
- Docstrings are **not required** for this module (per the subject) — none of the three
  scripts include them, which is compliant, not a gap.
- [x] Error handling: dependency imports and `dotenv` loading are wrapped in
  `try/except` so missing packages degrade to a helpful message instead of a crash.
- [x] Well-structured and readable: each script separates detection/loading logic from
  presentation (`*_report`/`print_*` functions) and gates on `if __name__ == '__main__':`.

## Defense Prep — Questions From the Evaluation Sheet

The bullets below restate the eval sheet's "Be ready to explain" items as the underlying
question the evaluator is likely to ask, paired with the talking points already
established in the checklists above.

### Exercise 0

*What is a virtual environment, why does it matter, and what problems does it solve?*

- Problems it solves: dependency/version conflicts between projects.
- Exactly how the program detects one: the `sys.prefix` vs `sys.base_prefix` comparison,
  plus the `VIRTUAL_ENV` environment variable as a fallback.

### Exercise 1

*What's the difference between pip and Poetry, and why does dependency management
matter?*

- How the program handles missing dependencies (graceful `[OK]`/`[MISSING]` reporting
  instead of crashing).
- How the data is simulated — via `numpy` (`np.random.normal`), not hardcoded.

### Exercise 2

*Why do environment variables matter for security, and how does the program use them?*

- Dev vs. production configuration (the explicit branch in `print_config()`).
- How `python-dotenv` helps (`load_dotenv()` loads `.env` into `os.environ`).
- How missing configuration is handled (sane defaults per key, no crash).

*Why must secrets never be committed to source control?*

- How env vars enable per-environment configuration.
- The role of `python-dotenv` in bridging `.env` files and `os.environ`.
- The security implications of configuration management in general.

### Overall Understanding

The learner should be able to explain, beyond just making the code run:

1. How virtual environments, package management, and environment variables work together
   in a real data engineering project.
2. Why each of these tools matters for professional development.
3. What breaks without them (dependency conflicts, "works on my machine," leaked
   credentials).
4. How they would bootstrap a new data engineering project using all three concepts
   together (venv → declare deps in `requirements.txt`/`pyproject.toml` → load secrets via
   `.env` + `python-dotenv`).

## Key Takeaways

- **Virtual environments** isolate project dependencies — always use one.
- **`requirements.txt`** pins versions for pip; **`pyproject.toml`** is the modern standard.
  Pinning only works if the versions are actually written down — `ex1/requirements.txt`
  now pins exact versions matching `pyproject.toml`.
- **Environment variables** keep secrets out of source code.
- **`.env` files** provide development defaults; `.gitignore` prevents committing real secrets.
- Every dependency a script actually imports (including `python-dotenv`) belongs in the
  dependency file the grader is told to check, and nothing else does — `ex2/requirements.txt`
  declares only `python-dotenv`, since that's the only third-party import `oracle.py`
  actually makes.
- These practices are non-negotiable in professional Python development.
- Understanding your environment (Python path, site-packages, active venv) helps debug
  import issues and version conflicts.
