from __future__ import annotations
import os
import sys
# Ensure module root is on sys.path so sibling packages like ex0 are importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import Any, List
from ex0.data_processor import DataProcessor


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for elem in stream:
            handled = False
            for proc in self._processors:
                try:
                    if proc.validate(elem):
                        proc.ingest(elem)
                        handled = True
                        break
                except Exception:
                    # Validation should be safe; ignore and continue
                    continue
            if not handled:
                print(f"DataStream error - Can't process element in stream: {elem}")

    def print_processors_stats(self) -> None:
        print('== DataStream statistics ==')
        if not self._processors:
            print('No processor found, no data')
            return
        for proc in self._processors:
            name = proc.__class__.__name__
            print(
                f"{name}: total {proc.total_processed} items processed, "
                f"remaining {proc.remaining} on processor"
            )


if __name__ == "__main__":
    print('=== Code Nexus - Data Stream ===')
    ds = DataStream()
    print('Initialize Data Stream...')
    ds.print_processors_stats()
    print('Registering Numeric Processor')
    from ex0.data_processor import NumericProcessor, TextProcessor, LogProcessor
    np = NumericProcessor()
    ds.register_processor(np)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'},
        ],
        42,
        ['Hi', 'five'],
    ]
    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    ds.print_processors_stats()
    print('Registering other data processors')
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(tp)
    ds.register_processor(lp)
    print('Send the same batch again')
    ds.process_stream(batch)
    ds.print_processors_stats()
    print('Consume some elements from the data processors: Numeric 3, Text 2, Log 1')
    for i in range(3):
        try:
            print(np.output())
        except Exception:
            break
    for i in range(2):
        try:
            print(tp.output())
        except Exception:
            break
    try:
        print(lp.output())
    except Exception:
        pass
    ds.print_processors_stats()
