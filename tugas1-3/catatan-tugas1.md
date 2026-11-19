# Catatan Tugas 1: Membaca Pohon

## 1. Contoh kode dan hasil parse

Saya menguji tiga potongan kode Python: fungsi tambah_bonus,
percabangan if/else, serta kelas Mahasiswa dengan satu method sapa.

Pada contoh fungsi, function_definition memiliki field name,
parameters, dan body. Body memuat return_statement dengan
binary_operator untuk penjumlahan nilai + 5.

Pada contoh percabangan, module memuat penugasan dan if_statement.
Field condition memuat perbandingan nilai >= 75.
Field consequence memuat blok if, sedangkan alternative
memuat else_clause.

Pada contoh kelas, class_definition memuat nama Mahasiswa dan
body berupa block. Method sapa muncul sebagai function_definition
di dalam block kelas.

Output lengkap tersimpan dalam output/t1-pohon.txt.

## 2. Perkiraan dan perbandingan

### Fungsi
Pada perkiraan awal, saya mengenali unsur fungsi, identifier, kata kunci, dan operasi penjumlahan.
Saya mengidentifikasi tambah_bonus sebagai nama fungsi dan nilai sebagai parameternya.
Namun, perkiraan tersebut belum menjelaskan hubungan parent dan child secara lengkap.

Hasil parse menunjukkan bahwa module memuat function_definition dengan field name, parameters, dan body.
ama fungsi dan parameter muncul sebagai identifier pada posisi yang berbeda.
Field body menunjuk block yang memuat return_statement.
Di dalamnya, binary_operator memiliki operand kiri berupa identifier nilai dan operand kanan berupa integer 5.
Hasil tersebut sesuai dengan unsur yang saya kenali, sekaligus memperjelas susunan node yang belum tercakup dalam perkiraan awal.
Pemeriksaan lanjutan juga menunjukkan bahwa kata kunci def merupakan node anonim.


### If/else
Berdasarkan percobaan sebelumnya, penugasan nilai dapat dipahami sebagai node assignment,
sedangkan pemanggilan print sebagai node call. Pada kode percabangan, kedua struktur tersebut
muncul bersama kondisi dan dua blok tindakan.

Hasil parse menunjukkan bahwa module memiliki dua anak langsung, yaitu expression_statement yang memuat penugasan nilai = 80 dan if_statement yang memuat percabangan. Field condition menunjuk comparison_operator untuk kondisi nilai >= 75. Field consequence menunjuk blok berisi print("Lulus"), sedangkan field alternative menunjuk else_clause dengan blok berisi print("Belum lulus"). Struktur ini memperjelas bahwa penugasan berada di luar percabangan, sementara kedua blok tindakan berada di dalam struktur if_statement.

### Kelas dengan satu method
Percobaan fungsi sebelumnya memperlihatkan bahwa definisi fungsi memiliki nama, parameter, dan body. Konsep tersebut membantu memahami method sapa sebagai fungsi yang berada di dalam kelas Mahasiswa.

Hasil parse menunjukkan bahwa module memuat class_definition dengan field name berupa identifier Mahasiswa. Field body menunjuk block yang memuat function_definition untuk method sapa. Method tersebut memiliki parameter self dan body berisi return_statement. Teks "Halo" muncul sebagai node string dengan anak string_start, string_content, dan string_end. Dibandingkan fungsi tambah_bonus yang langsung berada di bawah module, method sapa berada di dalam blok kela

## 3. Node bernama dan anonim
Node bernama yang ditemukan antara lain identifier, parameters,
dan block. Empat node anonim yang diperiksa adalah def, :, (, dan ).

Pada node parameters:
- children menghasilkan ['(', 'identifier', ')'].
- named_children menghasilkan ['identifier'].

children mencakup semua anak langsung suatu node.
named_children hanya mencakup anak langsung yang bernama.
Keduanya tidak otomatis mengambil seluruh keturunan node.

## 4. Percobaan sintaks rusak

Saya menghapus titik dua setelah def tambah_bonus(nilai).
Parser tetap menghasilkan pohon, tetapi memuat node ERROR.
Nilai tree_rusak.root_node.has_error adalah True.

Hasil ini menunjukkan bahwa Tree-sitter tetap membentuk pohon
ketika kode tidak valid dan menandai masalah sintaks.
Pada percobaan ini, penanda yang muncul adalah ERROR.

## 5. Kendala dan bantuan AI

Kendala yang saya alami adalah output tree.root_node berbentuk
satu baris panjang sehingga sulit dibaca. AI membantu menambahkan
fungsi pencetak pohon berindentasi. Output asli tetap dipertahankan.

AI juga membantu memperbaiki dalam penyusunan contoh kode dan pemeriksaan node. 
AI juga membentu menjelaskan konsep Tree-sitter dalam menggunakan Playground sebelumnya. 