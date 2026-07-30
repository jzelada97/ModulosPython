from __future__ import annotations
import os
import sys
# Ensure module root is on sys.path so sibling package ex0 is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from capabilities import Sproutling, Bloomelle, Shiftling, Morphagon
from ex0.creature import Creature
from ex0.factory import CreatureFactory


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
