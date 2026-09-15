from typing import List


def light_spell_allowed_ingredients() -> List[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # Deferred import: light_validator imports light_spell_allowed_ingredients
    # from this module at its top level, so this module must finish loading
    # before light_validator is imported (no circular import).
    from .light_validator import validate_ingredients
    result = validate_ingredients(ingredients)
    # result contains '... VALID' or '... INVALID'
    if 'VALID' in result:
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
