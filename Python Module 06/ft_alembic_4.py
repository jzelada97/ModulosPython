import alchemy

print('=== Alembic 4 ===')
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print('Now show that not all functions can be reached')
print('This will raise an exception!')
# Attempt to access create_earth which is not exposed in package __init__
try:
    # No "type: ignore" here on purpose: the subject states this line must
    # also raise a mypy error, since create_earth is not part of alchemy's
    # exposed interface (alchemy/__init__.py never imports it).
    hidden = alchemy.create_earth()
    print(f"Testing the hidden create_earth: {hidden}")
except AttributeError as e:
    print(f"AttributeError: {e}")
    print(
        "create_earth is defined in alchemy.elements but not exposed "
        "via __init__"
    )
