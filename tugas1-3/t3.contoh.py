import os
from pathlib import Path

def sapa(nama):
    print("Halo", nama)

def luas(panjang, lebar):
    return panjang * lebar

def lokasi():
    print(Path(os.getcwd()))

sapa("Alia")
print(luas(3, 4))