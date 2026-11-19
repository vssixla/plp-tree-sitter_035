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
