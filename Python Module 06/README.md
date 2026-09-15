# Module 06 — The Codex: Mastering Python Imports

## Overview

This module demystifies Python's import system through an alchemy-themed lab. You build
a package from scratch and explore the four import challenges: package initialization,
nested imports, absolute vs relative paths, and circular dependencies.

This README also doubles as a self-check against the official 42 evaluation scale for
*Python Module 06*: every bullet the evaluator is told to verify is reproduced below,
next to the file(s) that are supposed to satisfy it.

## Structure

```
elements.py              (root-level module: create_fire, create_water)
alchemy/
  __init__.py            (package gateway: controls what's exposed)
  elements.py            (create_earth, create_air)
  potions.py             (uses both root and package elements)
  transmutation/
    __init__.py
    recipes.py           (absolute + relative imports combined)
  grimoire/
    __init__.py
    light_spellbook.py   (avoids circular dependency)
    light_validator.py
    dark_spellbook.py    (intentional circular dependency)
    dark_validator.py
```

## Preliminaries (before the defense even starts)

The evaluator is asked to confirm, before looking at any exercise:

- The Git repository is the learner's own, cloned into an empty folder.
- No aliases were set up to disguise what is actually being graded.
- The project structure matches the subject's expected file tree (root-level
  `elements.py` + `ft_alembic_*.py` / `ft_distillation_*.py` / `ft_transmutation_*.py` /
  `ft_kaboom_*.py`, plus the `alchemy/` package with `elements.py`, `potions.py`,
  `transmutation/`, and `grimoire/`).
- Only the files the subject actually asks for are present (no stray scratch files).

## Parts & Learning Objectives

### Part I: The Alembic (`ft_alembic_0.py` through `ft_alembic_5.py`)
**Concept:** Basic import mechanisms — `import X` vs `from X import Y`, accessing
local files vs package submodules.

**What this part wants you to teach you:** the mechanical difference between
`import X` (you get a namespace, and must qualify every access as `X.name`) and
`from X import Y` (you get the name `Y` directly, bound into your own namespace) —
and, layered on top of that, that `__init__.py` is what decides which names inside a
package are actually reachable from outside it, regardless of what really exists in
the package's source files.

- `ft_alembic_0/1` — importing from a root-level `.py` file directly.
- `ft_alembic_2/3` — importing from inside a package (`alchemy/elements.py`).
- `ft_alembic_4` — using `import alchemy` and discovering that `__init__.py` controls
  what the package exposes. `create_earth` exists but isn't accessible via `alchemy.create_earth`.
- `ft_alembic_5` — `from alchemy import create_air` uses what `__init__.py` exports.

**Key insight:** `__init__.py` is the gatekeeper. It decides the package's public API.

**Evaluation checklist (Part I — Alembic experiment):**
- [x] `python3 ft_alembic_0.py` runs `import elements` and calls `elements.create_fire()`.
- [x] `python3 ft_alembic_1.py` runs `from elements import create_water` and calls `create_water()`.
- [x] `python3 ft_alembic_2.py` runs `import alchemy.elements` and calls `alchemy.elements.create_earth()`.
- [x] `python3 ft_alembic_3.py` runs `from alchemy.elements import create_air` and calls `create_air()`.
- [x] `python3 ft_alembic_4.py` runs `import alchemy`, calls `alchemy.create_air()`, then attempts
  `alchemy.create_earth()` — the subject allows this to raise uncaught; here it is caught in a
  `try/except AttributeError` and explained instead of crashing.
- [x] `python3 ft_alembic_5.py` runs `from alchemy import create_air` and calls `create_air()`.
- [x] `alchemy/__init__.py` has an `__init__.py`, imports `create_air` from `.elements`, and
  does **not** import `create_earth` (so it stays unreachable as `alchemy.create_earth`).

### Part II: Distillation (`ft_distillation_0.py`, `ft_distillation_1.py`)
**Concept:** Nested imports, package-level aliases.

