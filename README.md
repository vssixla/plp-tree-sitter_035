# 🌳 TREE-SITTER — PROGRAMMING LANGUAGE PRAGMATICS
| Informasi | Keterangan |
|---|---|
| **Nama** | Alia Ardani |
| **NIM** | 251524035 |
| **Kelas** | 2B — D4 Teknik Informatika |

## DESKRIPSI PROYEK

Repositori ini berisi hasil pengerjaan Tugas 1–6 mengenai penggunaan **Tree-sitter** dalam mata kuliah Programming Language Pragmatics (PLP).

Tree-sitter merupakan parser generator dan library incremental parsing yang digunakan untuk menganalisis struktur sintaks kode sumber. Tree-sitter dapat menghasilkan pohon sintaks, mengenali berbagai jenis node, melakukan pencarian pola, serta membantu pengembangan alat analisis kode.

Melalui enam tugas ini, saya mempelajari penggunaan Tree-sitter mulai dari memahami struktur pohon sintaks Python hingga mengembangkan grammar bahasa sederhana dan membangun program analisis statis berbasis Command Line Interface (CLI).

### TUJUAN PEMBELAJARAN

1. Memahami konsep parsing dan struktur pohon sintaks.
2. Mengenali named node, anonymous node, field, dan posisi node.
3. Mengimplementasikan penelusuran pohon secara rekursif.
4. Menggunakan query Tree-sitter untuk mencari pola dalam kode.
5. Mengembangkan grammar untuk Domain-Specific Language (DSL).
6. Mengimplementasikan syntax highlighting berdasarkan kategori token.
7. Membuat CLI untuk mendeteksi pola dan kesalahan sintaks dalam file Python.

---

## STRUKTUR REPOSITORI

```text
plp-tree-sitter_035/
│
├── README.md
├── laporan.md
│
├── tugas1-3/
│   ├── t1.py
│   ├── catatan-tugas1.md
│   ├── t2.file.py
│   ├── t2.jelajah.py
│   ├── t2.kecil.py
│   ├── t3.contoh.py
│   ├── t3.fungsi.scm
│   ├── t3.impor.scm
│   ├── t3.print.scm
│   ├── t3.q.py
│   ├── t3.semua.scm
│   ├── catatan-tugas3.md
│   └── output/
│
├── tree-sitter-filter/
│   ├── grammar.js
│   ├── tree-sitter.json
│   ├── contoh.filter
│   ├── queries/
│   │   └── highlights.scm
│   ├── test/
│   │   └── corpus/
│   │       └── dasar.txt
│   ├── src/
│   └── bindings/
│
└── cek/
    ├── README.md
    ├── cek.py
    ├── uji/
    │   ├── komentar.py
    │   ├── panjang.py
    │   └── rusak.py
    └── output/
        ├── t6-uji.txt
        ├── t6-repo.txt
        └── t6-validasi-sintaks.txt
```

Folder `src/` dan `bindings/` pada proyek `tree-sitter-filter` merupakan bagian dari struktur parser dan binding yang dihasilkan atau disiapkan oleh Tree-sitter.

---

## RANGKUMAN TUGAS

| Tugas | Topik | Implementasi |
|---|---|---|
| **Tugas 1** | Membaca Pohon Sintaks Python | Membandingkan prediksi pohon dengan hasil Tree-sitter |
| **Tugas 2** | Penjelajah Node | Membuat penelusuran rekursif terhadap struktur pohon |
| **Tugas 3** | Query Pertama | Mencari definisi fungsi, pemanggilan `print`, dan modul impor |
| **Tugas 4** | Grammar DSL Filter | Membuat grammar bahasa filter sederhana |
| **Tugas 5** | Syntax Highlighting | Membuat aturan pewarnaan token DSL filter |
| **Tugas 6** | Mini Proyek Analisis Statis | Mendeteksi TODO/FIXME, fungsi panjang, dan kesalahan sintaks |

---

## TUGAS 1 — MEMBACA POHON SINTAKS PYTHON

Pada tugas pertama, saya mempelajari cara Tree-sitter merepresentasikan kode Python dalam bentuk pohon sintaks.

Saya membuat prediksi struktur pohon secara manual, kemudian membandingkannya dengan hasil parser.

