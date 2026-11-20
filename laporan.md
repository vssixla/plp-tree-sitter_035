## TUGAS 1: MEMBACA POHON SINTAKS PYTHON 
Saya membandingkan tiga pohon perkiraan tulisan tangan dengan hasil Tree-sitter. Pada fungsi `kuadrat`, saya memperkirakan `call`, sedangkan parser menghasilkan `function_definition` karena kode mendefinisikan fungsi. Pada percabangan, saya memperkirakan `else` memiliki kondisi kedua. Hasil parser menunjukkan bahwa satu `if_statement` memuat kondisi `hadir` dan cabang `alternative` berupa `else_clause`. Pada kelas `Kata`, saya sudah mengenali dua blok. Hasil parser memperjelas bahwa blok kelas membungkus method, sedangkan blok method membungkus `return 3`.

Pada `def kuadrat(x):`, `children` memperlihatkan empat token anonim pada dua tingkat pohon. Token `def` dan `:` berada langsung di bawah `function_definition`, sedangkan `(` dan `)` berada di bawah `parameters`. Melalui `named_children`, satu-satunya anak `parameters` yang tampil adalah `identifier` untuk `x`. Saat `:` setelah `def kuadrat(x)` dihapus, `has_error` berubah dari `False` menjadi `True` dan pohon menampilkan `(module (ERROR ...))`.

**KENDALA DAN SOSIAL** 

Pada pengerjaan awal, saya belum mencatat prediksi sehingga tidak memiliki bahan perbandingan. Saya mengulang percobaan dengan menggambar pohon sebelum menjalankan parser, lalu mencocokkan hubungan induk dan anak dengan output terminal.

**CATATAN PENGGUNAAN AI** 

Pada Tugas 1, saya menggunakan AI untuk merapikan penjelasan dan membantu membandingkan *parse tree* dari terminal dengan pohon yang saya susun secara manual. AI juga membantu menata output terminal yang semula ditampilkan dalam satu baris menjadi pohon berindentasi. Dengan format ini, saya dapat memeriksa hubungan antara node induk dan anak dengan lebih cepat.

Saat memeriksa draf, saya menemukan bahwa Percobaan 1 belum menyertakan pohon berindentasi seperti pada Percobaan 2 dan 3. Saya kemudian meminta AI untuk menambahkannya berdasarkan output asli. Pada ekspresi `x * x`, node `binary_operator` berada di dalam `return_statement` dan memiliki dua anak bertipe `identifier`, masing-masing mewakili `x` di sebelah kiri dan kanan operator `*`.

[Bukti output terminal](tugas1-3/output/t1-pohon.txt) · 
[Prediksi dan perbandingan lengkap](tugas1-3/catatan-tugas1.md)

## TUGAS 2: PENJELAJAH NODE TREE-SITTER
Saya menggunakan `jelajah.py` untuk menampilkan pohon sintaks Python dengan satu node bernama per baris. Fungsi `jelajah()` dimulai dari `tree.root_node`, lalu menelusuri `node.children` secara rekursif. Untuk setiap anak dengan `is_named` bernilai benar, skrip mengambil nama field melalui `field_name_for_child(i)` menggunakan indeks asli anak tersebut. Setiap turun satu tingkat, skrip menambahkan dua spasi agar hubungan induk dan anak terlihat.

**PENGUJIAN DAN HASIL**
Saya menguji skrip pada `t2.jelajah.py` pada `t2.file.py`, program pengelolaan stok koperasi sepanjang 114 baris. Dari folder `tugas1-3/`, saya menyimpan hasil penelusuran pada file output/t2-pohon-stok.txt . 

Cuplikan output berikut menunjukkan bagaimana Tree-sitter membaca perhitungan nilai stok pada fungsi `nilai_stok()`.

```text
return_statement [14:8]
  binary_operator [14:15]
    left: attribute [14:15]
      object: identifier [14:15]
      attribute: identifier [14:20]
    right: attribute [14:28]
      object: identifier [14:28]
      attribute: identifier [14:33]
```

Pada `return self.harga * self.stok`, perkalian menjadi anak dari `return_statement`. Kedua operand berada pada kedalaman yang sama. Field `left` memuat `self.harga` dan field `right` memuat `self.stok`. Di dalam masing-masing operand, field `object` menunjuk ke `self`, sedangkan field `attribute` menunjuk ke `harga` atau `stok`.

