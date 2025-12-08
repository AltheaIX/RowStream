import csv
import os
import struct
from functools import lru_cache

from dataset.model.row import Row
from dataset.repository.dataset_repository import DatasetRepository


class CSVDatasetRepository(DatasetRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.index_file_path = "index.idx"
        self.index: list[int] = []

        self.load_index()

    def get_all_rows(self) -> list[Row]:
        rows = []
        with open(self.file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for r in reader:
                row = Row(
                    id=int(r["ID"]),
                    nama=r["Nama"],
                    umur=int(r["Umur"]),
                    gender=r["Gender"],
                    nilai=float(r["Nilai"]),
                    matkul=r["Matkul"],
                    tanggal=r["Tanggal"],
                    uts=float(r["UTS"]),
                    uas=float(r["UAS"])
                )
                rows.append(row)

        return rows

    def read_csv(self, offset: int = 0, limit: int = 10) -> list[Row]:
        rows = []
        with open(self.file_path) as csvfile:
            reader = csv.DictReader(csvfile)

            for _ in range(offset):
                next(reader)

            for i, r in enumerate(reader):
                if i > limit - 1:
                    break

                row = Row(
                    id=int(r["ID"]),
                    nama=r["Nama"],
                    umur=int(r["Umur"]),
                    gender=r["Gender"],
                    nilai=float(r["Nilai"]),
                    matkul=r["Matkul"],
                    tanggal=r["Tanggal"],
                    uts=float(r["UTS"]),
                    uas=float(r["UAS"])
                )
                rows.append(row)

        return rows

    def read_csv_with_seek(self, seek: int, limit: int = 10) -> list[Row]:
        rows = []
        with open(self.file_path) as csvfile:
            header = csvfile.readline()
            headerArray = header.strip().split(',')

            csvfile.seek(seek)
            reader = csv.DictReader(csvfile, headerArray)
            for i, r in enumerate(reader):
                if i > limit - 1:
                    break

                row = Row(
                    id=int(r["ID"]),
                    nama=r["Nama"],
                    umur=int(r["Umur"]),
                    gender=r["Gender"],
                    nilai=float(r["Nilai"]),
                    matkul=r["Matkul"],
                    tanggal=r["Tanggal"],
                    uts=float(r["UTS"]),
                    uas=float(r["UAS"])
                )

                rows.append(row)

        return rows

    def read_csv_indexing(self) -> list[int]:
        indexing = []
        with open(self.file_path, 'r') as csvfile:
            csvfile.readline() # for skipping header
            indexing.append(csvfile.tell())

            while True:
                pos = csvfile.tell()
                line = csvfile.readline()
                if not line:
                    break

                indexing.append(pos)

        return indexing

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


    @lru_cache(maxsize=1)
    def count_rows(self) -> int:
        with open(self.file_path, "r") as f:
            return sum(1 for _ in f) - 1 # minus 1 for header