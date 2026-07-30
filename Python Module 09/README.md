Module 09 — Cosmic Data (Pydantic models & validation)

Implemented exercises:
- ex0/space_station.py — `SpaceStation` model demonstrating field constraints and validation errors.
- ex1/alien_contact.py — `AlienContact` model with `ContactType` enum and `@model_validator` business rules.
- ex2/space_crew.py — `CrewMember` and `SpaceMission` nested models with mission-level validation.

Notes:
- All exercises use Pydantic v2-style APIs (`@model_validator`). If `pydantic` is not installed, the scripts print informative errors.

Run examples with:
python ex0/space_station.py
python ex1/alien_contact.py
python ex2/space_crew.py
