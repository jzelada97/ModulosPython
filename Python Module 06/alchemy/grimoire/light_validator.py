def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]
    lower = ingredients.lower()
    valid = any(a in lower for a in allowed)
    return f"{ingredients} - {'VALID' if valid else 'INVALID'}"
