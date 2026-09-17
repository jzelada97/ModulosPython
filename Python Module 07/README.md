# Module 07 — DataDeck: Abstract Card Architecture

## Overview

This module teaches advanced design patterns through a creature-based card game. You
apply abstract factories, capability mixins, and strategy patterns — the same patterns
used in game engines, plugin systems, and enterprise architectures. The exercise
descriptions below are paired with the exact checklist items from 42's official
peer-evaluation scale for this project, so this README also works as a "did I meet the
bar" reference before a defense.

## Repository Structure

```
battle.py             (ex0 test script — instantiates both factories, runs the battle scenario)
capacitor.py           (ex1 test script — exercises heal/transform capabilities)
tournament.py          (ex2 test script — multi-creature tournament with strategies)
ex0/
  __init__.py          (exposes only FlameFactory, AquaFactory)
  creature.py          (Creature ABC + 4 concrete creatures)
  factory.py           (CreatureFactory ABC + 2 concrete factories)
ex1/
  __init__.py          (exposes only HealingCreatureFactory, TransformCreatureFactory)
  capabilities.py      (HealCapability / TransformCapability ABCs + 4 concrete creatures)
  factory.py           (2 concrete factories, one per capability family)
ex2/
  __init__.py          (exposes BattleStrategy and the 3 concrete strategies)
  strategy.py          (BattleStrategy ABC + NormalStrategy/AggressiveStrategy/DefensiveStrategy)
```

## Preliminary Checks

Before grading individual exercises, the evaluation scale asks the corrector to confirm:

- The Git repository being graded actually belongs to the student and no aliases were
  used to substitute another codebase.
- The project structure matches the subject: `ex0/`, `ex1/`, and `ex2/` all exist and
  each contains an `__init__.py`.
- No unexpected, uncontrolled crash happens while the defense scripts (`battle.py`,
  `capacitor.py`, `tournament.py`) run — an unhandled traceback during the live defense
  is graded as a failed defense regardless of how correct the design pattern is.

**Verified status:** all three scripts (`battle.py`, `capacitor.py`, `tournament.py`)
run end-to-end without crashing, and the module is flake8-clean and mypy-clean
(`--disallow-untyped-defs --disallow-incomplete-defs`). `ex1/factory.py` previously
imported its sibling module as a bare top-level `from capabilities import ...`, which
raised `ModuleNotFoundError` as soon as `ex1` (and therefore `capacitor.py` and
`tournament.py`) was imported; it now uses the same absolute package-import
convention as `ex0/factory.py` (`from ex1.capabilities import ...`).

**Independent subject audit (second pass, against `en.subject (1).txt` directly):**
a few gaps slipped through the eval-sheet-only pass and were fixed:
- `ex2/strategy.py` raised the builtin `TypeError` on an invalid strategy/creature
  pairing. The subject requires "a dedicated exception... with a clear message" —
  added a proper `InvalidStrategyError(Exception)` class, raised by
  `AggressiveStrategy.act()` and `DefensiveStrategy.act()`, exported from
  `ex2/__init__.py`.
- The subject says the ex0 test function "receives a factory object" and the ex2
  tournament takes tuples of "a `CreatureFactory` and a `BattleStrategy`" — both read
  as instances, but `battle.py`'s `test_factory`/`run_battle` and `tournament.py`'s
  opponent tuples were passing factory/strategy **classes** and instantiating them
  internally. Both now take already-constructed objects.
- `battle.py`, `capacitor.py`, and `tournament.py` each had a top-level `print(...)`
  before their imports, which is an actual flake8 `E402` violation (`import` not at
  top of file) — contradicting the "flake8-clean" claim above. Fixed by moving the
  print into the `__main__` block (or after the imports for `capacitor.py`), with no
  change to the printed output.
- `ex0/factory.py`, `ex1/capabilities.py`, and `ex1/factory.py` each had a dead
  `sys.path.insert(...)` hack (guarded by nothing, always executed) that also
  produced `E402` and was never needed — these modules are only ever loaded through
  the package mechanism from the root-level test scripts. Removed.
