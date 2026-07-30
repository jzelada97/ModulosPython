print('Testing factory')
from ex0 import FlameFactory, AquaFactory


def test_factory(factory):
    f = factory()
    base = f.create_base()
    evolved = f.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


if __name__ == '__main__':
    test_factory(FlameFactory)
    test_factory(AquaFactory)
    print('Testing battle')
    f1 = FlameFactory().create_base()
    f2 = AquaFactory().create_base()
    print(f1.describe())
    print('vs.')
    print(f2.describe())
    print('fight!')
    print(f1.attack())
    print(f2.attack())
