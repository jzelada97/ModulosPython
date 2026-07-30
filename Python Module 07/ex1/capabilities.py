from __future__ import annotations
import os
import sys
# Ensure module root is on sys.path so sibling package ex0 is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import abc
from abc import ABC, abstractmethod
from typing import Any
from ex0.creature import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Any = None) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


# Concrete healing creatures
class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__('Sproutling', 'Grass')

    def attack(self) -> str:
        return 'Sproutling uses Vine Whip!'

    def heal(self, target: Any = None) -> str:
        return 'Sproutling heals itself for a small amount'


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__('Bloomelle', 'Grass/Fairy')

    def attack(self) -> str:
        return 'Bloomelle uses Petal Dance!'

    def heal(self, target: Any = None) -> str:
        return 'Bloomelle heals itself and others for a large amount'


# Concrete transforming creatures
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, 'Shiftling', 'Normal')
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return 'Shiftling performs a boosted strike!'
        return 'Shiftling attacks normally.'

    def transform(self) -> str:
        self.transformed = True
        return 'Shiftling shifts into a sharper form!'

    def revert(self) -> str:
        self.transformed = False
        return 'Shiftling returns to normal.'


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, 'Morphagon', 'Normal/Dragon')
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.transformed:
            return 'Morphagon unleashes a devastating morph strike!'
        return 'Morphagon attacks normally.'

    def transform(self) -> str:
        self.transformed = True
        return 'Morphagon morphs into a dragonic battle form!'

    def revert(self) -> str:
        self.transformed = False
        return 'Morphagon stabilizes its form.'
