import math

from .service import CSVDatasetService


def pagination_methods():
    def get_page(self, page_number: int, page_size: int):
        if page_number < 0:
            raise ValueError("page_number cannot be negative")
        if page_size < 1:
            raise ValueError("page_size must be higher than 0")

        start = page_number * page_size

        if start >= len(self.repository.index):
            return []

        offset = self.repository.index[start]

        return self.repository.read_csv_with_seek(offset, page_size)

    def get_total_pages(self, page_size: int):
        total = self.repository.count_rows()
        return math.ceil(total / page_size)

    CSVDatasetService.get_page = get_page
    CSVDatasetService.get_total_pages = get_total_pages
