# Module 05 — Code Nexus: Polymorphic Data Streams

## Overview

This module teaches abstract classes, polymorphism, and method overriding through a
data processing pipeline architecture. The key insight: different data types can be
processed through a single interface without the caller knowing (or caring) about the
specific implementation.

The subject's General Instructions apply to all three exercises:
- Python 3.10 or later.
- Code must adhere to the `flake8` coding standard.
- All code must include comprehensive type annotations, checked with `mypy`.
- Exception handling must protect the data streams from corruption.
- Authorized imports are limited to `abc` and `typing` (plus builtins and standard
  collections — `int`, `str`, `list`, `dict`, etc.).

This README mirrors the official 42 peer-evaluation scale for Python Module 05, so it
doubles as a "did I meet the grading bar" reference during defense.

## Exercises & Learning Objectives

### ex0 — `data_processor.py`
**What this exercise wants you to learn:** How to design a shared contract — an
abstract base class — that lets completely different data types be processed by the
same calling code. This is the core idea behind every plugin system and ORM you'll ever
use: define the shape of the behavior once, force every implementation to honor it, and
let the caller stop caring which concrete type it's holding.

**Concept:** Abstract Base Classes (ABC), `@abstractmethod`, polymorphic interfaces.
Defines a `DataProcessor` ABC with abstract `validate()` and `ingest()` methods, plus a
concrete `output()` method. Three concrete classes (`NumericProcessor`, `TextProcessor`,
`LogProcessor`) override `validate()`/`ingest()` to handle different data types while
sharing the same base interface. Demonstrates that you can't instantiate an abstract
class — only its concrete subclasses.

### ex1 — `data_stream.py`
**What this exercise wants you to learn:** How to write orchestration code that never
special-cases on type. `DataStream` doesn't ask "is this a `NumericProcessor`?" — it
asks every registered processor "can you handle this?" and lets each one answer for
itself. That single habit is what makes a system open to new data types later without
ever touching the code that routes them.

**Concept:** Polymorphic dispatch, runtime type routing.
The `DataStream` class registers multiple processors and routes incoming data to the
correct one automatically. The stream doesn't know what specific processors exist — it
just asks each one "can you handle this?" via `validate()`. This is polymorphism in
action: one interface, many behaviors.

### ex2 — `data_pipeline.py`
**What this exercise wants you to learn:** The difference between a nominal contract
(`ABC`, where a class must explicitly declare "I inherit this interface") and a
structural one (`Protocol`, where a class satisfies the interface just by having the
right method shape, no inheritance declared). Structural typing is what lets you bolt
new, unrelated classes onto a system without ever modifying it — the mechanism behind
the Open/Closed Principle.

**Concept:** `Protocol`-based plugin architecture, structural typing.
Extends the system with output plugins (exporters) defined through `Protocol` — a
duck-typing contract, as opposed to the nominal (inheritance-based) typing used by
`ABC` in ex0/ex1. Demonstrates how abstract interfaces enable extensibility: new export
formats can be added without modifying existing code (Open/Closed Principle).

## Evaluation Checklist

### Preliminaries
- [x] Only the requested files are present per exercise directory: `ex0/data_processor.py`,
  `ex1/data_stream.py`, `ex2/data_pipeline.py`. `ex0/__init__.py` and `ex1/__init__.py`
  are empty package-marker files (single docstring each), not exercise deliverables.
