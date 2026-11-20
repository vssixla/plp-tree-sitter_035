# Pemilihan Konteks Kode untuk Asisten AI dengan Tree-sitter pada Aplikasi Django

**Draf proposal proyek · Programming Language Pragmatics**  
Alia Ardani · 251524035 · 2B D4 Teknik Informatika · Politeknik Negeri Bandung

## MASALAH DAN TUJUAN

Ketika pengembang bertanya kepada asisten AI bagaimana sebuah halaman memproses formulir, potongan fungsi yang diberikan sering berakhir tepat pada pemanggilan fungsi pembantu. Padahal, aturan validasi yang ditanyakan bisa berada di fungsi tersebut. Proyek ini mengusulkan alat yang memilih konteks untuk AI. Masukannya berupa berkas Python dan nama fungsi awal. Alat mengambil definisi fungsi itu beserta definisi fungsi lokal yang dipanggil langsung. Pertanyaan yang akan diuji adalah apakah konteks tambahan tersebut membantu AI menjawab dengan rujukan kode yang tepat.

## PERAN AI DAN TREE-SITTER

AI akan menjelaskan alur kode kepada pengembang. Tree-sitter akan menentukan cuplikan sumber yang disertakan dan mencatat asalnya agar pemilihan konteks dapat diulang pada revisi yang sama. Pencarian teks biasa dapat ikut mengambil nama fungsi yang muncul dalam komentar. Query atas pohon sintaks dapat membedakan komentar, definisi, dan pemanggilan. Pengaruh konteks akan diamati melalui ketepatan jawaban dan rujukan baris yang diberikan AI.

## BAHASA, FRAMEWORK, DAN CAKUPAN

Targetnya adalah berkas Python pada aplikasi Django, dengan grammar `tree-sitter-python`. Prototipe akan mengindeks fungsi tingkat modul, lalu mengambil fungsi pembantu hingga **satu tingkat pemanggilan**. Nama harus memiliki satu definisi yang cocok dalam berkas yang sama. Pemanggilan metode, alias, dan impor lintas berkas berada di luar cakupan awal.

## CONTOH KODE

```python
def stok_cukup(jumlah):
    return jumlah > 0

def proses_pesanan(jumlah):
    # stok_cukup(jumlah) pernah dipanggil di sini.
    return stok_cukup(jumlah)
```

Jika fungsi awalnya `proses_pesanan`, pemanggilan setelah `return` membuat definisi `stok_cukup` ikut diambil. Teks pada baris komentar dilewati. Jika baris terakhir diganti menjadi `return True`, hasil hanya memuat `proses_pesanan`.

## RANCANGAN QUERY

```scheme
(module (function_definition name: (identifier) @nama) @definisi)
(call function: (identifier) @dipanggil)
```

Pola pertama membangun indeks definisi. Pola kedua dijalankan pada body fungsi awal dengan melewati definisi bersarang. Nama hasil tangkapan dicocokkan dengan indeks. Setiap definisi cukup disertakan sekali.

## BENTUK KELUARAN

CLI akan menghasilkan satu berkas Markdown yang dapat dilampirkan ke percakapan AI. Setiap cuplikan memuat nama fungsi, berkas, rentang baris, dan alasan pemilihannya. Misalnya, entri `stok_cukup` diberi keterangan “dipanggil langsung oleh `proses_pesanan`”.

## CARA EVALUASI

Saya akan memilih lima fungsi awal dari berkas Python pada satu revisi repositori [Django](https://github.com/django/django), lalu mencatat fungsi pembantunya secara manual. Saya akan menghitung cuplikan yang tepat, terlewat, dan keliru disertakan. Untuk setiap fungsi awal, saya juga akan menyiapkan satu pertanyaan dan kunci jawaban berbasis kode. Pertanyaan yang sama akan diajukan dalam dua percakapan baru dengan model dan pengaturan yang sama. Percobaan pertama hanya menyertakan fungsi awal, sedangkan percobaan kedua memakai keluaran alat. Skor tiap jawaban adalah 0–2, masing-masing satu poin untuk isi yang benar dan rujukan baris yang mendukungnya.

## RENCANA KERJA DAN RISIKO

- **Minggu 1** — Memilih revisi dan sampel, menandai definisi serta pemanggilan, dan menyusun pertanyaan uji.
- **Minggu 2** — Menerapkan query dan CLI, lalu menguji komentar, pemanggilan berulang, serta nama yang ambigu.
- **Minggu 3** — Menjalankan dua percobaan konteks, memeriksa jawaban, dan mencatat batas pendekatan.

Parameter atau variabel lokal dapat memiliki nama yang sama dengan fungsi tingkat modul. Kasus tersebut akan ditandai untuk pemeriksaan manual. Karena respons AI dapat bervariasi, hasil lima pertanyaan akan dilaporkan sebagai evaluasi awal.
