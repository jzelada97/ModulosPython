print('*** Tournament ***')
from ex0 import FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy


def battle(opponents):
    print(f"{len(opponents)} opponents involved")
    for i, (factory, strategy) in enumerate(opponents):
        for j, (factory2, strategy2) in enumerate(opponents):
            if i >= j:
                continue
            c1 = factory().create_base()
            c2 = factory2().create_base()
            print('* Battle *')
            print(c1.describe())
            print('vs.')
            print(c2.describe())
            print('now fight!')
            try:
                strategy().act(c1)
                strategy2().act(c2)
            except Exception as e:
                raise RuntimeError(f"Battle error, aborting tournament: {e}")


if __name__ == '__main__':
    # Simple tournament
    print('Tournament 0 (basic)')
    ops = [(FlameFactory, NormalStrategy), (HealingCreatureFactory, DefensiveStrategy)]
    print(ops)
    battle(ops)

    # Error tournament
    print('Tournament 1 (error)')
    ops = [(FlameFactory, AggressiveStrategy), (HealingCreatureFactory, DefensiveStrategy)]
    print(ops)
    try:
        battle(ops)
    except RuntimeError as e:
        print(e)

    # Multiple tournament
    print('Tournament 2 (multiple)')
    ops = [
        (FlameFactory, NormalStrategy),
        (HealingCreatureFactory, DefensiveStrategy),
        (TransformCreatureFactory, AggressiveStrategy),
    ]
    print(ops)
    battle(ops)
