import unittest

from dataset.repository.csv_repository import CSVDatasetRepository


class TestClass(unittest.TestCase):
    def test_read_csv_count_rows(self):
        repo = CSVDatasetRepository("../../../dataset_full.csv")
        total_count = repo.count_rows()
        print(total_count)