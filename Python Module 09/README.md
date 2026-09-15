# Module 09 — Cosmic Data: Pydantic Models & Validation

## Overview

This module introduces Pydantic v2 — Python's most popular data validation library.
Instead of manually writing validation code (like Module 02's exception handling),
Pydantic lets you declare what valid data looks like and handles the rest automatically.

The subject also ships a `data_generator.tar` archive as an optional helper: it contains
`data_generator.py` (generates realistic test data for all three exercises),
`data_exporter.py` (exports that data as JSON/CSV/Python), and a pre-generated
`generated_data/` folder. These tools are not graded deliverables — nothing in the
evaluation checklist below references them — they only exist to give you sample data to
throw at your models while developing. `json`, `csv`, and other standard-library modules
are explicitly authorized if you choose to use them.

## Exercises & Learning Objectives

### ex0 — `space_station.py`
**What this exercise wants you to teach you:** how declarative field constraints replace
repetitive manual `if` validation.

**Concept:** `BaseModel`, `Field` constraints, automatic type coercion.
Defines a `SpaceStation` model with constraints (min/max lengths, numeric ranges,
optional fields with defaults). Pydantic automatically validates input, converts
compatible types (string to datetime), and raises detailed `ValidationError` messages.

**Why it matters:** Manual validation code is repetitive and error-prone. Pydantic
replaces dozens of `if` checks with declarative field definitions. The same model
serves as documentation, validation, and serialization.

### ex1 — `alien_contact.py`
**What this exercise wants you to teach you:** cross-field/business-rule validation via
`@model_validator`, going beyond single-field checks.

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
**What this exercise wants you to teach you:** nested model validation, and how
hierarchical real-world data (a mission with a crew list) gets validated as a whole.

**Concept:** Nested models, list validation, complex relationships.
`SpaceMission` contains a list of `CrewMember` models. Validation rules span the
entire mission: crew must include a commander, long missions need experienced crew,
all members must be active.

**Why it matters:** Real data is hierarchical. Pydantic handles nested validation
automatically — if a crew member is invalid, the entire mission validation fails with
a clear path to the error. This is the foundation for API request validation in
FastAPI and similar frameworks.

## Evaluation Checklist

This section mirrors the official 42 peer-evaluation scale for Python Module 09, so it
doubles as a "did I meet the grading bar" reference during defense.

### Preliminaries
- [x] Required files exist: `ex0/space_station.py`, `ex1/alien_contact.py`,
  `ex2/space_crew.py`.
- [x] Every script runs without errors (`python3 ex0/space_station.py`, etc.) and prints
  both a successful case and a validation-error case.
- [x] Valid **and** invalid data scenarios are demonstrated for each exercise — outputs
  are produced by real Pydantic validation, not hardcoded strings.
- [x] Uses `BaseModel`, `Field`, and `@model_validator` (Pydantic v2 style).
- [x] No deprecated `@validator` decorator anywhere — only `@model_validator(mode='after')`.

### Exercise 0 — Space Station Data (`ex0/space_station.py`)
- [x] `SpaceStation` inherits from `BaseModel`.
- [x] Fields use `Field()` with proper constraints: `station_id` (3–10 chars),
  `name` (1–50 chars), `crew_size` (1–20), `power_level` / `oxygen_level` (0–100),
  `notes` (optional, ≤200 chars).
- [x] Accepts valid station data and constructs an instance successfully.
- [x] Invalid data (e.g. `crew_size > 20`, out-of-range power/oxygen, unparsable
  `last_maintenance`) raises a `ValidationError` — demonstrated with `crew_size=25`,
  `power_level=120.0`, `oxygen_level=-5.0`, and `last_maintenance='not a datetime'`.
- [x] Output shows both the successful creation and the validation errors.
- [x] `notes` is an optional field (`Optional[str]`, default `None`).
- [x] `last_maintenance: datetime` accepts an ISO string (`'2024-01-01T12:00:00'`) via
  Pydantic's automatic type coercion, and rejects an unparsable string with a clear
  `datetime_from_date_parsing` error.
- [x] Code is well-structured and readable (single model, single `main()`, no
  duplication).

### Exercise 1 — Alien Contact Data (`ex1/alien_contact.py`)
- [x] `AlienContact` uses `@model_validator(mode='after')` for custom, cross-field
  validation.
- [x] `ContactType` enum is defined (`radio`, `visual`, `physical`, `telepathic`) and
  used as the type of `contact_type`.
- [x] `message_received` combines `Optional[str]` typing **and** `max_length=500` in a
  single `Field()` declaration.
- [x] Demonstration shows one valid contact and one validation error.
- [x] No deprecated `@validator` decorators are used.
- [x] **Custom rule — ID prefix:** a `contact_id` not starting with `"AC"` raises
  `ValueError('Contact ID must start with "AC"')` (verified with `contact_id='XX2024'`).
- [x] **Custom rule — telepathic witnesses:** `contact_type='telepathic'` with
  `witness_count < 3` raises a validation error (verified interactively).
- [x] **Custom rule — strong signal needs a message:** `signal_strength > 7.0` with
  `message_received=None` raises a validation error (verified interactively).
- [x] **Custom rule — physical contact needs verification:** `contact_type='physical'`
  with `is_verified=False` raises a validation error (verified interactively).
- [x] `is_verified` defaults to `False` when not specified.
- [x] The validator returns `self` (required by `mode='after'`).
- [x] Error messages are specific and human-readable (e.g. `"Telepathic contact requires
  at least 3 witnesses"` rather than a generic message).

### Exercise 2 — Space Crew Management (`ex2/space_crew.py`)
- [x] `CrewMember` and `SpaceMission` are both properly defined `BaseModel` subclasses.
- [x] `SpaceMission.crew` is a `List[CrewMember]` — a nested-model field, not a list of
  dicts.
- [x] All 5 ranks are implemented in the `Rank` enum: `cadet`, `officer`, `lieutenant`,
  `captain`, `commander`.
- [x] Mission validation rules are implemented and individually verified:
  - a crew with no `commander`/`captain` is rejected
    (`"Must have at least one Commander or Captain"`);
  - a mission with `duration_days > 365` and fewer than 50% of crew having
    `years_experience >= 5` is rejected;
  - a mission with any inactive crew member is rejected, including the
    "active Commander + inactive Captain" case (rejected because the Captain is
    inactive, per the "all crew must be active" rule);
  - a `mission_id` not starting with `"M"` is rejected.
- [x] Demonstration prints mission details together with each crew member's rank and
  specialization.
- [x] Invalid missions are rejected — the shipped demo now uses `mission_id='MBAD0001'`
  (5-15 characters, starts with `"M"`) with a crew that has no Commander/Captain, so it
  correctly triggers the model validator's `"Must have at least one Commander or
  Captain"` error, matching the subject's own expected-output example. Confirmed by
  running `ex2/space_crew.py` directly. The "inactive crew" and "long mission needs
  experienced crew" rules were independently verified at the REPL rather than in the
  shipped demo.
- [x] `mission_status` defaults to `"planned"` when not specified.
- [x] A `budget_millions` above the `10000.0` ceiling is rejected by the `Field`
  constraint (`le=10000.0`).
- [x] Edge cases (missing high-ranking officer, inexperienced crew on a long mission,
  inactive members, over-budget mission) all behave correctly when tested directly
  against the models, not just through the two scenarios hardcoded in `main()`.

### Code Quality and Best Practices (applies to all three exercises)
- [x] Code targets Python 3.10+ syntax (`str | None`-style unions are not required here
  since `Optional[...]` from `typing` is used consistently; run on Python 3.12).
- [x] `flake8` reports zero errors against the repo's `.flake8` config
  (`max-line-length = 120`).
- [x] Type hints are present on every function/method, including `main() -> None` and
  every `@model_validator` (`-> 'SpaceStation'`, `-> 'AlienContact'`, `-> 'SpaceMission'`).
- [x] Docstrings are **not required** for this module (per the eval sheet) and are
  intentionally omitted.
- [x] Naming follows Python conventions (`snake_case` fields/functions, `PascalCase`
  classes).
- [x] Validation rules are implemented clearly, one condition per `if`, with a
  descriptive `ValueError` message each.
- [x] Demonstration output is informative: it labels each printed value and separates
  the "valid" and "invalid" sections with banners.
- [x] `Field()` constraints are used appropriately across all three models (lengths,
  numeric ranges, list length bounds).
- [x] `@model_validator` is used correctly (`mode='after'`, returns `self`) in both
  `ex1` and `ex2`.
- [x] Enums (`ContactType`, `Rank`) are used where the domain has a fixed set of valid
  values.
- [x] No deprecated Pydantic v1 features (`@validator`, `class Config`, `.dict()`) are
  used anywhere in the module.

## Defense Prep — Questions From the Evaluation Sheet

These are the exact live-questioning prompts from the 42 evaluation sheet, kept as
question-then-answer flashcards so you can rehearse each one before defense.

### Exercise 0

*"Is the datetime field properly handled? What happens when you pass a string timestamp
in 'last_maintenance'?"*
Pydantic coerces an ISO-format string (e.g. `'2024-01-01T12:00:00'`) into a real
`datetime` automatically; an unparsable string (`'not a datetime'`) raises a
`ValidationError` with a `datetime_from_date_parsing` message, demonstrated in `main()`.

### Exercise 1

Eval sheet's "Custom Validation Rules" section, exact prompts:

*"Try creating a contact with ID not starting with 'AC' - does it fail?"*
Yes, raises `ValueError('Contact ID must start with "AC"')`.

*"Try telepathic contact with < 3 witnesses - does it fail?"*
Yes.

*"Try strong signal without message - does it fail?"*
Yes, `signal_strength > 7.0` with `message_received=None` raises.

*"Try physical contact type which is not verified - does it fail?"*
Yes.

*"Try to create a contact without specifying is_verified. Is it False by default?"*
Yes, `is_verified: bool = False`.

*"Does the validator properly return 'self'?"*
Yes, required by `@model_validator(mode='after')`.

*"Are the validation error messages clear and helpful?"*
Yes — each rule raises a distinct, descriptive message rather than a generic one.

### Exercise 2

Eval sheet's "Nested Models Functionality" section, exact prompts:

*"Can you create individual `CrewMember` objects?"*
Yes, standalone.

*"Does the `SpaceMission` properly validate its crew list?"*
Yes, both per-member field constraints and the mission-level rules re-run whenever a
mission is built.

*"Create a `SpaceMission` with one active Commander and one inactive Captain. What
happens?"*
Rejected — the "must have a Commander/Captain" rule is satisfied, but the separate "all
crew members must be active" rule fails because the Captain is inactive, so the mission
is still invalid overall.

*"Try to create a `SpaceMission` without specifying the status. Is it 'planned' by
default?"*
Yes, `mission_status: str = 'planned'`.

*"Try to create a `SpaceMission` over budget. What happens?"*
`budget_millions` above `10000.0` is rejected by the `Field(le=10000.0)` constraint
before the model-level validator even runs.

*"Does the code handle edge cases appropriately?"*
Yes, each rule was independently verified (see the checklist item above).

### Understanding and Learning

*(Eval sheet's exact framing — assessed by discussion, not by reading code.)*

- Do the examples demonstrate proper Pydantic usage?
- Are the validation rules meaningful and well-thought-out (not arbitrary)?
- Does the code show progression from basic (`Field` constraints in ex0) to advanced
  concepts (cross-field `@model_validator` rules in ex1, nested models in ex2)?
- Would this code serve as a good learning example for others? Be ready to walk through
  *why* each constraint/rule exists (e.g. why a mission needs a Commander/Captain, why
  long missions need experienced crew), not just recite that it does.

## Key Takeaways

- **`BaseModel`** turns a class definition into a validation powerhouse.
- **`Field(...)`** declares constraints declaratively (min, max, ge, le, regex).
- **`@model_validator`** handles cross-field and business logic validation.
- **Nested models** validate hierarchical data structures automatically.
- **Enums** restrict fields to predefined valid values.
- Pydantic v2 uses `@model_validator(mode='after')` — not the deprecated `@validator`.
- These patterns are directly applicable to REST API development (FastAPI uses Pydantic).
