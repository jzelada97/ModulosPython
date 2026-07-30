from .ex3.ft_custom_errors import PlantError  # relative import within package won't work as script; import guarded in __main__


def water_plant(plant_name: str) -> None:
    # succeed if capitalized
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water:'{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    # first valid plants
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")

    # now an invalid sequence
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    # To avoid import issues when running directly, recreate PlantError locally if needed
    try:
        from ft_custom_errors import PlantError as LocalPlantError  # try local import
    except Exception:
        class LocalPlantError(Exception):
            pass
    # Monkey patch name used in water_plant if needed (the function raises PlantError by class name)
    test_watering_system()