### PERBANDINGAN DENGAN PLAYGROUND
| Bagian yang diperiksa | Posisi awal di terminal | Posisi awal di Playground | Struktur yang cocok |
|---|---|---|---|
| `return` pada `nilai_stok()` | `[14:8]` | `[13, 8]` | `return_statement` memuat `binary_operator` dengan field `left` dan `right`. |
| `if` pada `status()` | `[17:8]` | `[16, 8]` | `if_statement` memuat kondisi pada `condition`, blok pada `consequence`, dan cabang `elif` pada `alternative`. |

**KENDALA DAN PENYELESAIAN** 

Saat membandingkan kedua output, saya menemukan perbedaan nomor baris. Saya mencocokkan kembali posisi awal node pada versi kode yang sama. Playground menghitung baris dari 0, sedangkan `jelajah.py` menampilkan `baris + 1`. Keduanya menghitung kolom dari 0. Setelah memperhitungkan perbedaan ini, posisi, field, dan kedalaman node pada kedua bagian yang diperiksa sesuai.

**PENGGUNAAN AI** 

AI membantu saya dalam membuatkan program `file.py` di mana pada file.py ini sayang mengingkan untuk memasukkan berbagai logika dan operasi. AI juga membantu validasi saya, yang awawlnya saya tidak sadar pada hal yang berkaitan dengan kendala. 

[Program penjelajah](tugas1-3/t2.jelajah.py) · [Kode pengujian](tugas1-3/t2.file.py) · [Bukti output](tugas1-3/output/t2-pohon.txt)


## TUGAS 3: QUERY PERTAMA TREE-SITTER

Saya membaca `t3.contoh.py` dan mencatat prediksi nama fungsi beserta jumlah parameternya, letak pemanggilan `print()`, dan nama modul yang diimpor. Saya kemudian menjalankan tiga query melalui `t3.q.py` dan membandingkan hasilnya dengan catatan tersebut.

**PENGUJIAN DAN HASIL**

| Query | Prediksi manual | Hasil query |
|---|---|---|
| `t3.fungsi.scm` | `sapa(nama)`, `luas(panjang, lebar)`, dan `lokasi()` | `sapa` memiliki 1 parameter, `luas` memiliki 2 parameter, dan `lokasi` memiliki 0 parameter. |
| `t3.print.scm` | Tiga pemanggilan `print()` pada baris 5, 11, dan 14. | Capture `@panggilan` muncul satu kali pada masing-masing baris 5, 11, dan 14. |
| `t3.impor.scm` | Modul `os` pada baris 1 dan `pathlib` pada baris 2. | Capture `@modul` menghasilkan `os` dan `pathlib` pada kedua baris tersebut. |

Ketiga hasil sesuai dengan prediksi. Pada query fungsi, `matches()` memasangkan nama fungsi dengan daftar parameternya sehingga jumlah parameter dapat dihitung untuk setiap definisi. Pada `from pathlib import Path`, query menangkap `pathlib` sebagai modul sumber. Sementara itu, `Path` adalah nama yang diambil dari modul tersebut.

**KENDALA DAN PENYELESAIAN**

Saat memeriksa jumlah pemanggilan `print()`, saya memperhatikan bahwa satu pemanggilan menghasilkan dua baris output. Contohnya terlihat pada fungsi `lokasi()`:

```text
@panggilan  baris 11: print(Path(os.getcwd()))
@fn  baris 11: print
```

Capture `@fn` menunjukkan nama fungsi yang diperiksa oleh predikat `#eq?`, sedangkan `@panggilan` menunjukkan seluruh ekspresi pemanggilan. Karena itu, saya menghitung kemunculan `@panggilan` dan memperoleh tiga pemanggilan. Pemanggilan di dalam `lokasi()` ikut terdeteksi meskipun fungsi itu belum dijalankan, karena Tree-sitter memeriksa struktur kode sumber.

**CATATAN PENGGUNAAN AI**

AI membantu saya untuk menyiapkan contoh kode, menyusun pola query, memahami perbedaan antara `@fn` dan `@panggilan`, serta memberikan path untuk mengerjakan tugas 3 ini. 


## TUGAS 4: GRAMMAR DSL FILTER UNTUK HALAMAN ADMIN

