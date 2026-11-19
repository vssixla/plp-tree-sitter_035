import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

contoh_kode = {
    "Fungsi": """
def tambah_bonus(nilai):
    return nilai + 5
""".strip(),

    "If-Else": """
nilai = 80

if nilai >= 75:
    print("Lulus")
else:
    print("Belum lulus")
""".strip(),

    "Kelas dengan satu method": """
class Mahasiswa:
    def sapa(self):
        return "Halo"
""".strip(),
}

# initambahan iterasi, supaya cetak lebih rapi
def cetak_pohon(node, kedalaman=0, field=None):
    indentasi = "  " * kedalaman
    label = f"{field}: " if field else ""
    print(f"{indentasi}{label}{node.type}")

    for i, child in enumerate(node.children):
        if child.is_named:
            nama_field = node.field_name_for_child(i)
            cetak_pohon(child, kedalaman + 1, nama_field)

for judul, kode in contoh_kode.items():
    tree = parser.parse(kode.encode("utf-8"))

    print(f"\n=== {judul} ===")
    print("Kode:")
    print(kode)

    print("\nPohon asli:")
    print(tree.root_node)

    print("\nPohon berindentasi:")
    cetak_pohon(tree.root_node)

# Periksa node pada contoh fungsi
tree_fungsi = parser.parse(contoh_kode["Fungsi"].encode("utf-8"))
fungsi = tree_fungsi.root_node.named_children[0]

print("\n=== Anak langsung node fungsi ===")
for child in fungsi.children:
    status = "bernama" if child.is_named else "anonim"
    print(child.type, status)

parameter = fungsi.child_by_field_name("parameters")

print("\n=== Anak langsung node parameters ===")
for child in parameter.children:
    status = "bernama" if child.is_named else "anonim"
    print(child.type, status)

print("\nchildren pada parameters:")
print([child.type for child in parameter.children])

print("named_children pada parameters:")
print([child.type for child in parameter.named_children])