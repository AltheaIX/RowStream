from abc import ABC, abstractmethod
from typing import List

from dataset.model.row import Row


class DatasetRepository(ABC):
    @abstractmethod
    def get_all_rows(self) -> list[Row]:
        pass

    @abstractmethod
    def read_csv(self, offset: int = 0, limit: int = 10) -> list[Row]:
        pass

    @abstractmethod
    def read_csv_with_seek(self, seek: int, limit: int = 10) -> list[Row]:
        pass

    @abstractmethod
    def read_csv_indexing(self) -> list[int]:
        pass

    @abstractmethod
    def save_index(self, index: list[int]):
        pass

    @abstractmethod
    def load_index(self):
        pass

    @abstractmethod
    def count_rows(self) -> int:
        pass