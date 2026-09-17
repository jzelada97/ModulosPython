from ex0 import FlameFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy,
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    print(f"{len(opponents)} opponents involved")
    for i, (factory, strategy) in enumerate(opponents):
        for j, (factory2, strategy2) in enumerate(opponents):
            if i >= j:
                continue
            c1 = factory.create_base()
            c2 = factory2.create_base()
            print('* Battle *')
            print(c1.describe())
            print('vs.')
            print(c2.describe())
            print('now fight!')
            try:
                strategy.act(c1)
                strategy2.act(c2)
            except Exception as e:
                raise RuntimeError(f"Battle error, aborting tournament: {e}")


if __name__ == '__main__':
    print('*** Tournament ***')
    print('Tournament 0 (basic)')
    ops = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    print([(type(f).__name__, type(s).__name__) for f, s in ops])
    battle(ops)

    print('Tournament 1 (error)')
    ops = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    print([(type(f).__name__, type(s).__name__) for f, s in ops])
    try:
        battle(ops)
    except RuntimeError as e:
        print(e)

    print('Tournament 2 (multiple)')
    ops = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    print([(type(f).__name__, type(s).__name__) for f, s in ops])
    battle(ops)