### KONSEP YANG DIPELAJARI

- Perbedaan `function_definition` dan `call`.
- Hubungan parent dan child dalam pohon sintaks.
- Perbedaan `children` dan `named_children`.
- Named node dan anonymous node.
- Penggunaan `ERROR` ketika struktur sintaks tidak valid.

### HASIL PENGUJIAN

Tree-sitter dapat membedakan deklarasi fungsi, ekspresi pemanggilan, dan struktur percabangan berdasarkan grammar Python.

Pada percobaan penghapusan tanda `:` dalam definisi fungsi, parser menunjukkan keberadaan node `ERROR`.

**Berkas terkait:**

- [Program Tugas 1](tugas1-3/t1.py)
- [Catatan dan Perbandingan](tugas1-3/catatan-tugas1.md)
- [Output Pohon Sintaks](tugas1-3/output/t1-pohon.txt)

---

## TUGAS 2 — PENJELAJAH NODE TREE-SITTER

Tugas kedua berfokus pada implementasi penelusuran pohon menggunakan Python.

Saya mengembangkan `t2.jelajah.py` untuk menelusuri node secara rekursif dan menampilkan struktur pohon dengan indentasi sesuai kedalamannya.

### FITUR IMPLEMENTASI

- Penelusuran node menggunakan rekursi.
- Menampilkan jenis node dan posisi awal.
- Menampilkan hubungan induk dan anak.
- Mengidentifikasi field menggunakan `field_name_for_child()`.
- Menambahkan indentasi berdasarkan kedalaman node.

### HASIL PENGUJIAN

Program diuji pada `t2.file.py`, yaitu kode pengelolaan stok koperasi sepanjang 114 baris.

Hasil penelusuran dibandingkan dengan Tree-sitter Playground. Perbedaan nomor baris ditemukan karena Playground menggunakan indeks berbasis 0, sedangkan program penjelajah menampilkan nomor baris berbasis 1.

**Berkas terkait:**

- [Program Penjelajah](tugas1-3/t2.jelajah.py)
- [Kode Pengujian](tugas1-3/t2.file.py)
- [Output Penelusuran](tugas1-3/output/t2-pohon.txt)

---

## TUGAS 3 — QUERY PERTAMA TREE-SITTER

Pada tugas ketiga, saya mempelajari cara melakukan pencarian pola pada pohon sintaks menggunakan query Tree-sitter.

Tiga query utama yang dibuat adalah:

| Query | Tujuan |
|---|---|
| `t3.fungsi.scm` | Menemukan definisi fungsi dan jumlah parameter |
| `t3.print.scm` | Menemukan pemanggilan fungsi `print()` |
| `t3.impor.scm` | Menemukan modul yang diimpor |

### HASIL PENGUJIAN

Pengujian dilakukan pada file `t3.contoh.py`.

Hasilnya:

- Fungsi `sapa` memiliki 1 parameter.
- Fungsi `luas` memiliki 2 parameter.
- Fungsi `lokasi` memiliki 0 parameter.
- Terdapat 3 pemanggilan `print()`.
- Modul yang ditemukan adalah `os` dan `pathlib`.

Hasil query sesuai dengan penghitungan manual pada kode sumber.

**Berkas terkait:**

- [Kode Pengujian](tugas1-3/t3.contoh.py)
- [Query Fungsi](tugas1-3/t3.fungsi.scm)
- [Query Print](tugas1-3/t3.print.scm)
- [Query Import](tugas1-3/t3.impor.scm)
- [Catatan Tugas 3](tugas1-3/catatan-tugas3.md)

---

## TUGAS 4 — GRAMMAR DSL FILTER UNTUK HALAMAN ADMIN

Pada tugas keempat, saya membuat grammar bahasa sederhana bernama `filter` menggunakan Tree-sitter.

DSL ini dirancang untuk merepresentasikan ekspresi filter yang dapat digunakan pada halaman administrasi aplikasi.

### FITUR GRAMMAR

Grammar mendukung:

- Perbandingan: `=`, `!=`, `>`, `<`, `>=`, `<=`.
- Tipe data string, angka, dan boolean.
- Operator logika `and`, `or`, dan `not`.
- Pengelompokan dengan tanda kurung.
- Operator `in`.
- Operator `contains`.

