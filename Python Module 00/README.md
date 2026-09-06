# Module 00 — Growing Code: Python Fundamentals

## Overview

This module introduces Python's core building blocks through community garden scenarios.
Each exercise focuses on a single fundamental concept, progressing from basic output to
type-annotated functions.

## Exercises & Learning Objectives

### ex0 — `ft_hello_garden.py`
**Concept:** Defining and calling a function, using `print()`.
The simplest possible function — demonstrates function syntax (`def`) and that functions
encapsulate behavior.

### ex1 — `ft_garden_name.py`
**Concept:** User input with `input()`, string interpolation.
Shows how a program can receive data from the user at runtime and display it back.

### ex2 — `ft_plot_area.py`
**Concept:** Type conversion (`int()`), arithmetic operations.
Demonstrates converting string input to integers and performing calculations.

### ex3 — `ft_harvest_total.py`
**Concept:** Multiple inputs, accumulation.
Reinforces `input()` + `int()` and introduces the idea of summing multiple values.

### ex4 — `ft_plant_age.py`
**Concept:** Conditional logic (`if`/`else`), comparison operators.
First introduction to branching — the program behaves differently based on input.

### ex5 — `ft_water_reminder.py`
**Concept:** Conditionals with thresholds.
Reinforces `if`/`else` with a different real-world scenario.

### ex6 — `ft_count_harvest_iterative.py` / `ft_count_harvest_recursive.py`
**Concept:** Loops (`for` + `range()`), recursion.
Two implementations of the same problem — introduces iteration vs recursion tradeoff.

### ex7 — `ft_seed_inventory.py`
**Concept:** Type annotations, string methods (`.capitalize()`), multi-branch `if`/`elif`/`else`.
First exercise requiring explicit type hints (`str`, `int`, `-> None`). Demonstrates
how Python type annotations improve code clarity and enable static analysis with `mypy`.

## Key Takeaways

- Functions are Python's basic unit of reusable code.
- `input()` always returns a string; explicit conversion is needed for numbers.
- Conditionals control program flow based on data.
- Loops and recursion are two strategies for repetition.
- Type annotations document expected types and enable tooling support.
