
import sys
from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNGSI = Query(PY, "(function_definition name: (identifier) @nama) @fungsi")

def cari_error_pertama(node):
    if node.is_error or node.is_missing:
        return node

    for anak in node.children:
        if anak.has_error or anak.is_missing:
            temuan = cari_error_pertama(anak)
            if temuan is not None:
                return temuan

    return None

def cek_file(path):
    tree = parser.parse(path.read_bytes())

    # Fitur 1: komentar TODO/FIXME (sudah jadi)
    for node in QueryCursor(Q_TODO).captures(tree.root_node).get("c", []):
        print(
            f"{path}:{node.start_point[0] + 1}: "
            f"{node.text.decode(errors='replace').strip()}"
        )

    # Fitur 2: fungsi yang lebih dari 30 baris
    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        fungsi = cap["fungsi"][0]
        nama = cap["nama"][0].text.decode(errors="replace")

        awal = fungsi.start_point[0] + 1
        akhir = fungsi.end_point[0] + 1
        panjang = akhir - awal + 1

        if panjang > 30:
            print(
                f"{path}:{awal}: fungsi {nama} "
                f"memiliki {panjang} baris"
        )

    # Fitur 3: mendeteksi kesalahan sintaks
    if tree.root_node.has_error:
        masalah = cari_error_pertama(tree.root_node)

        if masalah is not None:
            baris = masalah.start_point[0] + 1
            jenis = "MISSING" if masalah.is_missing else "ERROR"

            print(
                f"{path}:{baris}: kesalahan sintaks ({jenis})"
            )

for path in Path(sys.argv[1]).rglob("*.py"):
    cek_file(path)
