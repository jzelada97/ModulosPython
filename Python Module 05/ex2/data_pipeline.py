from __future__ import annotations
import os
import sys
# Ensure module root is on sys.path so sibling packages like ex1/ex0 are importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from typing import List, Protocol, Tuple
from ex1.data_stream import DataStream


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class DataPipeline(DataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        # Collect nb elements from each registered processor and send to plugin
        for proc in list(getattr(self, '_processors', [])):
            collected: List[Tuple[int, str]] = []
            for _ in range(nb):
                try:
                    collected.append(proc.output())
                except IndexError:
                    break
            if collected:
                plugin.process_output(collected)


class CSVPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        # For simplicity join values with commas
        values = [v for _, v in data]
        print('CSV Output:')
        print(','.join(values))


class JSONPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        # Build a simple JSON-like string mapping item_N -> value
        mapping = {f'item_{i + 1}': v for i, (_, v) in enumerate(data)}
        items = ', '.join(f'"{k}": "{v}"' for k, v in mapping.items())
        print('JSON Output:')
        print('{' + items + '}')


if __name__ == "__main__":
    print('=== Code Nexus - Data Pipeline ===')
    dp = DataPipeline()
    from ex0.data_processor import NumericProcessor, TextProcessor, LogProcessor
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    print('Initialize Data Stream...')
    dp.print_processors_stats()
    print('Registering Processors')
    dp.register_processor(np)
    dp.register_processor(tp)
    dp.register_processor(lp)
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
    dp.process_stream(batch)
    dp.print_processors_stats()
    print('Send 3 processed data from each processor to a CSV plugin:')
    csv = CSVPlugin()
    dp.output_pipeline(3, csv)
    dp.print_processors_stats()
    print('Send another batch of data: numeric, texts, logs, numbers, single string')
    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'},
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello',
    ]
    dp.process_stream(batch2)
    dp.print_processors_stats()
    print('Send 5 processed data from each processor to a JSON plugin:')
    jsonp = JSONPlugin()
    dp.output_pipeline(5, jsonp)
    dp.print_processors_stats()
