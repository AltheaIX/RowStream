from dataset.model.row import Row


def test_row_creation():
    row = Row(
        id=1,
        nama="Budi",
        umur=21,
        gender="Laki-laki",
        nilai=85,
        matkul="Kimia",
        tanggal="9/8/2023",
        uts=90,
        uas=80,
    )

    assert row.id == 1
    assert row.nama == "Budi"
    assert row.umur == 21
    assert row.nilai == 85
