import unittest

from dataset.repository.csv_repository import CSVDatasetRepository


class TestSet(unittest.TestCase):
    def test_read_csv_with_seek(self):
        repo = CSVDatasetRepository('../../dataset.csv')
        rows = repo.read_csv_with_seek(95)

        assert rows[0].id == 2