Saya menyusun grammar bahasa filter di `tree-sitter-filter/grammar.js`. Saya mulai dari perbandingan sederhana seperti `status = "open"`, lalu menambahkan angka, boolean, operator logika, tanda kurung, serta operator `in` dan `contains`. Setiap kali menambahkan fitur, saya membangkitkan parser dengan `tree-sitter generate`, memeriksa pohonnya dengan `tree-sitter parse contoh.filter`, dan menguji hasilnya terhadap pohon yang diharapkan di `test/corpus/dasar.txt`.

**PENGUJIAN DAN HASIL**

Delapan kasus uji lulus. Tiga kasus pertama memeriksa perbandingan string, perbandingan angka, dan dua kondisi yang dihubungkan dengan `and`. Lima kasus berikut menunjukkan bagaimana parser mengelompokkan ekspresi.

| Input | Hasil yang diperiksa |
|---|---|
| `a = 1 or b = 2 and c = 3` | Node terluar di bawah `query` adalah `or_expression`. Anak kanannya berupa `and_expression`, sehingga pengelompokannya adalah `a = 1 or (b = 2 and c = 3)`. |
| `(a = 1 or b = 2) and c = 3` | Node terluarnya menjadi `and_expression`. Di sebelah kiri, `parenthesized` membungkus `or_expression`. |
| `not archived = true` | Field `operand` pada `not_expression` memuat perbandingan dengan nilai bertipe `boolean`. |
| `status in ("open", "pending", "closed")` | Satu `in_expression` memuat identifier `status` dan tiga node `string`. |
| `title contains "invoice"` | `contains_expression` memuat `title` sebagai `field` dan string `"invoice"` sebagai `value`. |

Hasil akhir dari `tree-sitter test`:

```text
Total parses: 8; successful parses: 8; failed parses: 0; success percentage: 100.00%; average speed: 1591 bytes/ms
```

**KENDALA DAN PENYELESAIAN**

Pada tahap awal, `tree-sitter generate` menampilkan `ReferenceError: module is not defined in ES module scope`. Proyek saya menggunakan ES Module, sementara grammar awal menggunakan `module.exports`. Saya menggantinya dengan `export default` agar format ekspor grammar sesuai dengan konfigurasi proyek.

Saat menambahkan `or_expression`, saya mendapat pesan `Unresolved conflict` untuk urutan `_expr 'or' _expr • 'or' …`. Pada rangkaian `A or B or C`, parser memiliki dua kemungkinan pengelompokan. Saya menggunakan `prec.left` untuk menetapkan pengelompokan dari kiri dan memberikan prioritas lebih tinggi kepada `and` daripada `or`. Saya memeriksa hasilnya melalui dua tes di atas, yaitu ekspresi campuran dengan dan tanpa tanda kurung.

**CATATAN PENGGUNAAN AI**

Saya menggunakan AI untuk membantu memahami konflik operator, membandingkan pohon dengan hasil yang diharapkan, membantu saya dalam memperbaiki kode program pada grammar.js . 

[Grammar filter](tree-sitter-filter/grammar.js) · [Delapan kasus uji dan pohon yang diharapkan](tree-sitter-filter/test/corpus/dasar.txt)


## TUGAS 5: HIGHLIGHT UNTUK DSL FILTER
Saya membuat aturan *syntax highlighting* pada `tree-sitter-filter/queries/highlights.scm` untuk bahasa filter yang telah dikembangkan pada Tugas 4. File `tree-sitter.json` dikonfigurasi agar ekstensi `.filter` dikenali dan aturan highlight dibaca dari `queries/highlights.scm`. Pengerjaan dimulai dari satu pola `(string) @string`, kemudian dilanjutkan secara bertahap untuk angka, boolean, kata kunci, operator perbandingan, dan nama field. Kata kunci `in` dan `contains` ditambahkan terakhir.

**PENGUJIAN DAN HASIL**

Pengujian awal menggunakan `title contains "invoice"`. Perintah `tree-sitter query queries/highlights.scm contoh.filter` menangkap `"invoice"` sebagai `string` pada posisi `(0, 15)` sampai `(0, 24)`. Perintah `tree-sitter highlight contoh.filter` juga menampilkan string tersebut berwarna hijau di terminal. Setelah konfigurasi terbukti bekerja, saya memperluas `contoh.filter` menjadi satu ekspresi enam baris yang memuat seluruh kategori token.

