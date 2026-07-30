Exercise 1 — Polymorphic Processing of a Data Stream

File: `data_stream.py`

Spec summary:
- Implement `DataStream` with `register_processor`, `process_stream`, and `print_processors_stats`.
- Route each stream element to the appropriate registered `DataProcessor` using `validate`.
- Demonstrate errors when no processor can handle an element and show processor statistics.

Run `python data_stream.py` to execute the test scenario.
