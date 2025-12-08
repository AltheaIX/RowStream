import unittest

from dataset.repository.csv_repository import CSVDatasetRepository


class TestClass(unittest.TestCase):
    def test_read_csv(self):
        repo = CSVDatasetRepository("../../dataset.csv")
        rows = repo.get_all_rows()
        assert len(rows) > 0
