from dataset.model.row import Row
from .service import CSVDatasetService


def operation_methods():
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

    def update_row(self, row_index: int, partial_data: dict):
        offset = self.repository.index[row_index-1]
        old_row = self.repository.read_csv_with_seek(offset, 1)[0]

        uts = partial_data.get('uts') or float(old_row.uts)
        uas = partial_data.get('uas') or float(old_row.uas)

        merged = {
            'id': old_row.id,
            'nama': partial_data.get('nama') or old_row.nama,
            'umur': partial_data.get('umur') or int(old_row.umur),
            'gender': partial_data.get('gender') or old_row.gender,
            'nilai': float(uts + uas) / 2,
            'matkul': partial_data.get('matkul') or old_row.matkul,
            'tanggal': partial_data.get('tanggal') or old_row.tanggal,
            'uts': partial_data.get('uts') or float(old_row.uts),
            'uas': partial_data.get('uas') or float(old_row.uas),
        }

        new_row = Row(**merged)

        return self.repository.update_csv(row_index, new_row)

    def delete_row(self, index: int):
        return self.repository.delete_csv(index)

    CSVDatasetService.create_row = create_row
    CSVDatasetService.update_row = update_row
    CSVDatasetService.delete_row = delete_row
