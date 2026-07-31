from .elements import create_air
from . import potions
from . import transmutation  # noqa: F401

# Expose only create_air and a package-level alias for healing
__all__ = ['create_air', 'potions', 'transmutation']

# Package alias
heal = potions.healing_potion
