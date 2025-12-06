from dataset.repository.csv_repository import CSVDatasetRepository


def test_read_csv():
    repo = CSVDatasetRepository("tests/dataset.csv")
    rows = repo.get_all_rows()
    assert len(rows) > 0
