# Pengujian Awal Tree Sitter Python
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

print("Pengujian Awal Tree Sitter Python")

kode = b"x = 1\n"
tree = parser.parse(kode)
print(tree.root_node)

#Percobaan 1: Fungsi Kuadrat 
print("\nPercobaan 1 - Fungsi kuadrat")

kode_fungsi = b"""def kuadrat(x):
    return x * x
"""

pohon_fungsi = parser.parse(kode_fungsi)
print(pohon_fungsi.root_node)

#Percobaan 2: If/Else
print("\nPercobaan 2 - If/Else")

kode_if_else = b"""if hadir:
    poin = 1
else:
    poin = 0
"""

pohon_if_else = parser.parse(kode_if_else)
print(pohon_if_else.root_node)

#Percobaan 3: Kelas dengan satu method
print("\nPercobaan 3 - Kelas dengan satu method")

kode_kelas = b"""class Kata:
    def jumlah_huruf(self):
        return 3
"""

pohon_kelas = parser.parse(kode_kelas)
print(pohon_kelas.root_node)

# Pemeriksaan node - Fungsi kuadrat
print("\nPemeriksaan node - Fungsi kuadrat")

fungsi = pohon_fungsi.root_node.named_children[0]
parameter = fungsi.child_by_field_name("parameters")

for induk in (fungsi, parameter):
    print(f"\nSemua anak {induk.type} (children):")
    for anak in induk.children:
        jenis = "bernama" if anak.is_named else "anonim"
        print(f"  {anak.type} -> {jenis}")

    print(f"Anak bernama {induk.type} (named_children):")
    for anak in induk.named_children:
        print(f"  {anak.type}")