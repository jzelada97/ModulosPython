from alchemy.elements import create_air  # absolute import
from ..potions import strength_potion  # relative import


def lead_to_gold() -> str:
    return f"Recipe transmuting Lead to Gold: brew '{create_air()}' and '{strength_potion()}' mixed with '{create_air()}'"
