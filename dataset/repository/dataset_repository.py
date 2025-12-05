from abc import ABC, abstractmethod
from typing import List

from dataset.model.row import Row


class DatasetRepository(ABC):
    @abstractmethod
    def get_all_rows(self) -> List[Row]:
        pass