Contoh ekspresi:

```text
status = "open" and priority > 2
```

```text
status in ("open", "pending", "closed")
```

```text
title contains "invoice"
```

### PENGUJIAN GRAMMAR

Parser dibangkitkan dan diuji menggunakan:

```bash
tree-sitter generate
tree-sitter parse contoh.filter
tree-sitter test
```

**Hasil pengujian:**

```text
Total parses: 8
Successful parses: 8
Failed parses: 0
Success percentage: 100.00%
```

Seluruh delapan kasus pengujian berhasil, termasuk prioritas operator `and` dan `or`.

**Berkas terkait:**

- [Grammar DSL](tree-sitter-filter/grammar.js)
- [Contoh Ekspresi](tree-sitter-filter/contoh.filter)
- [Corpus Pengujian](tree-sitter-filter/test/corpus/dasar.txt)

---

## TUGAS 5 — SYNTAX HIGHLIGHTING DSL FILTER

Pada tugas kelima, saya membuat aturan syntax highlighting agar token bahasa filter dapat dibedakan berdasarkan kategorinya.

Aturan ditulis dalam file `queries/highlights.scm`.

### KATEGORI HIGHLIGHT

| Kategori | Capture | Contoh |
|---|---|---|
| Kata kunci | `@keyword` | `and`, `or`, `not`, `in`, `contains` |
| Operator | `@operator` | `=`, `!=`, `>`, `<` |
| String | `@string` | `"open"`, `"invoice"` |
| Angka | `@number` | `2`, `10`, `100` |
| Boolean | `@constant.builtin` | `true`, `false` |
| Field | `@property` | `status`, `priority`, `title` |

### PENGUJIAN

Pengujian dilakukan menggunakan:

```bash
tree-sitter query queries/highlights.scm contoh.filter
tree-sitter highlight contoh.filter
```

Hasil query menunjukkan token berhasil ditangkap sesuai kategorinya. Pewarnaan token juga diperiksa melalui tampilan terminal.

**Berkas terkait:**

- [Aturan Highlight](tree-sitter-filter/queries/highlights.scm)
- [File Pengujian](tree-sitter-filter/contoh.filter)
- [Konfigurasi Parser](tree-sitter-filter/tree-sitter.json)

---

## TUGAS 6 — MINI PROYEK PENDETEKSI TODO DAN FUNGSI PANJANG

Pada tugas keenam, saya mengembangkan program CLI `cek.py` untuk melakukan analisis statis terhadap file Python.

### FITUR UTAMA

| Fitur | Deskripsi | Implementasi |
|---|---|---|
| TODO/FIXME | Mendeteksi komentar TODO atau FIXME | Query dengan `#match?` |
| Fungsi panjang | Mendeteksi fungsi lebih dari 30 baris | `matches()` dan posisi node |
| Kesalahan sintaks | Mendeteksi `ERROR` atau `MISSING` | `has_error` dan rekursi |

### PENGUJIAN LOKAL

Jalankan:

```bash
cd cek
python cek.py uji
```

Contoh output aktual:

```text
uji\komentar.py:2: # TODO: tambahkan validasi jumlah barang
uji\komentar.py:4: # FIXME: perbaiki pembulatan harga
uji\panjang.py:1: fungsi hitung_stok memiliki 32 baris
uji\rusak.py:2: kesalahan sintaks (ERROR)
```

### PENGUJIAN REPOSITORI NYATA

