from typing import List

from dataset.model.row import Row


class MockDatasetRepository:
    def __init__(self):
        self.rows: List[Row] = [
            Row(1, "Budi", 21, "Laki-laki", 85, "Kimia", "9/8/2023", 90, 80),
            Row(2, "Ani", 20, "Perempuan", 77.5, "Math", "10/8/2023", 75, 80)
        ]

    def get_all_rows(self) -> List[Row]:
        return self.rows

    def read_csv(self, offset: int = 0, limit: int = 10) -> List[Row]:
        return self.rows