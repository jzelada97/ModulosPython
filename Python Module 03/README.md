# Module 03 — Data Quest: Mastering Python Collections

## Overview

This module explores Python's core data structures through gaming scenarios. Each
exercise introduces a different collection type and demonstrates when and why to use it.
Understanding collection choice is fundamental to writing efficient, idiomatic Python.

## Exercises & Learning Objectives

### ex0 — `ft_command_quest.py`
**Concept:** Lists, `sys.argv`, command-line arguments.
Introduction to lists through Python's built-in argument list. Demonstrates indexing,
`len()`, and iteration over list elements.

### ex1 — `ft_score_analytics.py`
**Concept:** List operations, type conversion, basic statistics.
Processing command-line strings into numeric lists. Uses `sum()`, `max()`, `min()` and
demonstrates error handling for invalid inputs mixed with valid data.

### ex2 — `ft_coordinate_system.py`
**Concept:** Tuples, immutability, unpacking.
Tuples store fixed-structure data (x, y, z coordinates). Once created, they cannot be
modified — making them ideal for data that shouldn't change. Introduces the Euclidean
distance formula in 3D.

### ex3 — `ft_achievement_tracker.py`
**Concept:** Sets, set operations (union, intersection, difference).
Sets store unique elements and support mathematical operations. Demonstrates finding
common elements, exclusive elements, and missing elements across collections — operations
that would be complex with lists but are one-liners with sets.

### ex4 — `ft_inventory_system.py`
**Concept:** Dictionaries, key-value pairs, parsing structured input.
Dictionaries map keys to values — perfect for inventories, configs, and lookups.
Demonstrates parsing `key:value` format, `dict.keys()`, `dict.values()`, and
`dict.update()`.

### ex5 — `ft_data_stream.py`
**Concept:** Generators, `yield`, lazy evaluation.
Generators produce values on-demand without storing everything in memory. Essential
for processing large data streams. Introduces `yield` keyword and generator functions.

### ex6 — `ft_data_alchemist.py`
**Concept:** List/dict/set comprehensions, concise data transformation.
Comprehensions provide compact syntax for creating collections from existing data.
Demonstrates filtering, mapping, and transforming data in a single expression.

## Key Takeaways

- **Lists**: ordered, mutable, indexed — use for sequences you'll modify.
- **Tuples**: ordered, immutable — use for fixed-structure data (coordinates, records).
- **Sets**: unordered, unique elements — use for membership testing and math operations.
- **Dicts**: key-value mapping — use for lookups, configs, structured data.
- **Generators**: lazy sequences — use for large/infinite data streams.
- **Comprehensions**: concise syntax for transforming collections in one line.
- Choosing the right data structure is often more impactful than optimizing algorithms.
