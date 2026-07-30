from collections.abc import Callable
from typing import Dict


def mage_counter() -> Callable[[], int]:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    total = initial_power
    def add(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return add


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchanter(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchanter


def memory_vault() -> Dict[str, Callable]:
    store: Dict[str, object] = {}
    def _store(key: str, value: object) -> None:
        store[key] = value
    def _recall(key: str) -> object:
        return store.get(key, 'Memory not found')
    return {'store': _store, 'recall': _recall}


def main() -> None:
    print('Testing mage counter...')
    a = mage_counter()
    b = mage_counter()
    print('counter_a call 1:', a())
    print('counter_a call 2:', a())
    print('counter_b call 1:', b())

    print('Testing spell accumulator...')
    acc = spell_accumulator(100)
    print('Base 100, add 20:', acc(20))
    print('Base 100, add 30:', acc(30))

    print('Testing enchantment factory...')
    flaming = enchantment_factory('Flaming')
    frozen = enchantment_factory('Frozen')
    print(flaming('Sword'))
    print(frozen('Shield'))

    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store'secret'=", vault['recall']('secret'))
    print("Recall'unknown':", vault['recall']('unknown'))


if __name__ == '__main__':
    main()