| Kategori | Capture | Contoh yang terverifikasi |
|---|---|---|
| Kata kunci | `@keyword` | `and`, `or`, `not`, `in`, `contains` |
| Operator perbandingan | `@operator` | `=`, `!=`, `>`, `<`, `>=`, `<=` |
| String | `@string` | `"open"`, `"closed"`, `"bug"`, `"invoice"` |
| Angka | `@number` | `2`, `5`, `10`, `100` |
| Boolean | `@constant.builtin` | `true`, `false` |
| Nama field | `@property` | `status`, `priority`, `total`, `archived`, `verified`, `category`, `title` |

Hasil `tree-sitter query` menunjukkan keenam capture sesuai dengan token yang dimaksud. Secara khusus, `category` mendapat `@property` melalui `in_expression`, sedangkan `title` melalui `contains_expression`; nama field pada perbandingan biasa ditangkap melalui `comparison`. Hasil `tree-sitter highlight` terakhir memperlihatkan warna token berdasarkan kategori di terminal. Sebelum pengujian highlight, `tree-sitter parse contoh.filter` tidak menampilkan `ERROR` atau `MISSING`, dan `tree-sitter test` meluluskan seluruh delapan kasus (8 berhasil, 0 gagal, 100%).

**KENDALA DAN PENYELESAIAN**

Saat konfigurasi awal, saya sempat menggunakan perintah pembuka file konfigurasi yang tidak sesuai: `code "$env:LOCALAPPDATA\tree-sitter\config.json"`. Perintah tersebut menggunakan sintaks PowerShell, padahal terminal saya adalah CMD. Selain itu, output `tree-sitter init-config` menyatakan bahwa konfigurasi sebenarnya disimpan di `C:\Users\ASUS\AppData\Roaming\tree-sitter\config.json`, bukan `AppData\Local`. Saya membuka lokasi yang ditampilkan CLI, lalu menambahkan folder induk `D:/POLBAN/PEL/SEM3/PLP/plp-tree-sitter_035` ke `parser-directories`. Pada `tree-sitter.json`, properti `file-types` ternyata sudah benar, sehingga saya hanya menambahkan `"highlights": "queries/highlights.scm"`. Hasil query dan warna string setelah perbaikan membuktikan konfigurasi sudah terbaca.

**CATATAN PENGGUNAAN AI**

Saya menggunakan AI untuk memandu urutan pengerjaan, menyusun pola capture, menentukan lokasi file, dan memeriksa output `parse`, `query`, serta `highlight`. Saya menemukan kekurangan pada instruksi AI awal: lokasi konfigurasi diarahkan ke `AppData\Local` dan perintahnya menggunakan sintaks PowerShell. Saya membandingkan saran tersebut dengan output asli `tree-sitter init-config` yang menunjukkan lokasi `AppData\Roaming`, kemudian memperbaiki perintah sesuai terminal CMD. Saya juga tidak langsung menganggap semua warna benar dari output teks; kecocokan capture diperiksa melalui `tree-sitter query`, sedangkan warna dikonfirmasi melalui tampilan terminal. Dengan pemeriksaan tersebut, keenam kategori token berhasil diverifikasi.

[Aturan highlight](tree-sitter-filter/queries/highlights.scm) · [File pengujian](tree-sitter-filter/contoh.filter)



## TUGAS 6: MINI PROYEK PENDETEKSI TODO DAN FUNGSI PANJANG

Saya membuat program CLI `cek.py` untuk menganalisis file Python menggunakan Tree-sitter. Program memiliki tiga fitur, yaitu mendeteksi komentar TODO/FIXME, fungsi dengan panjang lebih dari 30 baris, dan kesalahan sintaks. Fitur pertama menggunakan query `comment` dengan predikat `#match?` serta `QueryCursor.captures()`. Fitur kedua menggunakan `QueryCursor.matches()` untuk memasangkan capture `@nama` dan `@fungsi`, kemudian menghitung panjang fungsi melalui `end_point[0] - start_point[0] + 1`. Fitur ketiga menggunakan `root_node.has_error` dan fungsi rekursif `cari_error_pertama()` untuk menemukan node `ERROR` atau `MISSING` beserta nomor barisnya.

**PENGUJIAN DAN HASIL**

Pengujian awal dilakukan pada tiga file buatan sendiri dalam folder `cek/uji/`. File `komentar.py` digunakan untuk membedakan TODO/FIXME dalam komentar dengan teks di dalam string. File `panjang.py` digunakan untuk menguji fungsi yang melebihi 30 baris, sedangkan `rusak.py` berisi kesalahan sintaks yang disengaja.

