# ModulosPython — Complete Python Learning Path

## About This Repository

This repository contains 11 progressive Python modules (00–10) covering fundamentals
through advanced patterns. Each module is a self-contained project with exercises that
build upon each other, designed to demonstrate understanding during peer evaluations.

---

## Module Map

| Module | Theme | Core Concepts |
|--------|-------|---------------|
| 00 | Growing Code | Functions, variables, control flow, type hints |
| 01 | Code Cultivation | OOP: classes, inheritance, encapsulation |
| 02 | Garden Guardian | Exception handling, custom errors, finally |
| 03 | Data Quest | Collections: lists, tuples, sets, dicts, generators |
| 04 | Data Archivist | File I/O, streams, context managers |
| 05 | Code Nexus | ABC, polymorphism, data pipelines |
| 06 | The Codex | Imports, packages, circular dependencies |
| 07 | DataDeck | Design patterns: factory, mixin, strategy |
| 08 | The Matrix | venv, pip/Poetry, environment variables |
| 09 | Cosmic Data | Pydantic: validation, nested models |
| 10 | FuncMage | Lambdas, closures, decorators, functools |

---

## Module 00 — Python Fundamentals

**What you learn:** These exercises teach the basic building blocks of Python: how to
wrap logic in functions, read values from the user, branch with conditions, repeat code
with loops, and annotate types.

### ex0 — `ft_hello_garden.py`
- Implements: a simple reusable function that prints a greeting.
- How to explain it: "I created a function because the same behavior should live in one
  place instead of being duplicated. The important idea is that a function gives a name to
  a block of code and makes it reusable."
- Oral prompt: "Why is this exercise useful for understanding functions?"

### ex1 — `ft_garden_name.py`
- Implements: input handling and string formatting.
- How to explain it: "The program reads text from the user, stores it in a variable, and
  combines it with fixed text to build the final output. This shows that `input()` returns
  a string and that I need to treat it as text unless I convert it."
- Oral prompt: "What does `input()` return, and why is that important here?"

### ex2 — `ft_plot_area.py`
- Implements: conversion from text to numbers and arithmetic.
- How to explain it: "The script receives values as strings, converts them to integers or
  floats, and performs a calculation. The key point is that user input is not automatically
  numeric, so I must validate and convert it."
- Oral prompt: "Why is conversion necessary before doing arithmetic?"

### ex3 — `ft_harvest_total.py`
- Implements: accumulation through repeated input.
- How to explain it: "I keep adding values into a running total. This is a good example of
  state: the program remembers the previous result as it processes each new input."
- Oral prompt: "What does the running total show about state in a program?"

### ex4 — `ft_plant_age.py`
- Implements: branching with `if`/`else`.
- How to explain it: "The program evaluates a condition and chooses one of two paths.
  The interesting part is the decision logic: one branch runs when the condition is true,
  the other when it is false."
- Oral prompt: "How do `if` and `else` change the behavior of the program?"

### ex5 — `ft_water_reminder.py`
- Implements: a simple threshold check.
- How to explain it: "This exercise repeats the same conditional idea, but with a different
  rule. I would explain that the program checks whether some value exceeds a limit and then
  decides what message to print."
- Oral prompt: "What is the condition being checked in this exercise?"

### ex6 — `ft_count_harvest_*.py`
- Implements: repetition with either iteration or recursion.
- How to explain it: "One version solves the problem with a loop and another with a
  function calling itself. I would highlight that both approaches produce the same result,
  but they differ in style and how they manage state."
- Oral prompt: "What is the difference between using a loop and using recursion here?"

### ex7 — `ft_seed_inventory.py`
- Implements: multiple conditions and type hints.
- How to explain it: "This script shows a decision chain with several possible cases. The
  type annotations make the expected input and output more explicit, which helps both the
  reader and tools such as mypy."
- Oral prompt: "Why are type hints useful in this exercise?"

---

## Module 01 — Object-Oriented Programming

**What you learn:** These exercises show how to model reality with classes: define data,
attach behavior to it, protect it, and reuse code through inheritance.

