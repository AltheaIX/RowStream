from dataset.repository.csv_repository import CSVDatasetRepository
from dataset.service.pagination_service import CSVPaginationService


def test_read_csv_pagination():
    repo = CSVDatasetRepository("tests/dataset.csv")
    service = CSVPaginationService(repo)

    rows = service.get_page(0, 2)

    assert len(rows) == 2