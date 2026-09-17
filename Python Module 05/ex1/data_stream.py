from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List, Tuple


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
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in d.items()
            )

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
                print(
                    "DataStream error - Can't process element in "
                    f"stream: {elem}"
                )

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
    np = NumericProcessor()
    ds.register_processor(np)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead',
            },
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
    print(
        'Consume some elements from the data processors: '
        'Numeric 3, Text 2, Log 1'
    )
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