- Re-ran plain `flake8` (79-column default, no config, no ignores) across the whole
  module: now 0 errors, where it previously reported 11 `E402` violations across 5 files.
  `mypy --strict` still passes. All three scripts re-verified to still print output
  matching the subject's example transcripts exactly.
- `capacitor.py` had **six `# type: ignore[attr-defined]` comments** suppressing real
  mypy errors on `base.heal()`, `base2.transform()`, etc. The root cause: `ex1/factory.py`'s
  `HealingCreatureFactory.create_base()`/`create_evolved()` and
  `TransformCreatureFactory.create_base()`/`create_evolved()` declared their return type as
  the generic `Creature` (matching `CreatureFactory`'s abstract signature), even though each
  one only ever returns one specific capability-bearing subclass (`Sproutling`, `Bloomelle`,
  `Shiftling`, `Morphagon`). Fixed by narrowing each override's return type to the concrete
  subclass it actually returns (a valid covariant override, not a type-safety hole) instead
  of suppressing the error — `mypy --strict` now type-checks `base.heal()` for real, with
  zero `# type: ignore` comments anywhere in the module.

## Exercises & Learning Objectives

### ex0 — Creature Factory (`creature.py`, `factory.py`)
**What this exercise wants you to teach you:** how to create families of related objects
through a single interface, so the calling code never needs to know which concrete
family it's working with — the Abstract Factory pattern.

**Concept:** Abstract Factory pattern.
An abstract `CreatureFactory` defines the contract for creating creature families. Concrete
factories (`FlameFactory`, `AquaFactory`) produce related objects (base + evolved) without
the client knowing which specific classes are instantiated.

**Why it matters:** When you need to create families of related objects that must work
together, abstract factories ensure consistency. Adding a new creature family means
creating one new factory — no changes to existing code.

**Test script:** `battle.py` — creates creatures from factories and demonstrates combat.

**Evaluation checklist (official grading scale):**
- `ex0/` contains an `__init__.py` and at least one other file (multiple files allowed).
- `Creature` is an abstract class inheriting from `ABC`; `attack()` is an abstract
  method, `describe()` is a concrete method.
- At least four different concrete `Creature` subclasses exist.
- `CreatureFactory` is an abstract class inheriting from `ABC`, declaring `create_base()`
  and `create_evolved()` as abstract methods.
- At least two concrete factory classes exist, one per creature family, each capable of
  producing two creatures (a base and an evolved form).
- `ex0/__init__.py` exposes only the creature **factories**, never the creature classes
  themselves.
- `battle.py` instantiates both concrete factory classes.
- `battle.py` defines a single function that accepts *any* factory and: creates the base
  creature, calls `describe()` and `attack()` on it, then repeats the same steps for the
  evolved creature — and this one function must work unchanged with both factories.
- `battle.py` defines a **second, separate function** that receives two factories,
  creates two creatures from them (base or evolved), describes both, and makes them
  fight. This is `run_battle(factory1, factory2)`, fully separated from
  `test_factory()` and from the `if __name__ == '__main__':` block.
- Naming is flexible: the evaluator accepts different class/method names as long as the
  Abstract Factory pattern itself is correctly implemented (this note applies to every
  exercise in this module).

### ex1 — Capabilities (`capabilities.py`, `factory.py`)
**What this exercise wants you to teach you:** composition over inheritance via mixins —
how to add orthogonal behavior to a class hierarchy without deepening or tangling it.

**Concept:** Multiple inheritance (mixins), capability-based design.
`HealCapability` and `TransformCapability` are abstract classes independent of `Creature`.
Concrete creatures inherit from BOTH `Creature` AND a capability, gaining extra behavior
without modifying the base class hierarchy.

**Why it matters:** Capabilities (mixins) add behavior orthogonally to the main hierarchy.
A creature can be both a Creature and a Healer without creating a complex diamond
inheritance tree. This is composition over inheritance.

**Test script:** `capacitor.py` — demonstrates healing and transforming creatures.

**Evaluation checklist (official grading scale):**
- `ex1/` contains an `__init__.py` and at least one other file (multiple files allowed).
- `HealCapability` and `TransformCapability` are abstract classes inheriting from `ABC`.
  `HealCapability` declares the abstract `heal()` method; `TransformCapability` declares
  the abstract `transform()` and `revert()` methods (other capability names/methods are
  acceptable as long as the pattern holds).
- At least four *new* concrete `Creature` subclasses exist, each inheriting from both
  `Creature` and one of the two capability classes — two creatures with the heal
  capability, two with the transform capability.
- At least two concrete factory classes exist, one per new family, each producing two
  creatures (base + evolved).
- `ex1/__init__.py` exposes only the creature **factories**, never the creature classes
  themselves.
- `capacitor.py` instantiates both new factory classes.
- `capacitor.py` exercises each factory's base and evolved creature using the standard
  `describe()`/`attack()` methods, plus the capability method inserted at the
  scenario-appropriate point (e.g. `heal()` after `attack()`, or `transform()` before
  `attack()` and `revert()` after).

### ex2 — Abstract Strategy (`strategy.py`)
**What this exercise wants you to teach you:** how to make behavior swappable at runtime
instead of hardcoding it into the object — the Strategy pattern, decoupling "what to do"
from "who does it."

**Concept:** Strategy pattern, runtime behavior selection.
`BattleStrategy` defines how a creature acts in combat. `NormalStrategy`, `AggressiveStrategy`,
and `DefensiveStrategy` implement different behaviors. The tournament script assigns
strategies to creatures dynamically — the same creature can fight differently based on
its assigned strategy.

**Why it matters:** Strategy decouples "what to do" from "who does it." You can add new
battle behaviors without touching creature classes. Invalid strategy-creature combinations
are caught via `is_valid()` checks.

**Test script:** `tournament.py` — runs multi-creature battles with mixed strategies.

**Evaluation checklist (official grading scale):**
- `ex2/` contains an `__init__.py` and at least one other file (multiple files allowed).
- `BattleStrategy` is an abstract class inheriting from `ABC`, declaring `act()` and
  `is_valid()` as abstract methods.
- At least three different concrete strategy classes inherit from `BattleStrategy`.
- A "normal" strategy exists that is valid for any creature, regardless of family or
  capability.
- Other strategies exist that match the capabilities introduced in ex1 — e.g. a
  defensive strategy that is only valid for a creature with the heal capability, and
  calls `heal()` after `attack()`.
- `tournament.py` instantiates creature factory classes from both ex0 and ex1.
- `tournament.py` instantiates the available strategies.
- A single `battle()` function exists and drives the whole tournament (helper functions
  are allowed).
- `battle()` accepts, as a parameter, a list of `(CreatureFactory, BattleStrategy)`
  tuples.
- `battle()` pairs up every opponent from that list exactly once: a creature never
  fights itself, and no pair fights twice (A vs B and B vs A must not both happen).
- The strategy assigned to each creature is actually applied during its fight (e.g. a
  healer creature calls `heal()` under a defensive strategy but not under a normal one).
- Pairing a creature with a strategy it is not compatible with (`is_valid()` returns
  `False`) must stop the tournament rather than silently continuing or crashing
  uncontrolled.

## Code Quality and Understanding

These requirements are graded once for the whole module (not per exercise), per the
official "Code Quality and Understanding" section of the scale:

- The code must run on **Python 3.10 or newer**.
- The code must be **flake8-clean** — no linter errors.
- **Type hints are required on every function and method** (this is checked with
  `mypy`). Unlike other modules, **docstrings are explicitly NOT required** for Module 07.
- The code must be well-structured and readable.

## Defense Prep — Questions From the Evaluation Sheet

This module's eval sheet is phrased as live checks the evaluator performs rather than
direct questions, so each item below restates a live check alongside what you should be
ready to show or explain for it.

### Exercise 0

- **Live check:** reads `ex0/`'s `Creature`/`CreatureFactory` classes and checks that
  `attack()`, `create_base()`, and `create_evolved()` are actually abstract methods.
  **Be ready to:** show that `Creature` and `CreatureFactory` truly inherit from `ABC`
  and that those three methods are declared abstract, not just named suggestively.
- **Live check:** runs `python3 battle.py` and confirms `test_factory()` works unchanged
  on both `FlameFactory` and `AquaFactory`.
  **Be ready to:** demonstrate that the same `test_factory()` function runs against both
  factories without modification.
- **Live check:** confirms `run_battle()` is a real second function (not code
  copy-pasted or inlined under `__main__`).
  **Be ready to:** point to `run_battle(factory1, factory2)` as a distinct function,
  fully separated from `test_factory()` and from the `if __name__ == '__main__':` block.

### Exercise 1

- **Live check:** confirms `HealCapability`/`TransformCapability` don't inherit from
  `Creature` (composition, not a deeper hierarchy).
  **Be ready to:** explain that the capability classes are independent of `Creature`,
  and that concrete creatures gain capability behavior via mixin (multiple inheritance)
  rather than by deepening the `Creature` hierarchy.
- **Live check:** confirms `capacitor.py` instantiates both new factories.
  **Be ready to:** show both new ex1 factory classes being instantiated in
  `capacitor.py`.
- **Live check:** confirms each capability method fires at the right point in the
  sequence (base → evolved, for both the healing and transforming families) when the
  script runs.
  **Be ready to:** walk through `capacitor.py`'s execution order and show
  `heal()`/`transform()`/`revert()` firing at the scenario-appropriate point for both
  base and evolved creatures in each family.

### Exercise 2

- **Live check:** runs `tournament.py` and checks the round-robin pairing — for n
  opponents, each pair must fight exactly once, no self-fights, and no A-B/B-A
  duplicate.
  **Be ready to:** explain how `battle()`'s pairing logic guarantees each opponent pair
  fights exactly once.
- **Live check:** confirms a healer creature calls `heal()` only under a defensive
  strategy, not under a normal one.
  **Be ready to:** show that the strategy assigned to a creature actually changes its
  behavior at runtime (e.g. `heal()` fires under `DefensiveStrategy` but not
  `NormalStrategy`).
- **Live check:** may construct an intentionally invalid strategy/creature pairing to
  verify the tournament stops cleanly instead of crashing.
  **Be ready to:** demonstrate that an invalid pairing (`is_valid()` returns `False`)
  raises the dedicated `InvalidStrategyError` with a clear message, instead of crashing
  uncontrolled or silently continuing (see "Independent subject audit" above).

### Code Quality and Understanding

- **Live check:** during the defense, the evaluator probes your real understanding of
  the abstract patterns used, not just whether the code runs.
  **Be ready to explain:**
  - why `CreatureFactory`/`HealCapability`/`BattleStrategy` need to be `ABC`s;
  - why capabilities are added via mixins instead of subclassing `Creature` directly;
  - how `is_valid()` prevents illegal strategy/creature pairings;
  - why the `__init__.py` files only export factories instead of the creature classes.

## Key Takeaways

- **Abstract Factory** creates families of related objects through a single interface.
- **Mixins/Capabilities** add behavior without deep inheritance hierarchies.
- **Strategy pattern** makes behavior interchangeable at runtime.
- `is_valid()` + exceptions handle invalid combinations gracefully — and, per the eval
  scale, an invalid pairing must stop the tournament instead of crashing it outright.
- These patterns enable systems that grow without breaking existing code (Open/Closed Principle).
- Packages expose only factories (`__init__.py`), hiding implementation details.
- Type hints are mandatory in this module (checked with `mypy`); docstrings are not.
