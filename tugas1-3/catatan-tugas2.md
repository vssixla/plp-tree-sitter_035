# TUGAS 3: HASIL ANALISIS 

## PERCOBAAN 1: MELAKUKAN ANALISIS SECARA MANUAL
*** 1. Definisi Fungsi dan Parameter ***

- sapa: 1 parameter (nama)
- luas: 2 parameter (panjang, lebar)
- lokasi: 0 parameter

Total: 3 fungsi.

*** 2. Pemanggilan print() ***

- Baris 5: print("Halo", nama)
- Baris 11: print(Path(os.getcwd()))
- Baris 14: print(luas(3, 4))

Total: 3 pemanggilan print().

*** 3. Import Modul ***

- import os
- from pathlib import Path

Total: 2 modul, yaitu os dan pathlib.
Path merupakan nama yang diimpor dari pathlib.

*** 4. Catatan ***

Analisis manual dilakukan sebelum menjalankan
query Tree-sitter.

Tree-sitter membaca struktur kode sumber tanpa
mengeksekusi program. Oleh karena itu, print()
di dalam fungsi lokasi() tetap dihitung meskipun
fungsi tersebut tidak dipanggil.

## PERCOBAAN 2: PENGUJIAN QUERY TREE SITTER 
### Tahap 1: Pencarian Seluruh Identifier
Query (identifier) @id digunakan untuk menemukan seluruh identifier pada kode sumber Python. Hasil pengujian menunjukkan bahwa Tree-sitter menemukan 20 kemunculan identifier, meliputi nama modul, fungsi, parameter, dan identifier lainnya. Query ini masih bersifat umum karena belum membatasi pencarian berdasarkan peran identifier.

### Tahap 2: Pencarian Nama Fungsi
Query (function_definition name: (identifier) @nama) digunakan untuk mencari identifier yang berperan sebagai nama definisi fungsi. Hasil pengujian menunjukkan tiga fungsi, yaitu sapa pada baris 4, luas pada baris 7, dan lokasi pada baris 10.

*** Kesimpulan ***
Kedua percobaan berhasil dilakukan. Query pertama menemukan seluruh identifier, sedangkan query kedua mempersempit pencarian hanya pada nama fungsi. Hasil percobaan kedua sesuai dengan analisis manual pada Tahap 1, sehingga menunjukkan bahwa pola query Tree-sitter dapat digunakan untuk mencari struktur sintaks tertentu secara spesifik.