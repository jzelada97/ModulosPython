# Module 07 — DataDeck: Abstract Card Architecture

## Overview

This module teaches advanced design patterns through a creature-based card game. You
apply abstract factories, capability mixins, and strategy patterns — the same patterns
used in game engines, plugin systems, and enterprise architectures.

## Exercises & Learning Objectives

### ex0 — Creature Factory (`creature.py`, `factory.py`)
**Concept:** Abstract Factory pattern.
An abstract `CreatureFactory` defines the contract for creating creature families. Concrete
factories (`FlameFactory`, `AquaFactory`) produce related objects (base + evolved) without
the client knowing which specific classes are instantiated.

**Why it matters:** When you need to create families of related objects that must work
together, abstract factories ensure consistency. Adding a new creature family means
creating one new factory — no changes to existing code.

**Test script:** `battle.py` — creates creatures from factories and demonstrates combat.

### ex1 — Capabilities (`capabilities.py`, `factory.py`)
**Concept:** Multiple inheritance (mixins), capability-based design.
`HealCapability` and `TransformCapability` are abstract classes independent of `Creature`.
Concrete creatures inherit from BOTH `Creature` AND a capability, gaining extra behavior
without modifying the base class hierarchy.

**Why it matters:** Capabilities (mixins) add behavior orthogonally to the main hierarchy.
A creature can be both a Creature and a Healer without creating a complex diamond
inheritance tree. This is composition over inheritance.

**Test script:** `capacitor.py` — demonstrates healing and transforming creatures.

### ex2 — Abstract Strategy (`strategy.py`)
**Concept:** Strategy pattern, runtime behavior selection.
`BattleStrategy` defines how a creature acts in combat. `NormalStrategy`, `AggressiveStrategy`,
and `DefensiveStrategy` implement different behaviors. The tournament script assigns
strategies to creatures dynamically — the same creature can fight differently based on
its assigned strategy.

**Why it matters:** Strategy decouples "what to do" from "who does it." You can add new
battle behaviors without touching creature classes. Invalid strategy-creature combinations
are caught via `is_valid()` checks.

**Test script:** `tournament.py` — runs multi-creature battles with mixed strategies.

## Key Takeaways

- **Abstract Factory** creates families of related objects through a single interface.
- **Mixins/Capabilities** add behavior without deep inheritance hierarchies.
- **Strategy pattern** makes behavior interchangeable at runtime.
- `is_valid()` + exceptions handle invalid combinations gracefully.
- These patterns enable systems that grow without breaking existing code (Open/Closed Principle).
- Packages expose only factories (`__init__.py`), hiding implementation details.
