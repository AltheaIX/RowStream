from time import perf_counter

from dataset.repository.csv_repository import CSVDatasetRepository


def test_read_csv_count_rows_cached():
    repo = CSVDatasetRepository("dataset_full.csv")

    start = perf_counter()
    repo.count_rows()
    t1 = perf_counter() - start

    start = perf_counter()
    repo.count_rows()
    t2 = perf_counter() - start

    assert t2 < t1