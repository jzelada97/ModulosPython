# Module 09 — Cosmic Data: Pydantic Models & Validation

## Overview

This module introduces Pydantic v2 — Python's most popular data validation library.
Instead of manually writing validation code (like Module 02's exception handling),
Pydantic lets you declare what valid data looks like and handles the rest automatically.

## Exercises & Learning Objectives

### ex0 — `space_station.py`
**Concept:** `BaseModel`, `Field` constraints, automatic type coercion.
Defines a `SpaceStation` model with constraints (min/max lengths, numeric ranges,
optional fields with defaults). Pydantic automatically validates input, converts
compatible types (string to datetime), and raises detailed `ValidationError` messages.

**Why it matters:** Manual validation code is repetitive and error-prone. Pydantic
replaces dozens of `if` checks with declarative field definitions. The same model
serves as documentation, validation, and serialization.

### ex1 — `alien_contact.py`
**Concept:** `@model_validator`, custom business rules, Enum fields.
Goes beyond field-level constraints to implement cross-field validation rules:
- Contact IDs must start with "AC"
- Physical contacts require verification
- Telepathic contacts need 3+ witnesses
- Strong signals should include messages

**Why it matters:** Real-world validation isn't just "is this a number between 0 and 10."
It's "if this field is X, then that field must be Y." Model validators implement these
complex business rules in one clean place.

### ex2 — `space_crew.py`
**Concept:** Nested models, list validation, complex relationships.
`SpaceMission` contains a list of `CrewMember` models. Validation rules span the
entire mission: crew must include a commander, long missions need experienced crew,
all members must be active.

**Why it matters:** Real data is hierarchical. Pydantic handles nested validation
automatically — if a crew member is invalid, the entire mission validation fails with
a clear path to the error. This is the foundation for API request validation in
FastAPI and similar frameworks.

## Key Takeaways

- **`BaseModel`** turns a class definition into a validation powerhouse.
- **`Field(...)`** declares constraints declaratively (min, max, ge, le, regex).
- **`@model_validator`** handles cross-field and business logic validation.
- **Nested models** validate hierarchical data structures automatically.
- **Enums** restrict fields to predefined valid values.
- Pydantic v2 uses `@model_validator(mode='after')` — not the deprecated `@validator`.
- These patterns are directly applicable to REST API development (FastAPI uses Pydantic).
