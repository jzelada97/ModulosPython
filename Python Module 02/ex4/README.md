Exercise 4 — Finally Block - Always Clean Up

Functions:
- `water_plant(plant_name: str)` : waters plant if capitalized, else raises `PlantError`.
- `test_watering_system()` : demonstrates opening/closing watering system and uses try/except/finally to guarantee cleanup.

Spec: ensure cleanup (closing watering system) always runs, even when errors occur.
