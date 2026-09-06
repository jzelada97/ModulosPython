# Module 05 — Code Nexus: Polymorphic Data Streams

## Overview

This module teaches abstract classes, polymorphism, and method overriding through a
data processing pipeline architecture. The key insight: different data types can be
processed through a single interface without the caller knowing (or caring) about the
specific implementation.

## Exercises & Learning Objectives

### ex0 — `data_processor.py`
**Concept:** Abstract Base Classes (ABC), `@abstractmethod`, polymorphic interfaces.
Defines a `DataProcessor` ABC with abstract `validate()` and `ingest()` methods.
Three concrete classes (`NumericProcessor`, `TextProcessor`, `LogProcessor`) override
these methods to handle different data types. Demonstrates that you can't instantiate
an abstract class — only its concrete subclasses.

### ex1 — `data_stream.py`
**Concept:** Polymorphic dispatch, runtime type routing.
The `DataStream` class registers multiple processors and routes incoming data to the
correct one automatically. The stream doesn't know what specific processors exist — it
just asks each one "can you handle this?" via `validate()`. This is polymorphism in
action: one interface, many behaviors.

### ex2 — `data_pipeline.py`
**Concept:** Plugin architecture, complete pipeline design.
Extends the system with output plugins (exporters). Demonstrates how abstract
interfaces enable extensibility — new data types or output formats can be added without
modifying existing code. This is the Open/Closed Principle in practice.

## Key Takeaways

- **Abstract classes** define contracts that subclasses must fulfill.
- **Polymorphism** lets you write code that works with any object implementing an interface.
- **Method overriding** lets each subclass provide specialized behavior.
- The `validate()`/`ingest()` pattern separates "can I?" from "do it" — defensive design.
- Plugin architectures make systems extensible without modification.
- These patterns are the foundation of framework design and large-scale systems.
