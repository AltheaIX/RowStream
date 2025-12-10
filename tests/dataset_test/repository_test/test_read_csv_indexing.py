import unittest

from dataset.repository.csv_repository import CSVDatasetRepository


class TestSet(unittest.TestCase):
    def test_read_csv_indexing(self):
        repo = CSVDatasetRepository('../../dataset.csv')
        indexing = repo.read_csv_indexing()
        print(indexing, len(indexing))