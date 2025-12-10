
class CSVDatasetRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.index_file_path = "index.idx"
        self.index: list[int] = []

        self.load_index()