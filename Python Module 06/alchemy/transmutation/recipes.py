from alchemy.elements import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    part1 = create_air()
    part2 = strength_potion()
    part3 = create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{part1}' and '{part2}' "
        f"mixed with '{part3}'"
    )
