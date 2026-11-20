# TUGAS 6 — PEMERIKSA KODE PYTHON DENGAN TREE-SITTER

**Alia Ardani** · NIM **251524035** · 2B D4 Teknik Informatika, Politeknik Negeri Bandung  
[Repositori praktikum PLP Tree-sitter](https://github.com/vssixla/plp-tree-sitter_035)

`cek.py` membaca seluruh file `.py` dalam folder yang dipilih beserta subfoldernya. Setiap temuan ditampilkan dengan nama file dan nomor baris agar potongan kode terkait mudah ditemukan.

## FITUR PEMERIKSAAN

| Temuan | Aturan yang digunakan |
|---|---|
| Komentar TODO atau FIXME | Query dengan predikat `#match?` mencari teks `TODO` atau `FIXME` pada node komentar. Tulisan yang sama di dalam string dilewati. |
| Fungsi lebih dari 30 baris | Panjang dihitung dari baris awal definisi sampai baris akhir fungsi dengan rumus `akhir - awal + 1`. Fungsi sepanjang 31 baris mulai dilaporkan. Method di dalam kelas dan fungsi bersarang juga diperiksa. |
| Kesalahan sintaks | Jika `root_node.has_error` bernilai benar, program menelusuri pohon dan melaporkan lokasi node `ERROR` atau `MISSING` pertama yang ditemukan pada file tersebut. |

## INSTALASI DEPENDENSI

Gunakan Python 3. Dari folder utama repositori, jalankan perintah berikut di terminal:

```bat
cd cek
python -m pip install tree-sitter tree-sitter-python
```

## CARA MENJALANKAN

Dari folder `cek/`, jalankan pemeriksaan pada tiga file contoh yang sudah tersedia:

```bat
python cek.py uji
```

Untuk memeriksa proyek lain, gunakan pola `python cek.py <folder>`. Misalnya, jika folder `requests-uji` berada sejajar dengan folder utama repositori praktikum, jalankan:

```bat
python cek.py ..\..\requests-uji
```

## CONTOH OUTPUT

Hasil pengujian lokal pada folder `uji/`:

```text
uji\komentar.py:2: # TODO: tambahkan validasi jumlah barang
uji\komentar.py:4: # FIXME: perbaiki pembulatan harga
uji\panjang.py:1: fungsi hitung_stok memiliki 32 baris
uji\rusak.py:2: kesalahan sintaks (ERROR)
```

Pada contoh tersebut, program menemukan dua komentar, satu fungsi sepanjang 32 baris, dan satu kesalahan sintaks. Angka setelah nama file menunjukkan baris awal temuan. Jadi, `uji\panjang.py:1` berarti fungsi `hitung_stok` dimulai pada baris 1.

[Bukti pengujian lokal](output/t6-uji.txt) · [Hasil pemeriksaan repositori Requests](output/t6-repo.txt) · [Validasi sintaks dua file sampel](output/t6-validasi-sintaks.txt)

---

```text
 /\_/\
( o.o )
 > ^ <
```
