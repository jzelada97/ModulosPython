# Module 10 — FuncMage: Functional Programming

## Overview

This module explores functional programming paradigms in Python. Functions become
first-class citizens — passed as arguments, returned from other functions, and stored
in variables. These patterns produce elegant, composable, and reusable code.

The official subject ("FuncMage — Master the Ancient Arts of Functional Programming",
v3.2) frames the five exercises as five realms: lambdas, higher-order functions,
closures/lexical scoping, `functools`, and decorators. Each realm has its own file,
required function/class signatures, an expected-output example, and one or more
conceptual questions the evaluator asks during the peer-review defence.

**Global requirements that apply to every exercise** (from the subject's Common
Instructions and the official evaluation scale):

- Python **3.10 or later**.
- Code must pass **flake8** with no errors.
- **Type hints are required** for every function/method — parameters and return
  values. (Docstrings are explicitly **not** required for this module.)
- When `Callable` is used as a type hint, import it from `collections.abc`, not
  `typing`.
- No **global variables** and no **file I/O** — everything is in-memory.
- No `eval()` / `exec()`, no external/third-party libraries (no `pip install`).
- Each exercise lives in its own file, submitted under the exact name the subject
  specifies:
  - `ex0/lambda_spells.py`
  - `ex1/higher_magic.py`
  - `ex2/scope_mysteries.py`
  - `ex3/functools_artifacts.py`
  - `ex4/decorator_mastery.py`
  - If any of these five files is missing (or misnamed), the peer-review scale says
    grading stops immediately.
- `generator.tar.gz` (attached to the subject) contains `data_generator.py`, a helper
  script for producing sample mages/artifacts/spells to exercise each function during
  self-testing and defence.

## Exercises & Learning Objectives

### ex0 — `lambda_spells.py`

**What this exercise wants you to teach you:** when a throwaway anonymous function
(a lambda) is clearer than a named `def`, and when it isn't.

**Concept:** Lambda expressions, `map()`, `filter()`, `sorted()` with key functions.
Anonymous functions (lambdas) are one-line expressions used for simple transformations.
Combined with `map()`, `filter()`, and `sorted()`, they enable data transformation
without defining named functions for trivial operations.

**Key insight:** Lambdas shine for short, throwaway operations. If the logic needs
a name or exceeds one expression, use `def`.

**Evaluation Checklist** (official grading scale + subject):
- Required signatures:
  `artifact_sorter(artifacts: list[dict]) -> list[dict]`,
  `power_filter(mages: list[dict], min_power: int) -> list[dict]`,
  `spell_transformer(spells: list[str]) -> list[str]`,
  `mage_stats(mages: list[dict]) -> dict`.
- `artifact_sorter()` uses `sorted()` with a lambda keyed on `'power'`, descending.
- `power_filter()` uses `filter()` with a lambda testing `power >= min_power`.
- `spell_transformer()` uses `map()` with a lambda that adds a `"* "` prefix and
  `" *"` suffix to each spell name.
- `mage_stats()` uses lambdas together with `max()` / `min()` to compute the most
  and least powerful mage's power, plus the average power rounded to 2 decimals;
  returns `{'max_power': int, 'min_power': int, 'avg_power': float}`.
- No `def` is used for simple one-off transformations — lambdas only.
- Authorized built-ins for this exercise: `map`, `filter`, `sorted`, `min`, `max`,
  `round`, `sum`, `len`.

### ex1 — `higher_magic.py`

**What this exercise wants you to teach you:** that functions are first-class
values in Python — they can be passed around, composed, wrapped, and combined just
like any other data.

**Concept:** Higher-order functions — functions that accept/return functions.
- `spell_combiner`: returns a function that calls two spells
- `power_amplifier`: returns a modified version of a spell
- `conditional_caster`: returns a spell that only fires if a condition is met
- `spell_sequence`: returns a function that chains multiple spells

**Key insight:** Functions are data. You can combine them, wrap them, and compose them
just like you combine strings or numbers. This is the foundation of functional composition.

**Evaluation Checklist:**
- Required signatures (every spell follows the contract
  `spell(target: str, power: int) -> str`):
  `spell_combiner(spell1: Callable, spell2: Callable) -> Callable`,
  `power_amplifier(base_spell: Callable, multiplier: int) -> Callable`,
  `conditional_caster(condition: Callable, spell: Callable) -> Callable`,
  `spell_sequence(spells: list[Callable]) -> Callable`.
- `spell_combiner()` returns a function that calls **both** input spells with the
  same arguments and returns a tuple of both results.
- `power_amplifier()` returns a function with the same signature as the original
  spell, where the `power` argument is multiplied by `multiplier` **before** the
  base spell is cast.
