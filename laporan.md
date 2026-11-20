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
Saya menguji skrip pada `file.py`, program pengelolaan stok koperasi sepanjang 114 baris. Dari folder `tugas1-3/`, saya menyimpan hasil penelusuran pada file output/t2-pohon-stok.txt . 

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

