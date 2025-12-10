import unittest

from dataset.repository import CSVDatasetRepository
from dataset.service import CSVDatasetService


class TestClass(unittest.TestCase):
    def test_update_row(self):
        repo = CSVDatasetRepository("../../dataset.csv")
        service = CSVDatasetService(repo)

        partial_update_data = {
            'nama': 'Test_Partial_Update',
            'gender': 'Gender_Partial',
            'nilai': 90
        }

        service.update_row(1, partial_update_data)