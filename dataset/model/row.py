from dataclasses import dataclass

@dataclass
class Row:
    id: int
    nama: str
    umur: int
    gender: str
    nilai: float
    matkul: str
    tanggal: str
    uts: float
    uas: float
