Exercise 1 — Agricultural Data Validation Pipeline

Functions:
- `input_temperature(temp_str: str) -> int` : converts string to int and raises ValueError if out of range (0..40)
- `test_temperature() -> None` : tests valid, invalid, and extreme values; demonstrates exception messages

Spec: range checks must raise exceptions with informative messages and tests must handle them.