- `conditional_caster()` returns a function that checks the condition first; if it
  is falsy, it returns `"Spell fizzled"` instead of casting.
- `spell_sequence()` returns a function that casts every spell in order and returns
  a list of all results.
- Functions must be demonstrably treated as first-class citizens: passed as
  arguments, returned from functions, stored/used like any other value.
- Authorized: `callable()`, `Callable` (from `collections.abc`).

### ex2 — `scope_mysteries.py`

**What this exercise wants you to teach you:** closures and lexical scoping as a
lightweight alternative to global mutable state for keeping private, persistent data.

**Concept:** Closures, lexical scoping, `nonlocal`.
Functions "remember" variables from where they were defined — not where they're called.
This creates closures: functions with persistent private state.
- `mage_counter`: closure that counts its own calls
- `spell_accumulator`: closure with running total
- `enchantment_factory`: factory function creating parameterized closures
- `memory_vault`: closure-based private storage (like a simple object)

**Key insight:** Closures are an alternative to classes for maintaining state. They're
lightweight and naturally encapsulated — the captured variables are truly private.

**Evaluation Checklist:**
- Required signatures:
  `mage_counter() -> Callable`, `spell_accumulator(initial_power: int) -> Callable`,
  `enchantment_factory(enchantment_type: str) -> Callable`,
  `memory_vault() -> dict[str, Callable]`.
- `mage_counter()` returns a function whose calls persist and increment a private
  count starting at 1; two separate counters must keep **independent** state.
- `spell_accumulator()` returns a function that adds the given amount to a running
  total (starting at `initial_power`) and returns the new total each call.
- `enchantment_factory()` returns a function formatted as
  `"{enchantment_type} {item_name}"`; independent factories must not interfere
  with each other (e.g. `"Flaming"` vs `"Frozen"` applied to the same item name).
- `memory_vault()` returns a dict with `'store'` (takes `key, value`) and `'recall'`
  (takes `key`, returns the stored value or `"Memory not found"`) functions sharing
  one private closure-scoped storage.
- No `global` keyword anywhere, and **no class definitions** in this file — state
  must be captured purely through closures/`nonlocal`.
- Authorized: `nonlocal`.

### ex3 — `functools_artifacts.py`

**What this exercise wants you to teach you:** the standard `functools` toolbox —
`reduce`, `partial`, `lru_cache`, `singledispatch` — instead of reinventing these
patterns by hand.

**Concept:** `functools` module — `reduce`, `partial`, `lru_cache`, `singledispatch`.
- `reduce`: collapses a list into a single value by repeatedly applying a function
- `partial`: pre-fills some arguments of a function, creating a specialized version
- `lru_cache`: memoization decorator that caches function results for repeated inputs
- `singledispatch`: dispatches to different implementations based on argument type

**Key insight:** `partial` is like creating a template from a general function.
`lru_cache` trades memory for speed on pure functions. `reduce` is powerful but
often less readable than a loop — use judiciously.

**Evaluation Checklist:**
- Required signatures:
  `spell_reducer(spells: list[int], operation: str) -> int`,
  `partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]`,
  `memoized_fibonacci(n: int) -> int`,
  `spell_dispatcher() -> Callable[[Any], str]`.
- **Spell Reducer:** uses `functools.reduce` together with `operator` module
  functions (`operator.add`, `operator.mul`, etc.); must support the operation
  strings `"add"`, `"multiply"`, `"max"`, `"min"`; returns `0` for an empty list;
  handles an unknown operation string gracefully.
- **Partial Enchanter:** uses `functools.partial` (not a lambda wrapping a call) to
  build **3** specialized versions of a `(power, element, target) -> str` function,
  each pre-filling `power=50` and one `element`. The grading scale specifically
  checks `type(result['fire_enchant']) is functools.partial`, so the returned dict
  keys matter, not just the values.
- **Memoized Fibonacci:** uses `functools.lru_cache` for memoization; the returned
  Fibonacci numbers must be correct, repeated calls must be measurably faster, and
  `memoized_fibonacci.cache_info()` must return a `CacheInfo` with `hits > 0` after
  calling e.g. `memoized_fibonacci(10)` then `memoized_fibonacci(5)` — i.e. the
  cache must be attached to `memoized_fibonacci` itself and persist across calls,
  not be re-created per call.
- **Spell Dispatcher:** uses `functools.singledispatch` (not a manual
  `dict`/`if`/`isinstance` dispatch table) to branch on argument type; must handle
  at least `int` (damage spell), `str` (enchantment), `list` (multi-cast), and
  degrade gracefully for an unregistered type such as `float`.
- Authorized: `functools`, `operator`.

