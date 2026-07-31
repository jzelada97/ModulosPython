def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        # ValueError
        int('abc')
    elif operation_number == 1:
        # ZeroDivisionError
        _ = 1 / 0
    elif operation_number == 2:
        # FileNotFoundError
        open('/non/existent/file')
    elif operation_number == 3:
        # TypeError
        _ = 'a' + 1  # type: ignore[operator]  # purposeful TypeError
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            if i >= 4:
                print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        except Exception as e:
            print(f"Caught Exception: {e}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
