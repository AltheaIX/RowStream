import math

from dataset.repository import dataset_repository


class CSVPaginationService:
    def __init__(self, repository: dataset_repository):
        self.repository = repository

    def get_page(self, page_number: int, page_size: int):
        if page_number < 0:
            raise ValueError("page_number cannot be negative")
        if page_size < 1:
            raise ValueError("page_size must be higher than 0")

        offset = page_number * page_size

        return self.repository.read_csv(offset, page_size)

    def get_total_pages(self, page_size: int):
        total = self.repository.count_rows()
        return math.ceil(total / page_size)