**What this part wants you to teach you:** how a single module (`potions.py`) can pull
symbols in from two different places at once — a root-level absolute import and a
package-relative import — and how a package's `__init__.py` can re-export and rename
(alias) things it imports, so callers get a simpler, curated API instead of having to
know the real internal module layout.

- `potions.py` imports from both root `elements.py` (absolute) and `alchemy/elements.py`
  (relative within package).
- `__init__.py` can create aliases (`heal = potions.healing_potion`) to simplify access.

**Key insight:** Packages can re-export and rename things to create a cleaner API.

**Evaluation checklist (Part II — Distillation experiment):**
- [x] `python3 ft_distillation_0.py` accesses `alchemy/potions.py` directly
  (`from alchemy.potions import strength_potion, healing_potion`) and exercises both potions.
- [x] `python3 ft_distillation_1.py` uses the `alchemy` module directly and exercises the
  strength potion (`alchemy.potions.strength_potion()`).
- [x] The healing potion is called through the `heal()` alias in `ft_distillation_1.py`
  (`alchemy.heal()`).
- [x] `alchemy/__init__.py` has been updated to expose the potions (`from . import potions`)
  and to define the `heal` alias (`heal = potions.healing_potion`).
- [x] `alchemy/potions.py` imports elements from **both** places: `from elements import
  create_fire, create_water` (root, absolute) and `from .elements import create_earth,
  create_air` (package, relative).
- [x] `strength_potion()` / `healing_potion()` return the exact strings from the subject,
  spaces included: `"Strength potion brewed with 'Fire element created' and 'Water element
  created'"` and `"Healing potion brewed with 'Earth element created' and 'Air element
  created'"` (verified against `en.subject.pdf` with `pdftotext -layout`, since the
  plain-text extraction of the subject collapses the spaces around the quotes).

### Part III: Transmutation (`ft_transmutation_0/1/2.py`)
**Concept:** Absolute vs relative imports within a package.

**What this part wants you to teach you:** that the same function can be reached
through several different import paths (module, sub-package, or top-level package),
and that absolute imports (full dotted path from the project root) and relative
imports (dot-prefixed, relative to the current package) are two different tools —
each with a context where it is the more explicit or more convenient choice.

- `recipes.py` demonstrates both: `from alchemy.elements import create_air` (absolute)
  and `from ..potions import strength_potion` (relative).
- All three test scripts import the same function through different paths.

**Key insight:** Absolute imports are explicit and clear. Relative imports are shorter
but only work within a package. Both have their place.

**Evaluation checklist (Part III — Transmutation experiment):**
- [x] `ft_transmutation_0.py` reaches `lead_to_gold` via the `recipes` module, using the
  subject-mandated `import ...` structure (not `from ... import ...`):
  `import alchemy.transmutation.recipes` → `alchemy.transmutation.recipes.lead_to_gold()`.
- [x] `ft_transmutation_1.py` reaches it via the `transmutation` module
  (`import alchemy.transmutation as trans` → `trans.recipes.lead_to_gold()`).
- [x] `ft_transmutation_2.py` reaches it via the `alchemy` module
  (`import alchemy` → `alchemy.lead_to_gold()`, using the top-level exposure from
  `alchemy/__init__.py`).
- [x] `alchemy/transmutation/__init__.py` exists (re-exports `recipes`).
- [x] `alchemy/__init__.py` is updated to expose `lead_to_gold`
  (`from .transmutation.recipes import lead_to_gold`), added alongside the existing
  `create_air`, `potions`, and `transmutation` exposures — `create_earth` stays
  unimported, so it remains hidden. `ft_transmutation_2.py` now calls it directly as
  `alchemy.lead_to_gold()` to demonstrate the top-level exposure (verified:
  `hasattr(alchemy, "lead_to_gold")` is `True`, `hasattr(alchemy, "create_earth")` is
  still `False`).
- [x] `alchemy/transmutation/recipes.py` contains at least one absolute import
  (`from alchemy.elements import create_air`, `from elements import create_fire`) and
  one relative import (`from ..potions import strength_potion`).

### Part IV: Kaboom (`ft_kaboom_0.py`, `ft_kaboom_1.py`)
**Concept:** Circular dependencies — what they are and how to avoid them.

