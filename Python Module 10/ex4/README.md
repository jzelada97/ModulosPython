Exercise 4 — Master's Tower (decorators & staticmethod)

File: `decorator_mastery.py`

Contains:
- `spell_timer(func)` — decorator that prints casting/completion messages and
  times execution (uses `functools.wraps`).
- `power_validator(min_power)` — decorator factory that rejects a cast below
  `min_power`.
- `retry_spell(max_attempts)` — decorator factory that retries a failing spell
  up to `max_attempts` times.
- `MageGuild` class demonstrating `@staticmethod` (`validate_mage_name`) and an
  instance method (`cast_spell`) decorated with `power_validator(min_power=10)`.

Run:
python ex4/decorator_mastery.py
