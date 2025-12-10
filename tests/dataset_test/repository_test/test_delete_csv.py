import unittest

from dataset.repository import CSVDatasetRepository
from dataset.service import CSVDatasetService


class TestClass(unittest.TestCase):
    def test_delete_csv(self):
        repo = CSVDatasetRepository('../../dataset.csv')
        repo.delete_csv(4)