# Module 06 — The Codex: Mastering Python Imports

## Overview

This module demystifies Python's import system through an alchemy-themed lab. You build
a package from scratch and explore the four import challenges: package initialization,
nested imports, absolute vs relative paths, and circular dependencies.

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

## Parts & Learning Objectives

### Part I: The Alembic (`ft_alembic_0.py` through `ft_alembic_5.py`)
**Concept:** Basic import mechanisms — `import X` vs `from X import Y`, accessing
local files vs package submodules.

- `ft_alembic_0/1` — importing from a root-level `.py` file directly.
- `ft_alembic_2/3` — importing from inside a package (`alchemy/elements.py`).
- `ft_alembic_4` — using `import alchemy` and discovering that `__init__.py` controls
  what the package exposes. `create_earth` exists but isn't accessible via `alchemy.create_earth`.
- `ft_alembic_5` — `from alchemy import create_air` uses what `__init__.py` exports.

**Key insight:** `__init__.py` is the gatekeeper. It decides the package's public API.

### Part II: Distillation (`ft_distillation_0.py`, `ft_distillation_1.py`)
**Concept:** Nested imports, package-level aliases.

- `potions.py` imports from both root `elements.py` (absolute) and `alchemy/elements.py`
  (relative within package).
- `__init__.py` can create aliases (`heal = potions.healing_potion`) to simplify access.

**Key insight:** Packages can re-export and rename things to create a cleaner API.

### Part III: Transmutation (`ft_transmutation_0/1/2.py`)
**Concept:** Absolute vs relative imports within a package.

- `recipes.py` demonstrates both: `from alchemy.elements import create_air` (absolute)
  and `from ..potions import strength_potion` (relative).
- All three test scripts import the same function through different paths.

**Key insight:** Absolute imports are explicit and clear. Relative imports are shorter
but only work within a package. Both have their place.

### Part IV: Kaboom (`ft_kaboom_0.py`, `ft_kaboom_1.py`)
**Concept:** Circular dependencies — what they are and how to avoid them.

- `ft_kaboom_0` — Light magic works because `light_validator.py` doesn't import back
  from `light_spellbook.py` (uses a deferred import inside the function).
- `ft_kaboom_1` — Dark magic explodes because `dark_spellbook.py` imports
  `dark_validator.py` which imports `dark_spellbook.py` back — an infinite loop.

**Key insight:** Circular imports happen when A needs B and B needs A at module load time.
Solutions: deferred imports (import inside a function), restructuring, or dependency inversion.

## Key Takeaways

- `__init__.py` turns a folder into a package and controls its public interface.
- `import X` makes `X` available as a namespace; `from X import Y` pulls `Y` directly.
- Absolute imports use the full package path; relative imports use dots (`..`).
- Circular dependencies are a design smell — resolve them by restructuring or deferring imports.
- Understanding imports is essential for scaling Python projects beyond single files.
