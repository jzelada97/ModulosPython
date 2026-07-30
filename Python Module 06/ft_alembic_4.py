print('=== Alembic 4 ===')
print("Accessing the alchemy module using 'import alchemy'")
import alchemy

print(f"Testing create_air: {alchemy.create_air()}")
print('Now show that not all functions can be reached')
print('This will raise an exception!')
# Attempt to access create_earth which is not exposed in package __init__
print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
