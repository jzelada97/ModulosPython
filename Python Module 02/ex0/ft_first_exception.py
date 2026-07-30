def input_temperature(temp_str: str) -> int:
    """Convert input string to int temperature."""
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    tests = ["25", "abc"]
    for t in tests:
        print(f"Input data is'{t}'")
        try:
            temp = input_temperature(t)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
