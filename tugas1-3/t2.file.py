"""Simulasi stok koperasi kampus untuk bahan uji Tree-sitter."""

from dataclasses import dataclass

@dataclass
class Barang:
    nama: str
    harga: int
    stok: int
    minimum: int
    isi_pak: int

    def nilai_stok(self):
        return self.harga * self.stok

    def status(self):
        if self.stok == 0:
            return "habis"
        elif self.stok < self.minimum:
            return "menipis"
        return "cukup"

    def usulan_pak(self):
        kekurangan = max(0, self.minimum - self.stok)
        pak_utuh = kekurangan // self.isi_pak
        sisa = kekurangan % self.isi_pak
        if sisa > 0:
            pak_utuh += 1
        return pak_utuh

def buat_katalog():
    return {
        "BK": Barang("Buku tulis", 6000, 25, 12, 6),
        "PL": Barang("Pulpen", 3500, 20, 10, 12),
        "PH": Barang("Penghapus", 2500, 4, 5, 5),
    }

def ubah_stok(katalog, jenis, kode, jumlah):
    if kode not in katalog:
        raise ValueError(f"Kode barang {kode} tidak ditemukan")
    if jenis not in ("masuk", "jual") or jumlah <= 0:
        raise ValueError("Jenis transaksi atau jumlah tidak valid")

    barang = katalog[kode]
    if jenis == "jual" and jumlah > barang.stok:
        raise ValueError(f"Stok {barang.nama} hanya {barang.stok}")

    if jenis == "masuk":
        barang.stok += jumlah
        return 0

    barang.stok -= jumlah
    return barang.harga * jumlah

def proses_transaksi(katalog, transaksi):
    omzet = 0
    terjual = 0
    ditolak = []
    for nomor, (jenis, kode, jumlah) in enumerate(transaksi, start=1):
        try:
            nilai = ubah_stok(katalog, jenis, kode, jumlah)
        except ValueError as masalah:
            ditolak.append((nomor, str(masalah)))
            continue

        omzet += nilai
        if jenis == "jual":
            terjual += jumlah

    return omzet, terjual, ditolak

def rupiah(nilai):
    return "Rp" + f"{nilai:,}".replace(",", ".")

def cetak_persediaan(katalog):
    print("PERSEDIAAN AKHIR")
    total = 0
    for kode, barang in sorted(katalog.items()):
        nilai = barang.nilai_stok()
        total += nilai
        print(f"{kode} | {barang.nama} | {barang.stok} unit | {barang.status()}")
    print(f"Nilai seluruh stok: {rupiah(total)}")

def cetak_usulan(katalog):
    print("\nUSULAN PEMBELIAN")
    perlu_dibeli = [barang for barang in katalog.values() if barang.usulan_pak()]
    if not perlu_dibeli:
        print("Seluruh stok mencukupi.")
        return
    for barang in perlu_dibeli:
        pak = barang.usulan_pak()
        unit = pak * barang.isi_pak
        print(f"{barang.nama}: {pak} pak ({unit} unit)")

def main():
    katalog = buat_katalog()
    transaksi = [
        ("masuk", "BK", 6),
        ("jual", "BK", 20),
        ("jual", "PL", 12),
        ("jual", "PH", 4),
        ("jual", "PH", 1),
        ("masuk", "XX", 2),
    ]
    omzet, terjual, ditolak = proses_transaksi(katalog, transaksi)
    cetak_persediaan(katalog)
    cetak_usulan(katalog)
    print(f"\nTerjual: {terjual} unit | Omzet: {rupiah(omzet)}")
    for nomor, alasan in ditolak:
        print(f"Transaksi {nomor} ditolak: {alasan}")


if __name__ == "__main__":
    main()