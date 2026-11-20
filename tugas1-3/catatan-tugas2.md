
# TUGAS 3: HASIL ANALISIS MANUAL

## 1. Definisi Fungsi dan Parameter
- sapa: 1 parameter (nama)
- luas: 2 parameter (panjang, lebar)
- lokasi: 0 parameter

Total: 3 fungsi.

## 2. Pemanggilan print()
- Baris 5: print("Halo", nama)
- Baris 11: print(Path(os.getcwd()))
- Baris 14: print(luas(3, 4))

Total: 3 pemanggilan print().

## 3. Import Modul
- import os
- from pathlib import Path

Total: 2 modul, yaitu os dan pathlib.
Path merupakan nama yang diimpor dari pathlib.

## 4. Catatan
Analisis manual dilakukan sebelum menjalankan
query Tree-sitter.

Tree-sitter membaca struktur kode sumber tanpa
mengeksekusi program. Oleh karena itu, print()
di dalam fungsi lokasi() tetap dihitung meskipun
fungsi tersebut tidak dipanggil.
