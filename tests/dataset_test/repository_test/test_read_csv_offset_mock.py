import unittest

from dataset.repository.mock_repository import MockDatasetRepository


class TestClass(unittest.TestCase):
    def test_read_csv_offset_mock(self):
        repo = MockDatasetRepository()
        rows = repo.read_csv(0,10)

        assert rows[0].id == 1