import unittest

from dataset.repository.mock_repository import MockDatasetRepository


class TestClass(unittest.TestCase):
    def test_read_csv_mock(test):
        repo = MockDatasetRepository()
        rows = repo.get_all_rows()

        assert rows[0].nama == "Budi"
        assert rows[0].nilai == 85
        assert rows[1].nama == "Ani"
        assert rows[1].nilai == 77.5
