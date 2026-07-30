# Intentional circular import: import validator which imports back this module
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if 'VALID' in result:
        return f"Dark spell recorded: {spell_name} ({ingredients} - VALID)"
    return f"Dark spell rejected: {spell_name} ({ingredients} - INVALID)"