### ex0 — `ft_garden_intro.py`
- Implements: a simple script with a safe entry point.
- How to explain it: "I use `if __name__ == "__main__":` so the code only runs when the file
  is executed directly and not when it is imported as a module."
- Oral prompt: "Why does the entry point matter when a file is imported?"

### ex1 — `ft_garden_data.py`
- Implements: a class with attributes initialized in the constructor.
- How to explain it: "This is a blueprint for an object. The constructor sets the initial
  state, and `self` allows each instance to keep its own data."
- Oral prompt: "What does `self` represent in this class?"

### ex2 — `ft_plant_growth.py`
- Implements: methods that change object state.
- How to explain it: "The behavior is not only stored in the class but also applied to the
  object. I would say that objects are not just containers of data; they also expose methods
  to modify that data."
- Oral prompt: "How do methods change the state of an object?"

### ex3 — `ft_plant_factory.py`
- Implements: object creation with constructor parameters.
- How to explain it: "The class is designed so that a new object is ready to use immediately
  after creation. This is useful because the constructor centralizes initialization logic."
- Oral prompt: "Why are constructor parameters useful when creating objects?"

### ex4 — `ft_garden_security.py`
- Implements: encapsulation and validation.
- How to explain it: "The internal state is protected, and access is controlled through
  methods. I would explain that this prevents invalid values from entering the object."
- Oral prompt: "What problem does encapsulation solve in this exercise?"

### ex5 — `ft_plant_types.py`
- Implements: inheritance and method overriding.
- How to explain it: "A specialized class extends a more general one and reuses its logic.
  The important idea is that child classes can customize behavior without rewriting everything."
- Oral prompt: "How is inheritance different from simply copying code?"

### ex6 — `ft_garden_analytics.py`
- Implements: class methods and shared behavior.
- How to explain it: "This exercise combines several OOP ideas: shared logic, class-level
  behavior, and counters that track how the system is being used."
- Oral prompt: "What does this exercise show about shared behavior in a class?"

---

## Module 02 — Exception Handling

**What you learn:** These exercises teach how to make programs resilient when something goes
wrong. The goal is not only to avoid crashes, but to make failures explicit and controlled.

### ex0 — `ft_first_exception.py`
- Implements: safe error handling with `try`/`except`.
- How to explain it: "The program attempts an operation that may fail, and if it does, the
  error is caught instead of breaking the whole script. This is a safety net for unexpected
  input or runtime problems."
- Oral prompt: "Why is `try`/`except` useful in this exercise?"

### ex1 — `ft_raise_exception.py`
- Implements: raising a custom error when a rule is violated.
- How to explain it: "I use `raise` to say that the input or state is invalid according to my
  own rules. This is useful because it turns a vague failure into a clear, intentional error."
- Oral prompt: "What is the difference between catching an error and raising one?"

### ex2 — `ft_different_errors.py`
- Implements: specific exception handling.
- How to explain it: "Different problems deserve different responses. I explain that catching
  a broad exception is less precise than handling the specific type of failure that occurred."
- Oral prompt: "Why is it better to handle specific exceptions?"

### ex3 — `ft_custom_errors.py`
- Implements: a small exception hierarchy.
- How to explain it: "I define my own exception classes to represent domain-specific problems.
  The key idea is that the program can distinguish garden-related errors from more general ones."
- Oral prompt: "Why create custom exceptions instead of using built-in ones?"

### ex4 — `ft_finally_block.py`
- Implements: cleanup that always runs.
- How to explain it: "The `finally` block guarantees execution even if an exception is raised
  or a function returns early. This is especially useful for closing files or releasing resources."
- Oral prompt: "Why is `finally` important for cleanup?"

---

## Module 03 — Python Collections

**What you learn:** These exercises teach that Python offers different data structures for
different jobs. The challenge is not just storing values, but choosing the right structure.

### ex0 — `ft_command_quest.py`
- Implements: parsing command-line arguments from `sys.argv`.
- How to explain it: "The script reads arguments passed to Python when the file is executed.
  I would explain that `sys.argv` is a list of strings, so indexing and iteration are the main
  operations involved."
- Oral prompt: "What does `sys.argv` represent in this script?"

