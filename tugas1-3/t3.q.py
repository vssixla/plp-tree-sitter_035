import sys
from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

bahasa = Language(tspython.language())
parser = Parser(bahasa)

kode = Path(sys.argv[1]).read_bytes()
pola = Path(sys.argv[2]).read_text(encoding="utf-8")

tree = parser.parse(kode)
query = Query(bahasa, pola)
cursor = QueryCursor(query)

for _, cap in cursor.matches(tree.root_node):
    if "params" in cap:
        nama = cap["nama"][0].text.decode()
        jumlah = cap["params"][0].named_child_count
        print(f"{nama}: {jumlah} parameter")
    else:
        for label, nodes in cap.items():
            for node in nodes:
                baris = node.start_point.row + 1
                print(f"@{label}  baris {baris}: {node.text.decode()}")