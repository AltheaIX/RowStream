from dataset.repository.csv_repository import CSVDatasetRepository


def test_read_csv_count_rows():
    repo = CSVDatasetRepository("dataset_full.csv")
    total_count = repo.count_rows()
    print(total_count)