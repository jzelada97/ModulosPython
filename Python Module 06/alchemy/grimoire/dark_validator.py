# Circular import: this imports dark_spellbook which imports this module
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    lower = ingredients.lower()
    valid = any(a in lower for a in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
