Exercise 2 — Space Crew Management

File: `space_crew.py`

Spec:
- Define `Rank` enum, `CrewMember` and `SpaceMission` Pydantic models.
- Implement `@model_validator(mode='after')` rules:
  - mission_id starts with 'M'
  - at least one Commander or Captain
  - long missions (>365 days) require 50% experienced crew (>=5 years)
  - all crew must be active

Run:
python ex2/space_crew.py