### ex1 — `ft_score_analytics.py`
- Implements: statistics over a list of values.
- How to explain it: "The script calculates metrics such as the sum, maximum, and minimum.
  I would mention that it validates input and handles bad values gracefully instead of crashing."
- Oral prompt: "What kind of analysis is being performed over the data?"

### ex2 — `ft_coordinate_system.py`
- Implements: immutable coordinate tuples and parsing.
- How to explain it: "This exercise stores three values together in a tuple, which is ideal
  for fixed-shape data like coordinates. I would explain why tuples are useful when the data
  should not be changed accidentally."
- Oral prompt: "Why is a tuple a good choice for coordinates?"

### ex3 — `ft_achievement_tracker.py`
- Implements: a set to track unique elements.
- How to explain it: "The important idea here is uniqueness. A set removes duplicates, so I
  would explain why it is better than a list when the goal is to keep only one copy of each value."
- Oral prompt: "Why is a set better than a list for this task?"

### ex4 — `ft_inventory_system.py`
- Implements: key-value storage with dictionaries.
- How to explain it: "The program maps names to quantities, which is exactly what a dictionary
  is for. I would explain that lookups are fast and that the data is organized by key rather than position."
- Oral prompt: "Why is a dictionary suitable for storing this data?"

### ex5 — `ft_data_stream.py`
- Implements: lazy generation with a generator.
- How to explain it: "The script yields values one at a time instead of building everything in
  memory at once. I would emphasize that generators are useful for large or streaming datasets."
- Oral prompt: "What makes a generator different from a list here?"

### ex6 — `ft_data_alchemist.py`
- Implements: transformations with comprehensions.
- How to explain it: "This exercise shortens common loops into compact expressions. The key
  point is that comprehensions are readable for simple transformations but should not be overused."
- Oral prompt: "When would you prefer a comprehension over a loop?"

---

## Module 04 — File I/O

**What you learn:** These exercises show how programs interact with the filesystem, read and
write data, and handle input and output streams safely.

### ex0 — `ft_ancient_text.py`
- Implements: reading a file from disk and printing its contents.
- How to explain it: "I open a file, read it line by line, and print the content. The important
  part is handling errors if the file does not exist or cannot be opened."
- Oral prompt: "What is the main purpose of reading a file in this exercise?"

### ex1 — `ft_archive_creation.py`
- Implements: writing content to a new file.
- How to explain it: "The program creates or overwrites a file and stores text in it. I would
  explain that file writing is a form of persistence: data survives the program execution."
- Oral prompt: "Why is writing to a file different from printing to the console?"

### ex2 — `ft_stream_management.py`
- Implements: using standard streams for input and output.
- How to explain it: "The script works with `stdin`, `stdout`, and `stderr` instead of only
  printing to the screen. I would mention that errors should go to `stderr` so normal output
  stays clean."
- Oral prompt: "How do `stdout` and `stderr` differ in this exercise?"

### ex3 — `ft_vault_security.py`
- Implements: safe file handling with a context manager.
- How to explain it: "The file is opened inside a `with` block so it closes automatically.
  This is a good example of resource management: the code is safer and easier to reason about."
- Oral prompt: "Why is a context manager useful when opening files?"

---

## Module 05 — Polymorphism & Abstract Classes

**What you learn:** These exercises teach how to define a common interface and let different
classes implement it in their own way.

### ex0 — `data_processor.py`
- Implements: an abstract base class and concrete processors.
- How to explain it: "The base class defines the contract, and each specific processor adds
  its own behavior. The important point is that the interface is shared even though the
  implementation differs."

### ex1 — `data_stream.py`
- Implements: a dispatcher that sends data to the right processor.
- How to explain it: "The stream does not need to know the exact processor type; it simply
  asks each processor whether it can handle the data. This is the core of polymorphism."

### ex2 — `data_pipeline.py`
- Implements: a modular pipeline with pluggable components.
- How to explain it: "The program builds a workflow where different stages can be swapped or
  extended. I would focus on the idea that the design stays open for future changes."

---

## Module 06 — Python Imports & Packages

**What you learn:** These exercises show how Python discovers and loads code across files and
packages, and why good package structure matters.

