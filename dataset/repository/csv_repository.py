import csv
import os
import struct
from functools import lru_cache

from dataset.model.row import Row
from .repository import CSVDatasetRepository


def csv_methods():
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
            csvfile.readline()

            while True:
                pos = csvfile.tell()
                line = csvfile.readline()
                if not line:
                    break

                indexing.append(pos)

        return indexing

    @lru_cache(maxsize=1)
    def count_rows(self) -> int:
        with open(self.file_path, "r") as f:
            return sum(1 for _ in f) - 1  # minus 1 for header

    def append_csv(self, row: Row):
        with open(self.file_path, "a") as f:
            offset = f.tell()
            line = f"{row.id},{row.nama},{row.umur},{row.gender},{row.nilai},{row.matkul},{row.tanggal},{row.uts},{row.uas}\n"
            f.write(line)

        with open(self.index_file_path, "ab") as idx:
            idx.write(struct.pack("<Q", offset))

        self.index.append(offset)
        self.count_rows.cache_clear()

    def update_csv(self, index_to_update: int, row: Row):
        tmp = self.file_path + ".tmp"
        need_reindexing = False

        with open(self.file_path, "r", newline="") as src, open(tmp, "w", newline="") as dst:
            for i, line in enumerate(src):
                if i == index_to_update:
                    new_data = f"{row.id},{row.nama},{row.umur},{row.gender},{row.nilai},{row.matkul},{row.tanggal},{row.uts},{row.uas}\n"

                    if len(line) != len(new_data):
                        need_reindexing = True

                    dst.write(new_data)
                    continue

                dst.write(line)

        os.replace(tmp, self.file_path)

        if need_reindexing:
            new_index = self.read_csv_indexing()
            self.index = new_index
            self.save_index(new_index)


    def delete_csv(self, index_to_delete: int):
        tmp = self.file_path + ".tmp"

        with open(self.file_path, "r", newline="") as src, open(tmp, "w", newline="") as dst:
            for i, line in enumerate(src):
                if i != index_to_delete:
                    dst.write(line)

        os.replace(tmp, self.file_path)

        new_index = self.read_csv_indexing()
        self.index = new_index
        self.save_index(new_index)
        self.count_rows.cache_clear()

    CSVDatasetRepository.get_all_rows = get_all_rows
    CSVDatasetRepository.read_csv = read_csv
    CSVDatasetRepository.read_csv_with_seek = read_csv_with_seek
    CSVDatasetRepository.read_csv_indexing = read_csv_indexing
    CSVDatasetRepository.count_rows = count_rows
    CSVDatasetRepository.append_csv = append_csv
    CSVDatasetRepository.update_csv = update_csv
    CSVDatasetRepository.delete_csv = delete_csv
