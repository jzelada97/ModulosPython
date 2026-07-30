from .elements import create_air
from . import potions

# Expose only create_air and a package-level alias for healing
__all__ = ['create_air', 'potions']

# Package alias
heal = potions.healing_potion