### Part I — Alembic
- Implements: importing modules from a package and controlling what the package exports.
- How to explain it: "I would explain that `import` loads code, while `__init__.py` defines
  the public face of the package. The package becomes easier to use when the entry points are clear."

### Part II — Distillation
- Implements: nested imports and package organization.
- How to explain it: "The code demonstrates that modules can be split across directories and
  still be imported in a consistent way. This becomes important when projects get bigger."

### Part III — Transmutation
- Implements: absolute and relative imports.
- How to explain it: "I would compare both styles and explain that they resolve the same
  dependency through different paths. The most important thing is that imports remain explicit and readable."

### Part IV — Kaboom
- Implements: circular import problems and how to avoid them.
- How to explain it: "This exercise shows what happens when two modules depend on each other
  at import time. I would explain the fix: delay the import until it is actually needed."

---

## Module 07 — Design Patterns

**What you learn:** These exercises introduce architectural patterns that solve recurring
problems in a reusable way.

### ex0 — Creature Factory
- Implements: an abstract factory that creates related objects.
- How to explain it: "The factory centralizes object creation so the rest of the program does
  not need to know which concrete class is being created. This makes the system easier to extend."

### ex1 — Capabilities
- Implements: mixins that add behavior without changing the main class hierarchy.
- How to explain it: "I would explain that a mixin contributes capabilities such as healing or
  special actions, while the main class remains focused on its core identity."

### ex2 — Strategy
- Implements: interchangeable behavior at runtime.
- How to explain it: "The creature keeps the same identity, but the strategy decides how it
  acts. This is a good example of separating what an object is from how it behaves."

---

## Module 08 — Environment Management

**What you learn:** These exercises introduce professional Python habits: isolating the
environment, declaring dependencies, and keeping secrets out of source code.

### ex0 — `construct.py`
- Implements: a virtual environment setup script.
- How to explain it: "The script demonstrates that a project can have its own isolated Python
  installation and dependency set. I would explain why this prevents conflicts between projects."

### ex1 — `loading.py`, `requirements.txt`, `pyproject.toml`
- Implements: dependency declaration and reporting.
- How to explain it: "This exercise shows how to declare packages so they can be installed in a
  reproducible way. The explanation should focus on the difference between installing manually
  and using a dependency file."

### ex2 — `oracle.py`, `.env.example`, `.gitignore`
- Implements: configuration from environment variables and secret handling.
- How to explain it: "The program reads values from the environment instead of hardcoding
  them. I would explain that secrets should never be committed to the repository and should
  be stored in a local configuration file."

---

## Module 09 — Pydantic Validation

**What you learn:** These exercises use Pydantic to validate data clearly and declaratively.
Instead of writing many manual checks, the model describes what is accepted.

### ex0 — `space_station.py`
- Implements: a validated model with constraints.
- How to explain it: "The class defines rules such as acceptable ranges and expected field
  types. I would explain that Pydantic checks the data automatically and raises helpful errors
  when the input violates those rules."

### ex1 — `alien_contact.py`
- Implements: cross-field validation and enums.
- How to explain it: "The model includes rules that depend on multiple fields at once. This is
  more powerful than checking each field independently because it captures business logic."

### ex2 — `space_crew.py`
- Implements: nested models and whole-structure validation.
- How to explain it: "The data is organized in a hierarchy of models, and the system validates
  the whole structure together. I would explain that one invalid nested value can make the entire
  submission invalid."

---

## Module 10 — Functional Programming

**What you learn:** These exercises show that functions are first-class objects in Python.
You can pass them around, compose them, store them, cache them, and decorate them.

### ex0 — `lambda_spells.py`
- Implements: small anonymous functions for transformations.
- How to explain it: "The exercise demonstrates that `lambda` is useful for short inline
  functions, especially when used with `map`, `filter`, or `sorted`."

### ex1 — `higher_magic.py`
- Implements: higher-order functions that receive or return functions.
- How to explain it: "I would explain that a function can be treated as data: it can be passed
  to another function and used as a building block for more complex behavior."

### ex2 — `scope_mysteries.py`
- Implements: closures that capture state from the surrounding scope.
- How to explain it: "This exercise shows that a function can remember values from the place
  where it was created. That is the essence of a closure."

