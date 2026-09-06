# Module 04 — Data Archivist: File Operations

## Overview

This module teaches file I/O — reading, writing, and managing data persistence. Programs
that only work with in-memory data lose everything when they stop. File operations
make data survive beyond program execution.

## Exercises & Learning Objectives

### ex0 — `ft_ancient_text.py`
**Concept:** Opening files, reading content, `open()`/`close()`, error handling.
Reads a file specified via command-line argument and displays its contents. Handles
missing files and permission errors gracefully. Introduces the file handle type returned
by `open()` and the importance of calling `close()`.

### ex1 — `ft_archive_creation.py`
**Concept:** Writing to files, creating/overwriting files, user interaction.
Extends ex0 by transforming content (appending a character to each line) and optionally
saving to a new file. Demonstrates `open()` with write mode and the difference between
creating and overwriting.

### ex2 — `ft_stream_management.py`
**Concept:** `sys.stdin`/`sys.stdout`/`sys.stderr`, stream separation.
Introduces the three standard I/O streams. Error messages go to stderr (not stdout),
and user input can be read without `input()` by using `sys.stdin.readline()` directly.
Understanding stream separation is essential for piping and scripting.

### ex3 — `ft_vault_security.py`
**Concept:** Context managers (`with` statement), guaranteed resource cleanup.
The `with` statement ensures files are always closed — even if exceptions occur. This is
Python's idiomatic pattern for resource management and eliminates the need for manual
`try`/`finally`/`close()` patterns.

## Key Takeaways

- `open()` returns a file object; always close it (or use `with`).
- Read modes (`'r'`) vs write modes (`'w'`) control how files are accessed.
- `sys.stderr` separates error output from normal output — essential for Unix pipelines.
- The `with` statement is Python's guarantee that resources get cleaned up.
- File I/O errors (missing files, permissions) must be handled gracefully.
- Data persistence transforms scripts into useful tools.
