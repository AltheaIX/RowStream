import struct
import unittest

from dataset.repository.csv_repository import CSVDatasetRepository


class TestCase(unittest.TestCase):
    def test_save_index(self):
        repo = CSVDatasetRepository('../../dataset.csv')

        repo.save_index([1,2,3,4,5,6])