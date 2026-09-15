from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def run_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print('Testing battle')
    f1 = factory1.create_base()
    f2 = factory2.create_base()
    print(f1.describe())
    print('vs.')
    print(f2.describe())
    print('fight!')
    print(f1.attack())
    print(f2.attack())


if __name__ == '__main__':
    print('Testing factory')
    test_factory(FlameFactory())
    test_factory(AquaFactory())
    run_battle(FlameFactory(), AquaFactory())
