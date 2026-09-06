# Module 10 — FuncMage: Functional Programming

## Overview

This module explores functional programming paradigms in Python. Functions become
first-class citizens — passed as arguments, returned from other functions, and stored
in variables. These patterns produce elegant, composable, and reusable code.

## Exercises & Learning Objectives

### ex0 — `lambda_spells.py`
**Concept:** Lambda expressions, `map()`, `filter()`, `sorted()` with key functions.
Anonymous functions (lambdas) are one-line expressions used for simple transformations.
Combined with `map()`, `filter()`, and `sorted()`, they enable data transformation
without defining named functions for trivial operations.

**Key insight:** Lambdas shine for short, throwaway operations. If the logic needs
a name or exceeds one expression, use `def`.

### ex1 — `higher_magic.py`
**Concept:** Higher-order functions — functions that accept/return functions.
- `spell_combiner`: returns a function that calls two spells
- `power_amplifier`: returns a modified version of a spell
- `conditional_caster`: returns a spell that only fires if a condition is met
- `spell_sequence`: returns a function that chains multiple spells

**Key insight:** Functions are data. You can combine them, wrap them, and compose them
just like you combine strings or numbers. This is the foundation of functional composition.

### ex2 — `scope_mysteries.py`
**Concept:** Closures, lexical scoping, `nonlocal`.
Functions "remember" variables from where they were defined — not where they're called.
This creates closures: functions with persistent private state.
- `mage_counter`: closure that counts its own calls
- `spell_accumulator`: closure with running total
- `enchantment_factory`: factory function creating parameterized closures
- `memory_vault`: closure-based private storage (like a simple object)

**Key insight:** Closures are an alternative to classes for maintaining state. They're
lightweight and naturally encapsulated — the captured variables are truly private.

### ex3 — `functools_artifacts.py`
**Concept:** `functools` module — `reduce`, `partial`, `lru_cache`.
- `reduce`: collapses a list into a single value by repeatedly applying a function
- `partial`: pre-fills some arguments of a function, creating a specialized version
- `lru_cache`: memoization decorator that caches function results for repeated inputs

**Key insight:** `partial` is like creating a template from a general function.
`lru_cache` trades memory for speed on pure functions. `reduce` is powerful but
often less readable than a loop — use judiciously.

### ex4 — `masters_tower.py`
**Concept:** Decorators, `@wraps`, `@classmethod`, `@staticmethod`.
Decorators wrap functions to add behavior (timing, access control, repetition) without
modifying the original function's code.
- `timing_decorator`: measures execution time
- `repeat(n)`: decorator factory that calls a function n times
- `authenticated(role)`: access control decorator
- `SpellBook`: class with `@classmethod` and `@staticmethod`

**Key insight:** Decorators are syntactic sugar for higher-order functions.
`@decorator` is equivalent to `func = decorator(func)`. `@wraps` preserves the
original function's metadata (name, docstring).

## Key Takeaways

- **Functions are first-class:** pass them, return them, store them in variables.
- **Lambdas:** anonymous one-expression functions for simple operations.
- **Higher-order functions:** enable composition, wrapping, and conditional execution.
- **Closures:** functions with memory — lightweight alternative to classes for state.
- **`functools`:** battle-tested utilities for partial application, memoization, and reduction.
- **Decorators:** the Pythonic way to add cross-cutting concerns (logging, auth, timing).
- Functional patterns complement OOP — use both where they fit best.
