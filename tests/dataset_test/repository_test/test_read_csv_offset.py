import unittest

from dataset.repository.csv_repository import CSVDatasetRepository


class TestClass(unittest.TestCase):
    def test_read_csv_offset(self):
        offset = 1
        limit = 10

        repo = CSVDatasetRepository("../../dataset.csv")
        rows = repo.read_csv(offset, limit)

        assert rows[0].id == 2
