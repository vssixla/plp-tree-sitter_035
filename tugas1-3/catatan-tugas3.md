# TUGAS 3: HASIL ANALISIS 

## PERCOBAAN 1: MELAKUKAN ANALISIS SECARA MANUAL
**1. Definisi Fungsi dan Parameter**

- sapa: 1 parameter (nama)
- luas: 2 parameter (panjang, lebar)
- lokasi: 0 parameter

Total: 3 fungsi.

**2. Pemanggilan print()**

- Baris 5: print("Halo", nama)
- Baris 11: print(Path(os.getcwd()))
- Baris 14: print(luas(3, 4))

Total: 3 pemanggilan print().

**3. Import Modul**

- import os
- from pathlib import Path

Total: 2 modul, yaitu os dan pathlib.
Path merupakan nama yang diimpor dari pathlib.

**4. Catatan**

Analisis manual dilakukan sebelum menjalankan
query Tree-sitter.

Tree-sitter membaca struktur kode sumber tanpa
mengeksekusi program. Oleh karena itu, print()
di dalam fungsi lokasi() tetap dihitung meskipun
fungsi tersebut tidak dipanggil.

## PERCOBAAN 2: PENGUJIAN QUERY TREE SITTER 
### Tahap 1: Pencarian Seluruh Identifier
```text
D:\POLBAN\PEL\SEM3\PLP\plp-tree-sitter_035\tugas1-3>python t3.q.py t3.contoh.py t3.semua.scm
@id  baris 1: os
@id  baris 2: pathlib
@id  baris 2: Path
@id  baris 4: sapa
@id  baris 4: nama
@id  baris 5: print
@id  baris 5: nama
@id  baris 7: luas
@id  baris 7: panjang
@id  baris 7: lebar
@id  baris 8: panjang
@id  baris 8: lebar
@id  baris 10: lokasi
@id  baris 11: print
@id  baris 11: Path
@id  baris 11: os
@id  baris 11: getcwd
@id  baris 13: sapa
@id  baris 14: print
@id  baris 14: luas
```
Query (identifier) @id digunakan untuk menemukan seluruh identifier pada kode sumber Python. Hasil pengujian menunjukkan bahwa Tree-sitter menemukan 20 kemunculan identifier, meliputi nama modul, fungsi, parameter, dan identifier lainnya. Query ini masih bersifat umum karena belum membatasi pencarian berdasarkan peran identifier.

### Tahap 2: Pencarian Nama Fungsi
```text
D:\POLBAN\PEL\SEM3\PLP\plp-tree-sitter_035\tugas1-3>python t3.q.py t3.contoh.py t3.semua.scm
@nama  baris 4: sapa
@nama  baris 7: luas
@nama  baris 10: lokasi
```
Query (function_definition name: (identifier) @nama) digunakan untuk mencari identifier yang berperan sebagai nama definisi fungsi. Hasil pengujian menunjukkan tiga fungsi, yaitu sapa pada baris 4, luas pada baris 7, dan lokasi pada baris 10.

## Kesimpulan

Kedua percobaan berhasil dilakukan. Query pertama menemukan seluruh identifier, sedangkan query kedua mempersempit pencarian hanya pada nama fungsi. Hasil percobaan kedua sesuai dengan analisis manual pada Tahap 1, sehingga menunjukkan bahwa pola query Tree-sitter dapat digunakan untuk mencari struktur sintaks tertentu secara spesifik.


## PERCOBAAN 3: PENGUJIAN TIGA QUERY WAJIB
### 1. Query Fungsi dan Parameter
**File:** `t3.fungsi.scm`

Query menggunakan `function_definition`, `matches()`, dan `named_child_count` untuk mencari nama fungsi serta menghitung jumlah parameternya.

**Hasil:**
```text
sapa: 1 parameter
luas: 2 parameter
lokasi: 0 parameter
```

**Analisis:** Ketiga fungsi berhasil ditemukan dengan jumlah parameter yang sesuai dengan perhitungan manual.

### 2. Query Pemanggilan print()

**File:** `t3.print.scm`

Query menggunakan node `call` dan predicate `#eq?` untuk menemukan pemanggilan fungsi `print()`.

**Hasil:**
```text
@panggilan  baris 5: print("Halo", nama)
@panggilan  baris 11: print(Path(os.getcwd()))
@panggilan  baris 14: print(luas(3, 4))
```

**Analisis:** Ditemukan tiga pemanggilan `print()` berdasarkan capture `@panggilan`. Pemanggilan di dalam fungsi `lokasi()` tetap terdeteksi meskipun fungsi belum dijalankan.

### 3. Query Modul Impor

**File:** `t3.impor.scm`

Query menggunakan `import_statement` dan `import_from_statement` untuk menemukan nama modul yang diimpor.

**Hasil:**
```text
@modul  baris 1: os
@modul  baris 2: pathlib
```

**Analisis:** Ditemukan dua modul, yaitu `os` dan `pathlib`. `Path` tidak termasuk karena merupakan nama yang diimpor dari modul `pathlib`.

### Kesimpulan
Ketiga query berhasil dijalankan dan seluruh hasilnya sesuai dengan perhitungan manual pada Tahap 1. Tree-sitter mampu mengidentifikasi struktur kode secara spesifik tanpa menjalankan program.

