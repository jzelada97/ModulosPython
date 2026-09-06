# Module 02 — Garden Guardian: Exception Handling

## Overview

This module teaches resilient programming through Python's exception handling system.
Instead of letting programs crash on bad data, you learn to anticipate failures and
handle them gracefully — essential for any data pipeline or production system.

## Exercises & Learning Objectives

### ex0 — `ft_first_exception.py`
**Concept:** `try`/`except` basics, catching runtime errors.
Demonstrates that exceptions don't have to crash a program. A `try` block attempts
risky operations; `except` catches and handles the error so execution continues.

### ex1 — `ft_raise_exception.py`
**Concept:** Raising exceptions intentionally with `raise`, custom validation.
Beyond catching errors from built-in operations, you can create your own validation
logic and `raise` exceptions when business rules are violated (e.g., temperature out
of range for plants).

### ex2 — `ft_different_errors.py`
**Concept:** Multiple exception types, targeted `except` clauses.
Python has a hierarchy of exception types (`ValueError`, `ZeroDivisionError`,
`FileNotFoundError`, `TypeError`). Catching specific types lets you respond
appropriately to each failure mode.

### ex3 — `ft_custom_errors.py`
**Concept:** Custom exception classes, inheritance for error hierarchies.
Creating domain-specific exceptions (`GardenError` -> `PlantError`, `WaterError`)
makes error handling more precise and code more readable. Catching a parent exception
catches all its children.

### ex4 — `ft_finally_block.py`
**Concept:** `finally` for guaranteed cleanup, resource management.
The `finally` block always executes — whether the `try` succeeded, the `except`
caught something, or even if `return` was called. Essential for closing resources
(files, connections, hardware) reliably.

## Key Takeaways

- `try`/`except` prevents crashes and enables graceful degradation.
- `raise` lets you enforce your own rules and communicate failures clearly.
- Specific exception types enable targeted error handling.
- Custom exceptions create a domain-specific error vocabulary.
- `finally` guarantees cleanup regardless of what happened in the try block.
- Well-designed exception handling is what separates scripts from production code.
