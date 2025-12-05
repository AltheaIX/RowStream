from dataset.repository.mock_repository import MockDatasetRepository


def test_read_csv_mock():
    repo = MockDatasetRepository()
    rows = repo.get_all_rows()

    assert rows[0].nama == "Budi"
    assert rows[0].nilai == 85
    assert rows[1].nama == "Ani"
    assert rows[1].nilai == 77.5
