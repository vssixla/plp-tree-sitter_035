# CATATAN PERBANDING PERCOBAAN DENGAN PROGRAM PADA TUGAS 1

## PERCOBAAN 1 — Fungsi `kuadrat`
**KODE YANG DIUJI**
```python
def kuadrat(x):
    return x * x
```

**PREDIKSI SEBELUM PARSER**
```text
module
  expression_statement
    call
      function: identifier
      arguments: integer
        return_statement
        binary_operator
          left: integer
          right: integer
```

**HASIL PARSER**
```text
Percobaan 1 - Fungsi kuadrat
(module (function_definition name: (identifier) parameters: (parameters (identifier)) body: (block (return_statement (binary_operator left: (identifier) right: (identifier))))))
```

**HASIL PARSER YANG DIRAPIKAN**
```text
module
    function_definition
        name: identifier
        parameters: parameters
            identifier
        body: block
            return_statement
                binary_operator
                    left: identifier
                    right: identifier
```

**PERBANDINGAN**

Saya memperkirakan akar pohonnya adalah `module` dan operasi `x * x` membentuk `binary_operator` dengan sisi `left` dan `right`. Kedua perkiraan ini sesuai dengan hasil parser.

Pada prediksi awal, saya menggambar `call` karena saya mengira `kuadrat(x)` merupakan pemanggilan fungsi. Setelah melihat hasil parser, saya memahami bahwa kata `def` menandai definisi fungsi. Oleh karena itu, anak langsung dari `module` adalah `function_definition`. Nama `kuadrat` muncul pada field `name`, sedangkan parameter `x` muncul sebagai `identifier` di dalam `parameters`.

Saya juga memperkirakan `return_statement` dan `binary_operator` berada pada tingkat yang sama. Hasil parser menunjukkan bahwa `return_statement` berada di dalam `block`, lalu `binary_operator` menjadi anak dari `return_statement` karena `x * x` adalah ekspresi yang dikembalikan. Kedua operand muncul sebagai `identifier` karena kode menggunakan nama variabel `x` pada kedua sisi perkalian.


## PERCOBAAN 2 — Percabangan if/else
**KODE YANG DIUJI**
```python
if hadir:
    poin = 1
else:
    poin = 0
```

**PREDIKSI SEBELUM PARSER**
```text
module
    if_statement 
    condition: identifier
        expression_statement
            assignment
                left: identifier
                right: integer 
    another_statement 
    condition: identifier 
        expression_statement
	    assignment
                left: identifier
                right: integer
        
```

**HASIL PARSER**
```text
Percobaan 2 - If/Else
(module (if_statement condition: (identifier) consequence: (block (expression_statement (assignment left: (identifier) right: (integer)))) alternative: (else_clause body: (block (expression_statement (assignment left: (identifier) right: (integer)))))))
```

**HASIL PARSER YANG DIRAPIKAN**
```text
module
    if_statement
        condition: identifier
        consequence: block
            expression_statement
                assignment
                    left: identifier
                    right: integer
        alternative: else_clause
            body: block
                expression_statement
                    assignment
                        left: identifier
                        right: integer
```

**PERBANDINGAN**

Saya sudah tepat memperkirakan `module` sebagai akar pohon dan `hadir` sebagai `identifier` yang berperan sebagai kondisi. Prediksi saya untuk kedua penugasan juga sesuai. Baik `poin = 1` maupun `poin = 0` menghasilkan `expression_statement` yang memuat `assignment`. Pada keduanya, `left` menunjuk ke `identifier` untuk nama `poin`, sedangkan `right` menunjuk ke `integer` untuk nilai `1` atau `0`.

Perbedaannya terdapat pada susunan cabang. Dalam prediksi saya, `condition` sejajar dengan `if_statement`, dan penugasan `poin = 1` berada di bawah kondisi. Hasil parser menunjukkan bahwa `condition`, `consequence`, dan `alternative` adalah tiga field milik satu `if_statement`. Field `condition` menunjuk ke `hadir`, sedangkan `consequence` menunjuk ke `block` yang berisi `poin = 1`.

