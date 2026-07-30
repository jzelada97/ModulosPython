from typing import List


def light_spell_allowed_ingredients() -> List[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # Validate via validator without importing spellbook (no circular import)
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)
    # result contains '... VALID' or '... INVALID'
    if 'VALID' in result:
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