- [x] Project structure matches the subject's per-exercise `Directory:` / `Files to
  Submit:` layout (`ex0/`, `ex1/`, `ex2/`).
- [x] **Authorized imports.** The subject restricts imports to `abc` and `typing`
  (plus builtins) for all three exercises. All three files now import only from
  `__future__`, `abc`, and `typing` — no `os`/`sys`. `ex1/data_stream.py` and
  `ex2/data_pipeline.py` no longer import their predecessor exercise's module; each
  file inlines its own copy of the `DataProcessor` ABC and the three concrete
  processor classes (and, in `ex2`, also `DataStream`), so no `sys.path` patching is
  needed.
- [x] **Self-containment.** Each of `ex0/data_processor.py`, `ex1/data_stream.py`, and
  `ex2/data_pipeline.py` is now fully standalone and runnable in isolation — copying
  just the single file named in a given exercise's "Files to Submit" is sufficient;
  none of them depend on sibling `ex0`/`ex1` directories or `__init__.py` markers at
  runtime.

### Exercise 0 — Data Processor (`ex0/data_processor.py`)
- [x] File named `data_processor.py` exists.
- [x] Imports `ABC` and `abstractmethod` from `abc` (line 2).
- [x] `DataProcessor` inherits from `ABC` (line 6).
- [x] `@abstractmethod` decorates both `validate()` (line 11) and `ingest()` (line 15).
- [x] Signatures match the subject exactly on the base class:
  `validate(self, data: Any) -> bool` (line 12),
  `ingest(self, data: Any) -> None` (line 16),
  `output(self) -> Tuple[int, str]` (line 19, equivalent to `tuple[int, str]`).
- [x] `NumericProcessor`, `TextProcessor`, `LogProcessor` all inherit from
  `DataProcessor` and override both abstract methods with specialized signatures, as
  required ("the overriding `ingest` method signature must reflect the accepted
  types").
- [x] `NumericProcessor` validates/ingests `int`, `float`, and lists of both
  (mixed-type lists included).
- [x] `TextProcessor` validates/ingests `str` and lists of `str`.
- [x] `LogProcessor` validates/ingests a `dict[str, str]` and lists of that type
  (multiple log entries), formatting each as `"LEVEL: message"`.
- [x] Running `python3 data_processor.py` exercises valid/invalid detection per class,
  ingestion, string transformation, and FIFO `output()` (oldest item first, removed
  after extraction, via `self._storage.pop(0)`). Verified by running the script — exit
  code 0, output matches the subject's example transcript.
- [x] The demo calls `ingest('foo')` on `NumericProcessor` without prior validation and
  catches the resulting `ValueError` (lines 105–109). Per the subject, this specific
  call is expected to also produce "a `mypy` warning, on purpose"; no
  `# type: ignore` is applied here, so `mypy --disallow-untyped-defs
  --disallow-incomplete-defs` reports exactly one `arg-type` error on this line and
  the module is otherwise clean — that single warning is the intended, documented
  exception, not a bug.

### Exercise 1 — Polymorphic Processing of Data Streams (`ex1/data_stream.py`)
- [x] File named `data_stream.py` exists.
- [x] All ex0 behavior remains available and correct — the `DataProcessor` ABC and its
  three concrete subclasses are inlined into this file (per exercise instructions,
  "use your code from Exercise 0 and improve it"), so the file is self-contained and
  submittable on its own.
- [x] `DataStream` implements `register_processor()` and `process_stream()`.
- [x] Signatures match: `register_processor(self, proc: DataProcessor) -> None`
  (line 102), `process_stream(self, stream: list[Any]) -> None` (line 105, `Any`
  imported directly rather than referenced as `typing.Any` — equivalent), and
  `print_processors_stats(self) -> None` (line 120).
- [x] `process_stream()` calls `validate()` then `ingest()` on each registered
  processor polymorphically (lines 108–113), trying processors in registration order
  until one accepts the element.
- [x] Invalid/unhandled data in the stream is handled gracefully: unroutable elements
  print `"DataStream error - Can't process element in stream: ..."` (line 118) instead
  of raising, and a `validate()` exception is caught defensively (lines 114–116).
- [x] Statistics for all registered processors are displayed via `total_processed` and
  `remaining` properties defined on the base `DataProcessor` (lines 25–31) and
  read by `print_processors_stats()` (lines 118–123, within this file).

### Exercise 2 — Data Pipeline (`ex2/data_pipeline.py`)
- [x] File named `data_pipeline.py` exists.
- [x] Builds on ex1: the `DataProcessor` hierarchy and `DataStream` class are inlined
  into this file (per exercise instructions, "use your code from Exercise 1 and
  improve it"), and `DataPipeline(DataStream)` subclasses the stream class rather than
  redefining it, adding the export behavior on top of the existing `register_processor`
  / `process_stream` / `print_processors_stats` methods. The file is fully
  self-contained and submittable on its own.
- [x] `ExportPlugin` is defined and inherits from `Protocol` (line 133).
- [x] `ExportPlugin.process_output` matches the required signature:
  `process_output(self, data: List[Tuple[int, str]]) -> None` (line 134, equivalent to
  `list[tuple[int, str]]`).
- [x] Two independent classes conform to the `ExportPlugin` protocol structurally
  (duck typing, no explicit inheritance): `CSVPlugin` (line 152) and `JSONPlugin`
  (line 160), each implementing `process_output` with a matching signature.
- [x] `output_pipeline(self, nb: int, plugin: ExportPlugin) -> None` (line 139) is
  implemented and matches the required signature exactly; it pulls up to `nb` items
  from every registered processor via `output()` (stopping early on `IndexError`) and
  hands them to the plugin. Note: the subject phrases this as "the `DataStream` class
  will now implement `output_pipeline`" — here it is added on the `DataPipeline`
  subclass instead of on `DataStream` itself. Since `DataPipeline` *is* a `DataStream`
  and inherits everything from it, this still satisfies the intent (extend the stream
  class with export behavior) and is arguably the more idiomatic use of inheritance,
  but it is worth calling out as an interpretation rather than a literal same-class
  edit.
- [x] Running `python3 data_pipeline.py` demonstrates both a CSV export and a JSON
  export against real ingested data, with statistics shown before/after each export —
  verified by running the script (exit code 0).
- [x] **`JSONPlugin` key numbering matches the subject's transcript exactly.** The
  subject's example shows JSON keys like `"item_3"`..`"item_7"` for the numeric
  plugin call and `"item_2"`/`"item_3"` for the log plugin call — i.e. the key is
  built from the actual processing rank returned by `DataProcessor.output()` (the
  tuple's first element), not a position index freshly starting at 1 for each
  `output_pipeline()` call. `JSONPlugin.process_output` (line ~163) was fixed to
  build `mapping = {f'item_{rank}': v for rank, v in data}` directly from the
  `(rank, value)` tuples instead of `enumerate(data)`; the previous positional
  version produced `item_1`..`item_5` every time, which diverged from the subject's
  example transcript. Re-verified against the subject's exact sample numbers by
  tracing ingestion order and re-running the script.

### Code Quality and Understanding (applies to the whole module)
- [x] Targets Python 3.10+ syntax: PEP 604 unions (`int | float`, `str | list[str]`)
  and lowercase generics (`list[...]`, `dict[str, str]`) are used throughout, guarded
  by `from __future__ import annotations` so annotations are also safe on slightly
  older interpreters. Verified running under Python 3.12.2.
- [x] `flake8 --max-line-length=99` (no ignores) is clean on all three files —
  verified with flake8 7.3.0. No trailing whitespace, no tabs, all three files end
  with a newline.
- [x] Type annotations are present on effectively every function, method, and
  parameter across all three files, including return types (`-> bool`, `-> None`,
  `-> Tuple[int, str]`, etc.), verified with `mypy --disallow-untyped-defs
  --disallow-incomplete-defs` (mypy 2.3.1). The one deliberate exception, called out
  by the grading sheet itself ("note that there is an exception on Ex0"), is the
  intentionally mistyped `np.ingest('foo')` demo call in `ex0/data_processor.py`
  (line 107): mypy reports exactly one `arg-type` error there and nothing else across
  all three files, matching the subject's expectation that this specific call "will
  leave you with a mypy warning, on purpose."
- [x] Docstrings are correctly omitted from the exercise files (not required for this
  module); the only docstrings in the module are the one-line package-marker
  docstrings in `ex0/__init__.py` and `ex1/__init__.py`.
- [x] `ABC` / `@abstractmethod` are used correctly in ex0 to force every concrete
  processor to implement `validate()` and `ingest()`.
- [x] `Protocol` is used correctly in ex2: `ExportPlugin` is a structural contract, and
  `CSVPlugin`/`JSONPlugin` satisfy it without inheriting from it, which is the point of
  duck typing versus `ABC`'s nominal inheritance.
- [x] Error handling is present at every ingestion/consumption boundary: `ingest()`
  raises `ValueError` on invalid data (all three processors, ex0), `output()` raises
  `IndexError` when storage is empty (ex0, line 21), and `DataStream.process_stream()`
  catches per-element failures instead of letting one bad element crash the whole
  batch (ex1, lines 26–28).

The eval sheet's "Understanding" section additionally asks the evaluator to confirm,
live, that the learner can explain ABCs, polymorphism, and `@abstractmethod` in their
own words — see the **Defense Prep** section below for the exact questions and talking
points.

## Defense Prep — Questions From the Evaluation Sheet

These are the verbal/live-demo checks from the eval sheet — not something a README
checkbox can satisfy on its own. Rehearse them before the defense.

### Exercise 0

*"Why are abstract base classes useful?"*
- `DataProcessor` defines a shared contract (`validate`/`ingest`/`output`) while
  forcing every concrete subclass to supply its own behavior.
- You can't instantiate `DataProcessor` directly, which prevents "half-built"
  processors from existing.
- `@abstractmethod` is what enforces this at class-definition time, not just by
  convention.

### Exercise 1

*"How does polymorphism enable `DataStream` to handle different data types in the
stream without knowing their specific implementations? What are the benefits of this
design approach?"* (eval sheet + subject's own "Think About" prompt)
- `process_stream()` never checks `isinstance` against a specific processor type; it
  just calls `validate()`/`ingest()` on whatever processors are registered and lets
  each one decide for itself whether it can handle the element.
- Adding a new data type later means writing one new `DataProcessor` subclass and
  registering it — zero changes to `DataStream` itself.

### Exercise 2

*"Explain the difference between `Protocol` (duck typing) and `ABC` (abstract base
classes)."*
- `ABC` requires explicit, nominal inheritance (`class CSVPlugin(ABC)`) and blocks
  instantiation until every `@abstractmethod` is overridden.
- `Protocol` is structural — `CSVPlugin`/`JSONPlugin` satisfy `ExportPlugin` just by
  having a matching `process_output` method, with no `class CSVPlugin(ExportPlugin)`
  inheritance line at all.
- Use `ABC` when you own the whole class hierarchy and want to force a contract; use
  `Protocol` when you want unrelated/third-party classes to plug in without modifying
  them.

### Code Quality and Understanding

The eval sheet's "Understanding" section asks the evaluator to confirm, live, that the
learner:

- *Can explain what abstract base classes (ABC) are and why they're useful* — see
  Exercise 0 above.
- *Understands when and why to use polymorphism* — see Exercise 1 above.
- *Can demonstrate how the same interface works with different implementations* — e.g.
  call `describe()`/`attack()` on any registered `DataProcessor` (or, in the ex1/ex2
  analogy, any `Creature`-style object) without special-casing per subclass.
- *Understands that `@abstractmethod` forces subclasses to implement specific
  methods* — try instantiating `DataProcessor()` directly in a live REPL to show it
  raises `TypeError: Can't instantiate abstract class DataProcessor...`.

## Key Takeaways

- **Abstract classes** define contracts that subclasses must fulfill.
- **Polymorphism** lets you write code that works with any object implementing an interface.
- **Method overriding** lets each subclass provide specialized behavior.
- The `validate()`/`ingest()` pattern separates "can I?" from "do it" — defensive design.
- **`Protocol`** gives you structural (duck-typed) contracts, as an alternative to
  `ABC`'s nominal (inheritance-based) contracts — useful when you don't own the classes
  that should conform to an interface.
- Plugin architectures make systems extensible without modification.
- Keep an eye on the subject's "Authorized imports" list even when it's tempting to
  reorganize a personal repo for convenience (e.g. `sys.path` tricks to share code
  between exercise folders) — each exercise file here is self-contained instead,
  copying forward the prior exercise's code per the subject's "use your code from
  Exercise N and improve it" instruction.
- These patterns are the foundation of framework design and large-scale systems.
