Exercise 7 — Seed Inventory with Type Annotations

Function: `ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None`

Spec:
- Use type annotations (required).
- Print formatted inventory messages depending on `unit`:
  - "packets": "<Name> seeds: <quantity> packets available"
  - "grams": "<Name> seeds: <quantity> grams total"
  - "area": "<Name> seeds: covers <quantity> square meters"
- If unit unknown, print: "Unknown unit type"

The implementation in `ft_seed_inventory.py` includes annotations and prints matching messages.
