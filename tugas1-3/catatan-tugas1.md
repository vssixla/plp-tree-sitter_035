# CATATAN PERBANDING PERCOBAAN DENGAN PROGRAM PADA TUGAS 1

## PERCOBAAN 1 — Fungsi `kuadrat`
**KODE YANG DIUJI**
```python
def kuadrat(x):
    return x * x
```

**PREDIKSI SEBELUM PARSE**
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

**PERBANIDNGAN**

Saya memperkirakan akar pohonnya adalah `module` dan operasi `x * x` membentuk `binary_operator` dengan sisi `left` dan `right`. Kedua perkiraan ini sesuai dengan hasil parser.

Pada prediksi awal, saya menggambar `call` karena saya mengira `kuadrat(x)` merupakan pemanggilan fungsi. Setelah melihat hasil parser, saya memahami bahwa kata `def` menandai definisi fungsi. Oleh karena itu, anak langsung dari `module` adalah `function_definition`. Nama `kuadrat` muncul pada field `name`, sedangkan parameter `x` muncul sebagai `identifier` di dalam `parameters`.

Saya juga memperkirakan `return_statement` dan `binary_operator` berada pada tingkat yang sama. Hasil parser menunjukkan bahwa `return_statement` berada di dalam `block`, lalu `binary_operator` menjadi anak dari `return_statement` karena `x * x` adalah ekspresi yang dikembalikan. Kedua operand muncul sebagai `identifier` karena kode menggunakan nama variabel `x` pada kedua sisi perkalian.