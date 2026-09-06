Exercise 1 — Alien Contact Logs

File: `alien_contact.py`

Spec:
- Define `ContactType` enum and `AlienContact` Pydantic model.
- Implement `@model_validator(mode='after')` with business rules:
  - contact_id must start with 'AC'
  - physical reports must be verified
  - telepathic requires at least 3 witnesses
  - strong signals (>7.0) require a `message_received`

Run:
python ex1/alien_contact.py
