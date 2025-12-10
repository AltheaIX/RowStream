import os
import struct

from .repository import CSVDatasetRepository


def index_methods():
    def save_index(self, index: list[int]):
        with open(self.index_file_path, "wb") as f:
            for offset in index:
                f.write(struct.pack("<Q", offset))

    def load_index(self):
        if not os.path.exists(self.index_file_path):
            index = self.read_csv_indexing()
            self.index = index
            self.save_index(index)
            return index

        with open(self.index_file_path, "rb") as f:
            data = f.read()

        self.index = [offset for (offset,) in struct.iter_unpack("<Q", data)]
        return self.index

    CSVDatasetRepository.save_index = save_index
    CSVDatasetRepository.load_index = load_index