**What this part wants you to teach you:** why circular imports break at module-load
time (two modules each needing the other before either has finished initializing),
how to recognize the pattern that causes it by comparing a working pair against a
broken one, and how to recognize/avoid it in practice — here, via a deferred
(function-local) import instead of a top-level one.

- `ft_kaboom_0` — Light magic works because `light_validator.py` doesn't import back
  from `light_spellbook.py` (uses a deferred import inside the function).
- `ft_kaboom_1` — Dark magic explodes because `dark_spellbook.py` imports
  `dark_validator.py` which imports `dark_spellbook.py` back — an infinite loop.

**Key insight:** Circular imports happen when A needs B and B needs A at module load time.
Solutions: deferred imports (import inside a function), restructuring, or dependency inversion.

**Evaluation checklist (Part IV — Circular experiment):**
- [x] Across the two scripts, one import works (`ft_kaboom_0.py`, light path) and one fails
  (`ft_kaboom_1.py`, dark path, uncaught `ImportError` — confirmed by actually running it:
  `ImportError: cannot import name 'dark_spell_allowed_ingredients' from partially
  initialized module 'alchemy.grimoire.dark_spellbook' (most likely due to a circular import)`).
- [x] `alchemy/grimoire/` contains `__init__.py`, `light_spellbook.py`, `light_validator.py`,
  `dark_spellbook.py`, and `dark_validator.py`.
- [x] Dark pair: ingredients are defined in `dark_spellbook.py`
  (`dark_spell_allowed_ingredients()`) and only *read* by `dark_validator.py` — yet
  `dark_spellbook.py` also imports `dark_validator.py`, so the two files need each other
  (the circular dependency that makes `ft_kaboom_1.py` explode).
- [x] Light pair: `light_spellbook.light_spell_record('Fantasy', 'Earth, wind and fire')`
  records the spell as `VALID` (matches the subject's "Earth, Wind & Fire" / "Fantasy" example;
  wording differs slightly but the validated elements — earth and fire — are the same).
  `light_validator.py` now imports `light_spell_allowed_ingredients()` from
  `light_spellbook.py` (a plain top-level import) instead of hardcoding its own copy of the
  list, so the ingredient list is defined once, in the spellbook — matching the dark pair's
  approach. This stays non-circular because `light_spellbook.py` only imports
  `light_validator.py` with a *deferred* import inside `light_spell_record` (not at module
  level), so `light_spellbook` always finishes loading before `light_validator` needs it.

## Code Quality and Understanding

The scale grades code quality independently of the four parts above:

- **Python version:** all modules use 3.10+ compatible syntax (e.g. builtin generics
  like `list[str]` in `alchemy/grimoire/dark_spellbook.py`); verified running under
  Python 3.12.
