from dataset.model.row import Row
from .service import CSVDatasetService


def create_methods():
    def create_row(self, data: dict):
        row = Row(
            id=data["id"],
            nama=data["nama"],
            umur=int(data["umur"]),
            gender=data["gender"],
            nilai=float(data["nilai"]),
            matkul=data["matkul"],
            tanggal=data["tanggal"],
            uts=float(data["uts"]),
            uas=float(data["uas"])
        )
        return self.repository.append_csv(row)

    CSVDatasetService.create_row = create_row
