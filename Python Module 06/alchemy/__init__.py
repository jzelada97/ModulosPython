from .elements import create_air
from . import potions
from . import transmutation  # noqa: F401
from .transmutation.recipes import lead_to_gold  # noqa: F401

# Expose create_air, potions, transmutation and lead_to_gold.
# create_earth is intentionally NOT imported here, so it stays
# unreachable as alchemy.create_earth (AttributeError).
__all__ = ['create_air', 'potions', 'transmutation', 'lead_to_gold']

# Package alias
heal = potions.healing_potion
