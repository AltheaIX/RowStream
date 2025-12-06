from dataset.repository.mock_repository import MockDatasetRepository


def test_read_csv_offset_mock():
    repo = MockDatasetRepository()
    rows = repo.read_csv(0,10)

    assert rows[0].id == 1