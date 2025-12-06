import csv
from typing import List

from dataset.model.row import Row
from dataset.repository.dataset_repository import DatasetRepository


class CSVDatasetRepository(DatasetRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_all_rows(self) -> List[Row]:
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

    def read_csv(self, offset: int = 0, limit: int = 10) -> List[Row]:
        rows = []
        with open("tests/dataset.csv") as csvfile:
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
