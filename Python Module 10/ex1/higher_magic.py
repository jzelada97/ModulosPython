from collections.abc import Callable
from typing import List, Any


def spell_combiner(spell1: Callable[[str,int], str], spell2: Callable[[str,int], str]) -> Callable[[str,int], tuple]:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str,int], str], multiplier: int) -> Callable[[str,int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str,int], bool], spell: Callable[[str,int], str]) -> Callable[[str,int], str]:
    def wrapped(target: str, power: int) -> str:
        try:
            if condition(target, power):
                return spell(target, power)
            return 'Spell fizzled'
        except Exception:
            return 'Spell fizzled'
    return wrapped


def spell_sequence(spells: List[Callable[[str,int], str]]) -> Callable[[str,int], List[str]]:
    def seq(target: str, power: int) -> List[str]:
        return [s(target, power) for s in spells]
    return seq


# Example simple spells
def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def main() -> None:
    print('Testing spell combiner...')
    combined = spell_combiner(fireball, heal)
    print('Combined spell result:', combined('Dragon', 10))

    print('Testing power amplifier...')
    mega = power_amplifier(fireball, 3)
    print('Original: 10, Amplified:', mega('Orc', 10))

    print('Testing conditional caster...')
    cond = conditional_caster(lambda t,p: p > 5, fireball)
    print(cond('Goblin', 3))
    print(cond('Goblin', 6))

    print('Testing spell sequence...')
    seq = spell_sequence([fireball, heal])
    print(seq('Hero', 8))


if __name__ == '__main__':
    main()
