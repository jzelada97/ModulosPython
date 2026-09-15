print('=== Kaboom 1 ===')
print('Access to alchemy/grimoire/dark_spellbook.py directly')
print('Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION')
# The narration above must run BEFORE the import: the import itself is what
# raises the uncaught ImportError (circular dependency), so moving it to the
# top of the file like the other scripts would silently drop these lines
# from the transcript. This E402 is therefore intentional, not an oversight.
from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402

# If import succeeds (it shouldn't), try to call it
print(dark_spell_record('Forbidden', 'bats, frogs'))
