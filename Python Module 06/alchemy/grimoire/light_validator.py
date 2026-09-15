from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lower = ingredients.lower()
    valid = any(a in lower for a in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
