# Module 01 — Code Cultivation: Object-Oriented Garden Systems

## Overview

This module introduces Object-Oriented Programming (OOP) progressively. Starting from
basic program structure, it builds up to inheritance hierarchies, encapsulation, and
method tracking — all modeled around a digital garden ecosystem.

## Exercises & Learning Objectives

### ex0 — `ft_garden_intro.py`
**Concept:** Program entry point, `if __name__ == "__main__":` pattern.
Explains how Python scripts execute and why the `__main__` guard matters for imports
and modularity.

### ex1 — `ft_garden_data.py`
**Concept:** Classes as data models, `__init__`, instance attributes, methods.
First class definition — a `Plant` class that groups related data (name, height, age)
and provides a `show()` method for display.

### ex2 — `ft_plant_growth.py`
**Concept:** Methods that modify state (`grow()`, `age()`), simulating behavior over time.
Objects aren't just data containers — they have behavior that changes their state.

### ex3 — `ft_plant_factory.py`
**Concept:** Constructor parameters, creating objects with initial state.
The `__init__` method accepts arguments so objects are ready to use immediately after
creation (no separate "set" step needed).

### ex4 — `ft_garden_security.py`
**Concept:** Encapsulation, getters/setters, data validation.
Introduces protected attributes (`_name` convention), controlled access through methods,
and validation logic that rejects invalid data to maintain integrity.

### ex5 — `ft_plant_types.py`
**Concept:** Inheritance, `super()`, method overriding.
Specialized classes (`Flower`, `Tree`, `Vegetable`) inherit common behavior from `Plant`
while adding their own attributes and overriding methods like `show()`.

### ex6 — `ft_garden_analytics.py`
**Concept:** Decorators/tracking, `@staticmethod`, `@classmethod`, combining concepts.
Demonstrates counting method calls, static utility methods, and class-level behavior.
Combines all OOP concepts from previous exercises into a cohesive system.

## Key Takeaways

- Classes model real-world entities with data (attributes) and behavior (methods).
- `__init__` initializes objects; `self` refers to the current instance.
- Encapsulation protects internal state from invalid modifications.
- Inheritance enables code reuse; `super()` delegates to parent implementations.
- Method overriding lets subclasses specialize behavior while sharing structure.
