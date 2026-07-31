from functools import wraps
from time import perf_counter
from typing import Callable


def timing_decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {(end - start):.6f}s")
        return result
    return wrapper


def repeat(times: int) -> Callable:
    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = []
            for _ in range(times):
                res.append(func(*args, **kwargs))
            return res
        return wrapper
    return deco


def authenticated(required_role: str):
    def deco(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(user_role: str, *args, **kwargs):
            if user_role != required_role:
                return 'Access denied'
            return func(user_role, *args, **kwargs)
        return wrapper
    return deco


class SpellBook:
    spells: list[str] = []

    @classmethod
    def add_spell(cls, name: str) -> None:
        cls.spells.append(name)

    @staticmethod
    def format_spell(name: str) -> str:
        return f"Spell::{name}"


@timing_decorator
def cast_spell(name: str) -> str:
    return f"Casting {name}"


@repeat(3)
def echo_spell(name: str) -> str:
    return f"Echo {name}"


@authenticated('archmage')
def secret_spell(role: str, name: str) -> str:
    return f"{role} casts {name}"


def main() -> None:
    print(cast_spell('Fireball'))
    print(echo_spell('Ping'))
    print(secret_spell('novice', 'Shadow'))
    print(secret_spell('archmage', 'Shadow'))
    SpellBook.add_spell('Fireball')
    print(SpellBook.format_spell('Fireball'))


if __name__ == '__main__':
    main()
