import unittest

from dataset.model.row import Row
from dataset.repository import CSVDatasetRepository


class TestClass(unittest.TestCase):
    def test_update_csv(self):
        repo = CSVDatasetRepository("../../dataset.csv")
        row = Row(
            id="1",
            nama="Asd",
            umur=1000,
            gender="Test Update",
            nilai=10,
            matkul="Test Update",
            tanggal="0000/00/00",
            uts=10,
            uas=10,
        )

        repo.update_csv(1, row)