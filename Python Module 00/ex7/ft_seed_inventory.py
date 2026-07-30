def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(name + " seeds: " + str(quantity) + " packets available")
    elif unit == "grams":
        print(name + " seeds: " + str(quantity) + " grams total")
    elif unit == "area":
        print(name + " seeds: covers " + str(quantity) + " square meters")
    else:
        print("Unknown unit type")