Untuk cabang `else`, saya memperkirakan ada `another_statement` dengan kondisi kedua. Pada hasil parser, field `alternative` menunjuk ke node `else_clause`. Di dalamnya, field `body` menunjuk ke `block` yang berisi `poin = 0`. Kondisi hanya muncul satu kali karena `else` dijalankan ketika kondisi `hadir` bernilai salah.


## PERCOBAAN 3 — Kelas Dengan Satu Method
**KODE YANG DIUJI**
```python
class Kata:
    def jumlah_huruf(self):
        return 3
```

**PREDIKSI SEBELUM PARSER**
```text
module
    class_definition
    name: identifier 
    body: block
        function_definition
            name: identifier 
            parameters: identifier 
        body: block 
	    return_statement
	        integer
```

**HASIL PARSER**
```text
Percobaan 3 - Kelas dengan satu method
(module (class_definition name: (identifier) body: (block (function_definition name: (identifier) parameters: (parameters (identifier)) body: (block (return_statement (integer)))))))
```

**HASIL PARSER YANG DIRAPIKAN**
```text
module
    class_definition
        name: identifier
        body: block
            function_definition
                name: identifier
                parameters: parameters
                    identifier
                body: block
                    return_statement
                        integer
```

**PERBANDINGAN**

Saya sudah memperkirakan bahwa `module` merupakan akar pohon, `jumlah_huruf` muncul sebagai `function_definition` di dalam blok kelas, dan angka `3` menjadi node `integer` di bawah `return_statement`. Saya juga memperkirakan adanya dua node `block`, masing-masing untuk isi kelas dan isi method.

Dalam prediksi saya, `name` dan `body` milik kelas ditulis sejajar dengan `class_definition`. Hasil parser menunjukkan bahwa keduanya berada satu tingkat di dalam `class_definition`. Hal serupa terjadi pada `body` milik method. Saya menulisnya sejajar dengan `function_definition`, padahal blok yang berisi `return 3` berada di dalam definisi method tersebut.

Perbedaan kedua terdapat pada parameter `self`. Saya memperkirakan `parameters: identifier`. Pada hasil aktual, field `parameters` menunjuk ke node `parameters`, lalu node tersebut memiliki anak `identifier` yang mewakili `self`.


## PEMERIKSAAN NODE BERNAMA DAN ANONIM
Pada definisi fungsi `kuadrat`, `children` menampilkan lima anak langsung.
Dua di antaranya merupakan token anonim, yaitu `def` dan `:`.
Dengan `named_children`, yang tampil hanya tiga node bernama, yaitu
`identifier` untuk nama fungsi, `parameters` untuk parameter, dan `block`
untuk isi fungsi.

Pada bagian `(x)`, `children` menampilkan tiga anak secara berurutan,
yaitu `(`, `identifier`, dan `)`. Dengan `named_children`, hanya
`identifier` yang mewakili `x` yang tampil. Dari hasil ini, saya melihat
bahwa `children` mencakup semua anak langsung, sedangkan `named_children`
hanya mencakup anak langsung yang bernama.


## PENGUJIAN KODE TANPA TITIK DUA
Pada pengujian ini menghapus tanda `:` di akhir baris `def kuadrat(x):` pada salinan fungsi, lalu membandingkan hasil parse dengan fungsi asli.

**HASIL PARSER**

```text
Pengujian error - Fungsi kuadrat tanpa titik dua
Kode valid, has_error = False
Kode rusak, has_error = True
(module (ERROR (identifier) (parameters (identifier)) (return_statement (binary_operator left: (identifier) right: (identifier)))))
```

**PERBANDINGAN**

Pada kode valid, anak langsung `module` adalah `function_definition` dan nilai `has_error` adalah `False`. Setelah titik dua dihapus, anak langsung `module` berubah menjadi `ERROR` dan `has_error` menjadi `True`. Tree-sitter tetap menghasilkan pohon. Di dalam `ERROR`, parser masih mengenali parameter `x` dan pernyataan `return x * x`.