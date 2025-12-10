from dataset.service.operation_service import operation_methods
from dataset.service.pagination_service import pagination_methods
from dataset.service.service import CSVDatasetService

pagination_methods()
operation_methods()

__all__ = ["CSVDatasetService"]