### ex3 — `functools_artifacts.py`
- Implements: functional utilities from `functools`.
- How to explain it: "I would explain how tools such as `reduce`, `partial`, and `lru_cache`
  help structure code around transformations and reuse."

### ex4 — `masters_tower.py`
- Implements: decorators that add behavior to functions.
- How to explain it: "The point is that a decorator wraps existing behavior without changing
  the original function directly. I would describe it as a reusable layer of logic such as
  timing, logging, or authentication."

---

## How to Verify Everything Works

```powershell
# From the workspace root:
.venv\Scripts\flake8 . --exclude=.venv,.mypy_cache,.git
.venv\Scripts\python run_all_mains.py
foreach ($i in 0..10) {
    $mod = "Python Module {0:D2}" -f $i
    .venv\Scripts\python -m mypy $mod --ignore-missing-imports
}
```

## Tips for Peer Evaluation

1. **Explain the WHY, not just the HOW.** Don't just say "I used a try/except" —
   explain why the program would crash without it and what scenario you're protecting against.

2. **Trace execution.** Be ready to walk through your code line by line, explaining
   what happens at each step with concrete values.

3. **Know the alternatives.** If asked "why did you use a set here?", explain what
   would happen with a list (duplicates, O(n) lookup) vs a set (unique, O(1) lookup).

4. **Understand error messages.** If mypy or flake8 flags something, know why. "I added
   `# type: ignore` because Pydantic handles str→datetime coercion at runtime, which
   mypy can't verify statically."

5. **Connect concepts across modules.** Module 02's custom exceptions appear in Module 07's
   strategy pattern. Module 05's ABC appears in Module 07's factories. Show you understand
   how concepts build on each other.

6. **Modify on the spot.** If asked to change behavior (add a new plant type, add a new
   strategy), you should be able to do it quickly — proving you wrote it, not copied it.

## Short Oral Answers for Evaluations

Use these as ready-made mini-explanations. They are intentionally concise, but they show
that you understand not just the syntax, but the purpose of the code.

Each exercise below follows the same pattern:
- **Question:** what the evaluator could ask you.
- **Answer:** a short response you can say aloud.
- **Why it matters:** the core concept the exercise is trying to teach.

### Module 00

#### ex0 — `ft_hello_garden.py`
- **Question:** What does this exercise implement?
- **Answer:** "It implements a reusable function that prints a greeting. The important idea is
  that the logic lives in one place and can be used again instead of being duplicated."
- **Why it matters:** This teaches that functions are a way to package behavior so it can be
  reused and tested more easily.

#### ex1 — `ft_garden_name.py`
- **Question:** What does this exercise show?
- **Answer:** "It shows how to read input from the user and combine it with fixed text to build
  a message. The key point is that `input()` returns a string."
- **Why it matters:** This reinforces that user input is text by default and must be handled as
  such unless converted.

#### ex2 — `ft_plot_area.py`
- **Question:** Why is conversion important here?
- **Answer:** "The values come from the user as text, so I must convert them to numbers before
  doing arithmetic. Without that, the calculation would not work correctly."
- **Why it matters:** This shows the difference between raw input and numeric data.

#### ex3 — `ft_harvest_total.py`
- **Question:** What is the main idea of this exercise?
- **Answer:** "It keeps a running total as new values are entered. This shows how state is
  accumulated over multiple iterations."
- **Why it matters:** This teaches how variables can store cumulative information across loop
  iterations.

#### ex4 — `ft_plant_age.py`
- **Question:** What does the program decide?
- **Answer:** "It evaluates a condition and chooses one of two branches depending on whether the
  condition is true or false."
- **Why it matters:** This introduces control flow through branching.

#### ex5 — `ft_water_reminder.py`
- **Question:** What concept is being reinforced here?
- **Answer:** "It reinforces conditional logic with a threshold check. The program decides what
  message to print based on whether a value exceeds a limit."
- **Why it matters:** This shows how the same branching pattern can be reused with different
  conditions.

