from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List, Protocol, Tuple


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._total_processed: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> Tuple[int, str]:
        if not self._storage:
            raise IndexError('No data available')
        rank, item = self._storage.pop(0)
        return rank, item

    @property
    def total_processed(self) -> int:
        return self._total_processed

    @property
    def remaining(self) -> int:
        return len(self._storage)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError('Improper numeric data')
        if isinstance(data, (int, float)):
            items = [data]
        else:
            items = list(data)
        for it in items:
            self._storage.append((self._total_processed, str(it)))
            self._total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError('Improper text data')
        items = [data] if isinstance(data, str) else list(data)
        for it in items:
            self._storage.append((self._total_processed, str(it)))
            self._total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def valid_log(d: Any) -> bool:
            if not isinstance(d, dict):
                return False
            return all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())

        if isinstance(data, dict):
            return valid_log(data)
        if isinstance(data, list):
            return all(valid_log(x) for x in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError('Improper log data')
        items = [data] if isinstance(data, dict) else list(data)
        for it in items:
            # Convert to readable string like 'LEVEL: message'
            # if keys are 'log_level' and 'log_message' join them
            level = it.get('log_level', 'INFO')
            msg = it.get('log_message', '')
            text = f"{level}: {msg}"
            self._storage.append((self._total_processed, text))
            self._total_processed += 1


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
        # Build a simple JSON-like string mapping item_<rank> -> value, using
        # the processing rank returned by DataProcessor.output() (not the
        # position within this batch), matching the subject's example.
        mapping = {f'item_{rank}': v for rank, v in data}
        items = ', '.join(f'"{k}": "{v}"' for k, v in mapping.items())
        print('JSON Output:')
        print('{' + items + '}')


if __name__ == "__main__":
    print('=== Code Nexus - Data Pipeline ===')
    dp = DataPipeline()
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