- **flake8:** clean with no ignores at all — verified with
  `flake8 --isolated --max-line-length=99` (bypassing the monorepo-root `.flake8` entirely,
  simulating a fresh clone of just this project). All `ft_*.py` scripts now import first and
  print their banner/description lines afterward, so `E402` no longer fires anywhere. The one
  intentional exception is `ft_kaboom_1.py`: its narration ("THIS WILL RAISE AN UNCAUGHT
  EXCEPTION") must print *before* the import that actually raises the `ImportError`, so the
  import stays below those prints with a scoped `# noqa: E402` and an explanatory comment —
  reordering it would silently drop those lines from the transcript. The long lines
  previously in `ft_alembic_4.py` (around lines 10 and 13) were wrapped; `ft_kaboom_0.py`
  was already within the 99-column limit.
- **Type annotations (mypy):** every function in the library modules (`elements.py`,
  `alchemy/elements.py`, `alchemy/potions.py`, `alchemy/transmutation/recipes.py`,
  `alchemy/grimoire/*.py`) has parameter and return annotations; verified with
  `mypy --strict` (0 errors across 23 of the 24 source files). `ft_alembic_4.py` is the
  subject's documented exception: it accesses `alchemy.create_earth()` on purpose, and the
  subject is explicit that "*A mypy error will also raise, again, on purpose*" — so this
  file is **not** silenced with `# type: ignore`; running
  `mypy --strict ft_alembic_4.py` intentionally reports
  `error: Module has no attribute "create_earth"; maybe "create_air"? [attr-defined]`,
  matching the subject's own AttributeError example (`Did you mean: 'create_air'?`).
- **Docstrings:** explicitly NOT required by the subject for this module — none are used.
- **Overall organization:** one script per import scenario, one concern per file inside
  `alchemy/`, consistent naming (`ft_<part>_<n>.py`) — matches the "clean and professional"
  bar the scale asks about.

## Defense Prep — Questions From the Evaluation Sheet

Flashcard-style prep for the "be ready to explain, live" bullets pulled out of the
checklists above. Each question is followed by the talking point to give out loud.

### Part I — Alembic

*"Why does `alchemy.create_earth()` fail even though `create_earth` is a real function
in `alchemy/elements.py`?"*
- `alchemy/__init__.py` only imports `create_air` from `.elements` — it never imports
  `create_earth`. A package's `__init__.py` is the gatekeeper for what's reachable as
  `alchemy.<name>`; a function can be fully defined and working inside
  `alchemy/elements.py` and still be invisible from `alchemy.<name>` if `__init__.py`
  never brings it in. That's exactly why `ft_alembic_4.py` gets an `AttributeError`
  (caught and explained here rather than left to crash).

### Part II — Distillation

*"What's the difference between the absolute import of the root `elements.py` and the
relative import of `alchemy/elements.py` inside `potions.py`?"*
- `alchemy/potions.py` imports `create_fire, create_water` from the root-level
  `elements.py` using an **absolute** import (`from elements import ...`) because that
  file lives outside the `alchemy` package. It imports `create_earth, create_air` from
  `alchemy/elements.py` using a **relative** import (`from .elements import ...`)
  because that file lives inside the same package — the leading dot means "look in my
  own package" rather than spelling out the full path.

### Part III — Transmutation

*"When do you reach for an absolute import vs. a relative one?"*
- Absolute imports spell out the full path from the project root
  (`from alchemy.elements import create_air`) — more explicit and unambiguous, and they
  keep working no matter where the importing file itself lives. Relative imports use
  leading dots (`from ..potions import strength_potion`) to say "relative to my current
  package" — shorter to write, but they only work for code that is itself part of a
  package (they break if the file is ever run as a standalone script). `recipes.py`
  demonstrates both side by side.

### Part IV — Kaboom

*"What is a circular dependency, why does Python raise `ImportError` on a partially
initialized module, and which fix was chosen here?"*
- A circular dependency happens when module A needs something from module B while B
  is loading, and B needs something from A while A is loading — each is waiting on the
  other to finish first. Python starts executing a module top-to-bottom the first time
  it's imported; if, partway through, that module's own import statement pulls in a
  second module which then tries to import a name back out of the *first* module before
  it has finished running (and therefore before that name has been defined), Python
  raises `ImportError` on the "partially initialized module." That's exactly the dark
  pair: `dark_spellbook.py` imports `dark_validator.py`, which imports back from
  `dark_spellbook.py`, so `ft_kaboom_1.py` explodes. The fix used here is a **deferred
  (local) import**: `light_spellbook.py` only imports `light_validator.py` inside the
  `light_spell_record` function body, not at module level, so `light_spellbook` always
  finishes loading completely before `light_validator` is ever needed — as opposed to
  the alternative fixes of restructuring the modules or merging them together.

## Key Takeaways

- `__init__.py` turns a folder into a package and controls its public interface.
- `import X` makes `X` available as a namespace; `from X import Y` pulls `Y` directly.
- Absolute imports use the full package path; relative imports use dots (`..`).
- Circular dependencies are a design smell — resolve them by restructuring or deferring imports.
- Understanding imports is essential for scaling Python projects beyond single files.
- For the defense: see **Defense Prep — Questions From the Evaluation Sheet** above for
  the full set of "explain it out loud" talking points, part by part.
