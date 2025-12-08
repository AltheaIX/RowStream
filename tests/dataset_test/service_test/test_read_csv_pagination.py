import unittest

from dataset.repository.csv_repository import CSVDatasetRepository
from dataset.service.pagination_service import CSVPaginationService


class TestClass(unittest.TestCase):
    def test_read_csv_pagination(self):
        repo = CSVDatasetRepository("../../dataset.csv")
        service = CSVPaginationService(repo)

        rows = service.get_page(0, 2)

        assert len(rows) == 2