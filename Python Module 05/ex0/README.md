Exercise 0 — Data Processor

File: `data_processor.py`

Spec summary:
- Implement an abstract `DataProcessor` class with abstract `validate` and `ingest` methods and a concrete `output` method.
- Provide `NumericProcessor`, `TextProcessor`, and `LogProcessor` with specific `ingest` signatures.
- Store ingested data as strings and track processing rank. `output()` returns `(rank, data)` and removes the item.

Run `python data_processor.py` to exercise validations, ingestion and outputs.
