Exercise 3 — Vault Security

Script: `ft_vault_security.py`

Spec:
- Implement `secure_archive(filename, mode='r', content=None) -> (bool, str)` using
  the `with` statement. It must return `(True, content)` on success or `(False, error)` on failure.
- Demonstrate reading and writing using `secure_archive` in `__main__`.
