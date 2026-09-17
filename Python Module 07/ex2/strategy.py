from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Any) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return True

    def act(self, creature: Any) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return (
            hasattr(creature, 'transform') and hasattr(creature, 'revert')
        )

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature'{creature.name}'"
                "for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, 'heal')

    def act(self, creature: Any) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature'{creature.name}'for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
