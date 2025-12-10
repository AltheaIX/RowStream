import unittest

from dataset.model.row import Row
from dataset.repository.csv_repository import CSVDatasetRepository
from dataset.service import CSVDatasetService


class TestClass(unittest.TestCase):
    def test_create_row(self):
        repo = CSVDatasetRepository("../../dataset.csv")
        service = CSVDatasetService(repo)

        service.create_row()