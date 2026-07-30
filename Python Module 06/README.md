Module 06 — The Codex (Import Mysteries)

Files added to demonstrate package/module import patterns, absolute vs relative imports, and circular dependency examples.

Key files:
- `elements.py` (root): `create_fire()`, `create_water()`
- `alchemy/` package with `elements.py`, `potions.py`, `transmutation/recipes.py`, and `grimoire/` validators and spellbooks.
- Test scripts starting with `ft_alembic_*.py`, `ft_distillation_*.py`, `ft_transmutation_*.py`, `ft_kaboom_*.py`.

Notes:
- `alchemy/__init__.py` intentionally exposes only `create_air` and `potions.healing_potion` as `heal` to demonstrate limited package interface.
- `alchemy/grimoire/dark_*` files intentionally create a circular import to raise an ImportError when imported.
