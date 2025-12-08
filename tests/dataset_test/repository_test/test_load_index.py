import unittest

from dataset.repository.csv_repository import CSVDatasetRepository


class TestClass(unittest.TestCase):
    def test_load_index(self):
        repo = CSVDatasetRepository('../../dataset.csv')
        offsets = repo.load_index()
        print(offsets)