#### ex6 — `ft_count_harvest_*.py`
- **Question:** What is the difference between the two versions?
- **Answer:** "One version uses iteration and the other uses recursion, but both solve the same
  problem. The comparison helps show different ways to control repetition."
- **Why it matters:** This helps explain that the same outcome can be achieved with different
  control-flow strategies.

#### ex7 — `ft_seed_inventory.py`
- **Question:** What does this exercise demonstrate?
- **Answer:** "It demonstrates decision chains and type hints. The code is clearer because the
  expected input and output are more explicit."
- **Why it matters:** This reinforces that good code should be explicit about both logic and
  expected types.

### Module 01

#### ex0 — `ft_garden_intro.py`
- **Question:** Why is the entry point used?
- **Answer:** "It prevents the code from running on import and ensures the script only executes
  when it is run directly."

#### ex1 — `ft_garden_data.py`
- **Question:** What does the class represent?
- **Answer:** "It represents an object with initial state defined by the constructor. Each
  instance can keep its own data."

#### ex2 — `ft_plant_growth.py`
- **Question:** What does this exercise show about objects?
- **Answer:** "It shows that objects can have behavior and that methods can change their state."

#### ex3 — `ft_plant_factory.py`
- **Question:** Why are constructor parameters useful?
- **Answer:** "They allow objects to be created already initialized, which makes the code more
  readable and reduces repetitive setup."

#### ex4 — `ft_garden_security.py`
- **Question:** What concept is central here?
- **Answer:** "Encapsulation is central here because the object controls access to its internal
  data and validates changes."

#### ex5 — `ft_plant_types.py`
- **Question:** What does inheritance add?
- **Answer:** "It allows a child class to reuse and extend the behavior of a parent class without
  rewriting everything."

#### ex6 — `ft_garden_analytics.py`
- **Question:** What does this exercise combine?
- **Answer:** "It combines several OOP ideas such as shared behavior, class-level logic, and
  tracking how the system is used."

### Module 02

#### ex0 — `ft_first_exception.py`
- **Question:** Why is exception handling useful?
- **Answer:** "It allows the program to recover from an error instead of crashing. That makes the
  code more robust."

#### ex1 — `ft_raise_exception.py`
- **Question:** What is the purpose of raising an exception?
- **Answer:** "It makes invalid input or invalid state explicit. Instead of silently continuing,
  the program stops and signals that something is wrong."

#### ex2 — `ft_different_errors.py`
- **Question:** Why handle different error types separately?
- **Answer:** "Because different failures may need different responses. Catching the specific
  type is more precise than catching everything at once."

#### ex3 — `ft_custom_errors.py`
- **Question:** Why create custom exceptions?
- **Answer:** "They represent domain-specific problems in a clearer way and make the code easier
  to understand."

#### ex4 — `ft_finally_block.py`
- **Question:** Why is `finally` important?
- **Answer:** "It guarantees that cleanup code runs even if an exception occurs or the function
  exits early."

### Module 03

#### ex0 — `ft_command_quest.py`
- **Question:** What does this exercise parse?
- **Answer:** "It parses values passed from the command line. The important point is that these
  values arrive as strings."

#### ex1 — `ft_score_analytics.py`
- **Question:** What does the script calculate?
- **Answer:** "It calculates summary statistics such as the sum, maximum, and minimum over a
  list of values."

#### ex2 — `ft_coordinate_system.py`
- **Question:** Why use a tuple here?
- **Answer:** "Because the data has a fixed shape and should not be changed accidentally. A tuple
  is a good way to represent coordinates."

#### ex3 — `ft_achievement_tracker.py`
- **Question:** Why is a set appropriate?
- **Answer:** "Because the aim is to keep only unique values. A set removes duplicates naturally."

#### ex4 — `ft_inventory_system.py`
- **Question:** What structure is used and why?
- **Answer:** "A dictionary is used because the data is stored as key-value pairs, which allows
  fast lookup by name."

#### ex5 — `ft_data_stream.py`
- **Question:** Why use a generator?
- **Answer:** "Because it produces values lazily and does not need to build everything in memory
  at once."

#### ex6 — `ft_data_alchemist.py`
- **Question:** What does this exercise show about comprehensions?
- **Answer:** "It shows how a compact comprehension can replace a longer loop for simple
  transformations."

