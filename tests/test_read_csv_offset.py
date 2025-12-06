import csv

from dataset.model.row import Row
from dataset.repository.csv_repository import CSVDatasetRepository


def test_read_csv_offset():
    offset = 1
    limit = 10

    repo = CSVDatasetRepository("tests/dataset.csv")
    rows = repo.read_csv(offset, limit)

    print(rows)
    assert rows[0].id == 2
