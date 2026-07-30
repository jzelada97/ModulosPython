from functools import reduce, partial, wraps, lru_cache
from typing import Callable, Any, Dict, List
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    ops = {
        'sum': operator.add,
        'mul': operator.mul,
        'max': lambda a, b: a if a > b else b,
        'min': lambda a, b: a if a < b else b,
    }
    if not spells:
        return 0
    op = ops.get(operation)
    if op is None:
        raise ValueError('Unsupported operation')
    return reduce(op, spells)


def partial_enchanter(base_enchantment: Callable[[str, int], str]) -> Dict[str, Callable]:
    return {
        'weak': partial(base_enchantment, power=1),
        'normal': partial(base_enchantment, power=5),
        'strong': partial(base_enchantment, power=10),
    }


def memoized_fibonacci(n: int) -> int:
    @lru_cache(maxsize=None)
    def fib(k: int) -> int:
        if k < 2:
            return k
        return fib(k-1) + fib(k-2)
    return fib(n)


def spell_dispatcher() -> Callable[[Any], str]:
    dispatch_map = {
        int: lambda v: f'Int spell: {v}',
        str: lambda v: f'String spell: {v}',
        list: lambda v: f'List spell with {len(v)} items'
    }
    def dispatcher(value: Any) -> str:
        handler = dispatch_map.get(type(value), lambda v: 'Unknown spell type')
        return handler(value)
    return dispatcher


def main() -> None:
    print('Testing spell reducer...')
    print('sum:', spell_reducer([1,2,3,4], 'sum'))
    print('mul:', spell_reducer([1,2,3,4], 'mul'))

    print('Testing partial enchanter...')
    def base_enchant(item: str, power: int) -> str:
        return f'{item} enchanted with power {power}'
    parts = partial_enchanter(base_enchant)
    print(parts['weak']('Dagger'))
    print(parts['strong']('Greatsword'))

    print('Testing memoized fibonacci...')
    print(memoized_fibonacci(10))

    print('Testing spell dispatcher...')
    d = spell_dispatcher()
    print(d(5))
    print(d('echo'))
    print(d([1,2,3]))


if __name__ == '__main__':
    main()