### Module 04

#### ex0 — `ft_ancient_text.py`
- **Question:** What does the script do with files?
- **Answer:** "It opens a file, reads it, and prints its contents while handling errors if the
  file cannot be opened."

#### ex1 — `ft_archive_creation.py`
- **Question:** Why write to a file?
- **Answer:** "Because the data needs to persist after the program finishes instead of disappearing
  after printing to the console."

#### ex2 — `ft_stream_management.py`
- **Question:** What is the special point of this exercise?
- **Answer:** "It uses standard streams so normal output and errors can be separated clearly."

#### ex3 — `ft_vault_security.py`
- **Question:** Why use a context manager?
- **Answer:** "Because it ensures the file closes automatically and safely even if an error occurs."

### Module 05

#### ex0 — `data_processor.py`
- **Question:** What does the abstract base class define?
- **Answer:** "It defines a common interface that several concrete processors implement in their
  own way."

#### ex1 — `data_stream.py`
- **Question:** What is the main idea of polymorphism here?
- **Answer:** "The stream sends data to the appropriate processor without needing to know its
  exact type in advance."

#### ex2 — `data_pipeline.py`
- **Question:** Why is this design useful?
- **Answer:** "Because the pipeline can be extended or modified by plugging in different
  components without changing the overall structure."

### Module 06

#### Alembic / Distillation / Transmutation / Kaboom
- **Question:** What do these exercises teach?
- **Answer:** "They teach how Python loads modules across packages, how imports are organized,
  and how circular dependencies can be avoided."

### Module 07

#### ex0 — Creature Factory
- **Question:** What is the purpose of the factory?
- **Answer:** "It centralizes object creation so the rest of the code does not need to know the
  exact concrete class being created."

#### ex1 — Capabilities
- **Question:** What do mixins add?
- **Answer:** "They add extra behavior without changing the main class hierarchy."

#### ex2 — Strategy
- **Question:** What does the strategy pattern change?
- **Answer:** "It changes how an object behaves while keeping its identity the same."

### Module 08

#### ex0 — `construct.py`
- **Question:** Why is isolation important?
- **Answer:** "It keeps the project's Python environment separate from other projects and avoids
  dependency conflicts."

#### ex1 — `loading.py`, `requirements.txt`, `pyproject.toml`
- **Question:** What is the purpose of these files?
- **Answer:** "They declare dependencies so the project can be installed and run consistently."

#### ex2 — `oracle.py`, `.env.example`, `.gitignore`
- **Question:** Why keep secrets out of the source code?
- **Answer:** "Because configuration should be local and safe, and secrets should not be exposed
  in the repository."

### Module 09

#### ex0 — `space_station.py`
- **Question:** What does Pydantic validate here?
- **Answer:** "It validates that the input matches the constraints defined in the model."

#### ex1 — `alien_contact.py`
- **Question:** What makes this validation more advanced?
- **Answer:** "It checks relationships between fields and applies business rules, not just single
  values."

#### ex2 — `space_crew.py`
- **Question:** What is the main idea of nested models?
- **Answer:** "They validate data that is organized into a hierarchy of objects, so one invalid
  child value can make the whole structure invalid."

### Module 10

#### ex0 — `lambda_spells.py`
- **Question:** Why use a lambda here?
- **Answer:** "Because it is useful for short inline transformations that do not need a full
  function definition."

#### ex1 — `higher_magic.py`
- **Question:** What is a higher-order function?
- **Answer:** "It is a function that takes another function as input or returns one as output."

#### ex2 — `scope_mysteries.py`
- **Question:** What is a closure?
- **Answer:** "It is a function that remembers values from the surrounding scope where it was
  created."

#### ex3 — `functools_artifacts.py`
- **Question:** What do utilities like `reduce` and `lru_cache` help with?
- **Answer:** "They help structure code around functional transformations and reuse results when
  appropriate."

#### ex4 — `masters_tower.py`
- **Question:** What does a decorator do?
- **Answer:** "It wraps a function with extra behavior such as timing, logging, or
  authentication without changing the original function directly."
