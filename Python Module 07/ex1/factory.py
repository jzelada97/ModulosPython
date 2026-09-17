from __future__ import annotations
from ex0.factory import CreatureFactory
from ex1.capabilities import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    # Narrowed (covariant) return types: every Creature this factory
    # produces actually has HealCapability's heal(), so callers can use
    # it without an unsafe cast or a `# type: ignore`.
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling()

    def create_evolved(self) -> Morphagon:
        return Morphagon()