Program juga diuji menggunakan repositori open source [Requests](https://github.com/psf/requests), pada commit `3c7baaa`.

Hasil pemindaian:

| Jenis Temuan | Jumlah |
|---|---:|
| Komentar TODO/FIXME | 7 |
| Fungsi lebih dari 30 baris | 56 |
| Kesalahan sintaks yang dilaporkan | 0 |
| **Total temuan** | **63** |

Dua file acak diperiksa secara manual dan menunjukkan hasil yang sesuai dengan keluaran program. Validasi sintaks independen juga dilakukan menggunakan `ast.parse()` dan `py_compile`.

**Berkas terkait:**

- [Program CLI](cek/cek.py)
- [README Tugas 6](cek/README.md)
- [Output Pengujian Lokal](cek/output/t6-uji.txt)
- [Output Pengujian Requests](cek/output/t6-repo.txt)
- [Validasi Sintaks](cek/output/t6-validasi-sintaks.txt)

---

## INSTALASI DAN PERSIAPAN LINGKUNGAN

### PRASYARAT

Untuk menjalankan proyek, diperlukan:

- Python 3
- Node.js dan npm
- Tree-sitter CLI
- Git
- Visual Studio Code atau editor kode lainnya

### INSTALASI DEPENDENSI PYTHON

Jalankan:

```bash
python -m pip install tree-sitter tree-sitter-python
```

### INSTALASI TREE-SITTER CLI

Tree-sitter CLI dapat dipasang menggunakan npm:

```bash
npm install -g tree-sitter-cli
```

Periksa instalasi:

```bash
tree-sitter --version
```

### CLONE REPOSITORI

```bash
git clone https://github.com/vssixla/plp-tree-sitter_035.git
cd plp-tree-sitter_035
```

---

## CARA MENJALANKAN PROYEK

### TUGAS 1 — MEMBACA POHON

```bash
cd tugas1-3
python t1.py
```

### TUGAS 2 — PENJELAJAH NODE

```bash
cd tugas1-3
python t2.jelajah.py t2.file.py
```

### TUGAS 3 — QUERY TREE-SITTER

```bash
cd tugas1-3
python t3.q.py
```

### TUGAS 4 — GRAMMAR DSL

```bash
cd tree-sitter-filter
tree-sitter generate
tree-sitter parse contoh.filter
tree-sitter test
```

### TUGAS 5 — SYNTAX HIGHLIGHTING

Dari folder `tree-sitter-filter/`:

```bash
tree-sitter query queries/highlights.scm contoh.filter
tree-sitter highlight contoh.filter
```

### TUGAS 6 — ANALISIS STATIS

Dari folder `cek/`:

```bash
python cek.py uji
```

Untuk memeriksa folder Python lain:

```bash
python cek.py <folder>
```

Dokumentasi lengkap Tugas 6 tersedia di [cek/README.md](cek/README.md).

---

## RINGKASAN HASIL

| Tugas | Hasil Utama |
|---|---|
| Tugas 1 | Pohon sintaks dibandingkan dengan prediksi manual |
| Tugas 2 | Penjelajahan rekursif pada kode Python sepanjang 114 baris |
| Tugas 3 | Tiga query berhasil dan sesuai penghitungan manual |
| Tugas 4 | Delapan pengujian grammar berhasil (100%) |
| Tugas 5 | Enam kategori syntax highlighting berhasil diverifikasi |
| Tugas 6 | Tiga fitur analisis statis berjalan pada file lokal dan repositori nyata |

---

## DOKUMENTASI DAN REFERENSI

### DOKUMENTASI PROYEK

- [Laporan Pengerjaan Tugas 1–6](laporan.md)
- [Catatan Tugas 1](tugas1-3/catatan-tugas1.md)
- [Catatan Tugas 3](tugas1-3/catatan-tugas3.md)
- [Dokumentasi Mini Proyek Tugas 6](cek/README.md)

### REFERENSI

- [Tree-sitter — Official Website](https://tree-sitter.github.io/tree-sitter/)
- [Tree-sitter — GitHub](https://github.com/tree-sitter/tree-sitter)
- [Python Bindings for Tree-sitter](https://github.com/tree-sitter/py-tree-sitter)
- [Tree-sitter Python Grammar](https://github.com/tree-sitter/tree-sitter-python)
- Materi Praktikum *Part 1 — Tree-sitter*, Programming Language Pragmatics, Politeknik Negeri Bandung.

---

## CATATAN PENGEMBANGAN

Proyek ini dikerjakan sebagai bagian dari proses pembelajaran. Setiap implementasi diuji menggunakan kode sumber, output terminal, dan perbandingan manual sesuai kebutuhan tugas.

Penggunaan AI sebagai pendamping pembelajaran serta kendala yang ditemukan selama pengerjaan dicatat dalam `laporan.md`.

---

```text
 /\_/\
( o.o )
 > ^ <
```