### ex4 — `decorator_mastery.py`

**What this exercise wants you to teach you:** how decorators transparently
transform a function's behavior (timing, validation, retries) without touching its
code, and how `@staticmethod` differs from a regular instance method.

**Concept:** Decorators, `@wraps`, `@staticmethod`, parameterized decorators.
Decorators wrap functions to add behavior (timing, validation, retries) without
modifying the original function's code.

**Key insight:** Decorators are syntactic sugar for higher-order functions.
`@decorator` is equivalent to `func = decorator(func)`. `@wraps` preserves the
original function's metadata (name, docstring).

**Evaluation Checklist:**
- Required file name per the subject: **`decorator_mastery.py`** (submitted under
  `ex4/`).
- Required signatures:
  `spell_timer(func: Callable) -> Callable`,
  `power_validator(min_power: int) -> Callable`,
  `retry_spell(max_attempts: int) -> Callable`,
  and a `MageGuild` class with
  `@staticmethod validate_mage_name(name: str) -> bool` and instance method
  `cast_spell(self, spell_name: str, power: int) -> str`.
- `spell_timer()`: decorator that prints `"Casting <function_name>..."` before
  execution, runs the function, prints `"Spell completed in X.XXX seconds"`
  (3 decimal places) after, uses `functools.wraps`, and returns the wrapped
  function's original result.
- `power_validator(min_power)`: a **parameterized** decorator factory — if the
  decorated function's `power` argument is `>= min_power`, run it normally;
  otherwise return `"Insufficient power for this spell"`. Must use
  `functools.wraps`.
- `retry_spell(max_attempts)`: decorator factory that retries the wrapped function
  on exception, printing `"Spell failed, retrying... (attempt n/max_attempts)"` for
  each failed attempt; if every attempt fails, returns
  `"Spell casting failed after max_attempts attempts"`; returns the result normally
  as soon as one attempt succeeds.
- `MageGuild.validate_mage_name(name)`: `@staticmethod` that returns `True` only
  when `name` is at least 3 characters long and contains only letters/spaces.
- `MageGuild.cast_spell(self, spell_name, power)`: instance method that applies the
  `power_validator` decorator with `min_power=10`; returns
  `"Successfully cast <spell_name> with <power> power"` when valid, otherwise
  `"Insufficient power for this spell"`.
- `functools.wraps` must be used on every decorator so wrapped functions keep their
  original `__name__`/metadata.
- Authorized: `functools.wraps`, `staticmethod`.

## Preliminary / Whole-Module Checks

Before grading individual exercises, the official scale also verifies:

- All five required files are present under the exact paths listed above.
- Every exercise runs without crashing, on both valid and invalid inputs.
- Functional-programming idioms are actually used (lambdas, higher-order functions,
  decorators, `functools`) rather than reimplemented manually.
- Dependencies (if any) are managed via a virtual environment.
- No global variables and no file I/O anywhere in the module.

## Code Quality and Understanding

The evaluation scale's shared "Code Quality and Understanding" section — applied
across all five exercises — checks:

- **Conceptual understanding**, discussed live with the evaluator:
  - The difference between `lambda` and `def` functions.
  - What makes functions "first-class citizens."
  - How closures capture lexical scope.
  - The benefits of `functools` utilities.
  - How decorators transform functions.
- **Code quality:**
  - Python 3.10+ syntax.
  - Clean `flake8` run (no errors).
  - Type hints on **every** function/method, for **all** parameters and the return
    value (docstrings are explicitly not required for this module).
  - Clean, readable code.
  - Functional patterns used correctly (not reimplemented by hand where a
    standard-library tool exists).
  - Evidence of genuine understanding rather than copied code.

## Defense Prep — Questions From the Evaluation Sheet

The subject's peer-review defence asks conceptual questions for each realm. These
were previously mixed into the per-exercise checklists above; they're collected here
as flashcards — verbatim question, then the talking points already documented
elsewhere in this README.

### Exercise 0 — Lambdas

*"How do lambda expressions make code more concise?"*
- Lambdas are one-line expressions used for simple transformations (see Concept).
- Combined with `map()`, `filter()`, `sorted()`, they replace a full `def` block for
  trivial operations.

*"When should you use lambda vs. regular function definitions?"*
- Key insight: lambdas shine for short, throwaway operations. If the logic needs a
  name or exceeds one expression, use `def`.
- This exercise specifically requires lambdas-only for its simple one-off
  transformations (no `def`).

### Exercise 1 — Higher-Order Functions

*"How do higher-order functions enable code reuse and composition?"*
- Key insight: functions are data — you can combine them, wrap them, and compose
  them just like strings or numbers. This is the foundation of functional
  composition.
