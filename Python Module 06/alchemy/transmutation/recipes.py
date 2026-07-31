from alchemy.elements import create_air  # absolute import
from ..potions import strength_potion  # relative import
from elements import create_fire  # absolute import from root


def lead_to_gold() -> str:
    part1 = create_air()
    part2 = strength_potion()
    part3 = create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{part1}' and '{part2}' "
        f"mixed with '{part3}'"
    )
