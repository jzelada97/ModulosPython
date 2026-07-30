Exercise 2 — Data Pipeline

File: `data_pipeline.py`

Spec summary:
- Implement `ExportPlugin` protocol with `process_output(data: list[tuple[int,str]])`.
- Extend the `DataStream` with `output_pipeline(nb, plugin)` to export nb items per processor.
- Provide a CSV plugin and a JSON plugin (no external imports required).

Run `python data_pipeline.py` to see the pipeline in action.