- Demonstrated by `spell_combiner` (calls two spells), `power_amplifier` (wraps a
  spell with modified behavior), `conditional_caster` (wraps a spell with a guard
  condition), and `spell_sequence` (chains multiple spells).

*"What makes functions 'first-class citizens' in Python?"*
- Functions can be passed as arguments, returned from other functions, and
  stored/used like any other value — exactly what all four required functions in
  this exercise must demonstrate.

*"From which package is it recommended to use `Callable`?"*
- `collections.abc`, not `typing` (per the module's global requirements).

*"What is the purpose of `callable()`?"*
- Listed as one of the authorized built-ins for this exercise, alongside `Callable`
  from `collections.abc`.

### Exercise 2 — Closures / Lexical Scoping

*"How do closures enable functions to 'remember' their creation environment?"*
- Concept: functions "remember" variables from where they were defined — not where
  they're called. This creates closures: functions with persistent private state.

*"What are the benefits of lexical scoping in functional programming?"*
- Key insight: closures are an alternative to classes for maintaining state.
  They're lightweight and naturally encapsulated — the captured variables are truly
  private.

*"Why is `global` forbidden but `nonlocal` allowed? What are the key differences?"*
- This exercise's checklist requires no `global` keyword anywhere and no class
  definitions — state must be captured purely through closures/`nonlocal`.
- `nonlocal` is the authorized mechanism for this exercise; it is what lets
  `mage_counter`, `spell_accumulator`, `enchantment_factory`, and `memory_vault`
  mutate their own enclosing-scope state while keeping it private, instead of
  relying on module-level (`global`) mutable state, which the module's global
  requirements forbid outright.

### Exercise 3 — `functools`

*"How are `\"min\"` and `\"max\"` implemented via `reduce`, since `operator` has no
direct min/max-reducer? Are there alternative approaches?"*
- The Spell Reducer checklist notes it uses `functools.reduce` together with
  `operator` module functions (`operator.add`, `operator.mul`, etc.) for `"add"`
  and `"multiply"`, while still needing to support `"max"` and `"min"` as
  operation strings.

*"How does `functools.reduce` enable powerful data aggregation?"*
- Concept: `reduce` collapses a list into a single value by repeatedly applying a
  function.
- Key insight: `reduce` is powerful but often less readable than a loop — use
  judiciously.

*"What are the performance benefits of memoization with `lru_cache`?"*
- Key insight: `lru_cache` trades memory for speed on pure functions.
- Demonstrated by Memoized Fibonacci: repeated calls must be measurably faster, and
  `cache_info()` must show `hits > 0` once a cached value is requested again.

*"What happens if you call `reduce` on an empty list without an initializer?"*
- Relevant to the Spell Reducer requirement that `spell_reducer` returns `0` for an
  empty list rather than letting `reduce` fail.

*"What is the difference between memoization and simply storing results in a global
dict?"*
- The module forbids global variables outright (global requirements section).
- The checklist requires the `lru_cache` to be attached to `memoized_fibonacci`
  itself and persist across calls (not be re-created per call), which is what
  `functools.lru_cache` gives for free versus hand-rolled caching.

### Exercise 4 — Decorators

*"How do decorators enable separation of concerns?"*
- Concept: decorators wrap functions to add behavior (timing, validation, retries)
  without modifying the original function's code.
- Key insight: decorators are syntactic sugar for higher-order functions;
  `@decorator` is equivalent to `func = decorator(func)`.
- Illustrated by `spell_timer` (timing), `power_validator` (validation), and
  `retry_spell` (retries) — three independent cross-cutting concerns layered onto
  spells without changing the spells themselves.

*"What's the difference between `@staticmethod` and regular instance methods?"*
- `MageGuild.validate_mage_name` is a `@staticmethod` — it doesn't take `self` and
  only checks a `name` string.
- `MageGuild.cast_spell(self, spell_name, power)` is a regular instance method that
  additionally applies the `power_validator` decorator with `min_power=10`.

## Key Takeaways

- **Functions are first-class:** pass them, return them, store them in variables.
- **Lambdas:** anonymous one-expression functions for simple operations.
- **Higher-order functions:** enable composition, wrapping, and conditional execution.
- **Closures:** functions with memory — lightweight alternative to classes for state.
- **`functools`:** battle-tested utilities for partial application, memoization,
  type-based dispatch, and reduction — the evaluator specifically checks that these
  are used instead of hand-rolled equivalents.
- **Decorators:** the Pythonic way to add cross-cutting concerns (logging, retries,
  validation, timing), always paired with `functools.wraps`.
- Functional patterns complement OOP — use both where they fit best.
