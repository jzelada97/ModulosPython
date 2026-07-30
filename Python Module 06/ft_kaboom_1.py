print('=== Kaboom 1 ===')
print('Access to alchemy/grimoire/dark_spellbook.py directly')
print('Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION')
from alchemy.grimoire.dark_spellbook import dark_spell_record

# If import succeeds (it shouldn't), try to call it
print(dark_spell_record('Forbidden', 'bats, frogs'))
