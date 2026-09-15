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


if __name__ == "__main__":
    print('=== Code Nexus - Data Processor ===')
    # Numeric Processor tests
    print('Testing Numeric Processor...')
    np = NumericProcessor()
    print("Trying to validate input '42':", np.validate(42))
    print("Trying to validate input 'Hello':", np.validate('Hello'))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest('foo')  # intentional bad type demo: mypy warning expected here
    except Exception as e:
        print('Got exception:', e)
    print('Processing data: [1, 2, 3, 4, 5]')
    np.ingest([1, 2, 3, 4, 5])
    print('Extracting 3 values...')
    for i in range(3):
        rank, val = np.output()
        print(f'Numeric value {i}: {val}')

    # Text Processor tests
    print('Testing Text Processor...')
    tp = TextProcessor()
    print("Trying to validate input '42':", tp.validate(42))
    tp.ingest(['Hello', 'Nexus', 'World'])
    print('Extracting 1 value...')
    r, v = tp.output()
    print(f'Text value 0: {v}')

    # Log Processor tests
    print('Testing Log Processor...')
    lp = LogProcessor()
    print("Trying to validate input 'Hello':", lp.validate('Hello'))
    lp.ingest([{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
               {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    print('Extracting 2 values...')
    for i in range(2):
        rank, v = lp.output()
        print(f'Log entry {i}: {v}')