Hasil akhir dari `python cek.py uji`:

```text
uji\komentar.py:2: # TODO: tambahkan validasi jumlah barang
uji\komentar.py:4: # FIXME: perbaiki pembulatan harga
uji\panjang.py:1: fungsi hitung_stok memiliki 32 baris
uji\rusak.py:2: kesalahan sintaks (ERROR)
```
Pada pengujian fungsi panjang, perubahan panjang `hitung_stok` dari 31 menjadi 32 baris menghasilkan perubahan jumlah baris yang sesuai pada output. Komentar TODO di dalam string tidak ikut dilaporkan karena query hanya menangkap node `comment`. Kesalahan pada `rusak.py` berhasil dikenali sebagai `ERROR` di baris 2.

Pengujian selanjutnya dilakukan pada repositori open source Requests dari GitHub dengan commit `3c7baaa`. Program dijalankan menggunakan `python cek.py ..\..\requests-uji` dan menghasilkan 7 temuan komentar TODO/FIXME serta 56 fungsi dengan panjang lebih dari 30 baris. Tidak ditemukan laporan kesalahan sintaks. Salah satu hasilnya adalah fungsi `send` pada `adapters.py` sepanjang 115 baris dan `resolve_redirects` pada `sessions.py` sepanjang 122 baris.

Untuk verifikasi, saya memilih dua file Python secara acak menggunakan `random.sample()` dari daftar file yang dilacak Git. Hasil pemeriksaan manual dibandingkan dengan output `cek.py`.

| File acak | Hasil pemeriksaan manual | Hasil `cek.py` |
|---|---|---|
| `src/requests/__version__.py` | Tidak terdapat TODO/FIXME atau deklarasi fungsi, dan tidak terlihat kesalahan sintaks. | Tidak ada temuan. |
| `tests/test_adapters.py` | Tidak terdapat TODO/FIXME. Satu fungsi `test_request_url_handles_leading_path_separators` memiliki panjang 5 baris dan tidak terlihat kesalahan sintaks. | Tidak ada temuan. |

Hasil pemeriksaan manual pada kedua file sesuai dengan output cek.py. Validasi independen menggunakan ast.parse() dan py_compile juga menunjukkan bahwa kedua file memiliki sintaks Python yang valid, sehingga tidak adanya laporan kesalahan sintaks merupakan hasil yang sesuai.

**KENDALA DAN PENYELESAIAN**

Pada implementasi fitur ketiga, kondisi `if masalah is not None` awalnya memiliki indentasi yang sejajar dengan `if tree.root_node.has_error`. Kondisi tersebut berpotensi mengakses variabel `masalah` sebelum didefinisikan ketika file tidak memiliki kesalahan sintaks. Saya memperbaiki indentasinya sehingga pemeriksaan node hanya dilakukan jika `has_error` bernilai benar.

Saat pengujian berikutnya, output hanya menampilkan komentar TODO/FIXME dan fungsi panjang. Setelah diperiksa, file `rusak.py` belum tersedia di folder `uji/`. Saya kemudian membuat file tersebut dengan kode `hasil = jumlah + )` untuk menghasilkan kesalahan sintaks. Pengujian ulang berhasil menampilkan `kesalahan sintaks (ERROR)` pada baris 2.

**CATATAN PENGGUNAAN AI**

Saya menggunakan AI untuk membantu memahami penggunaan `QueryCursor.matches()`, menyusun fitur pencarian kesalahan secara rekursif, memandu pengujian, dan membandingkan hasil program dengan instruksi modul. AI juga membantu menentukan langkah pengujian pada repositori nyata dan pemilihan dua file acak.

Selama pemeriksaan kode, saya menemukan kekurangan pada penempatan indentasi fitur ketiga yang diberikan oleh AI. Saya memeriksa kembali alur kondisi `if`, memperbaiki indentasi, kemudian menjalankan `python cek.py uji` untuk memastikan file normal tetap dapat diproses dan kesalahan pada `rusak.py` berhasil dilaporkan. 

[Bukti pengujian lokal](cek/output/t6-uji.txt) · [Bukti pengujian repositori](cek/output/t6-repo.txt) · [Bukti validasi sintaks](cek/output/t6-validasi-sintaks.txt) · [Program CLI](cek/cek.py)