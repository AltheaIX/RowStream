from dataset.repository.csv_repository import csv_methods
from dataset.repository.indexing_repository import index_methods
from dataset.repository.repository import CSVDatasetRepository

index_methods()
csv_methods()

__all__ = ["CSVDatasetRepository"]