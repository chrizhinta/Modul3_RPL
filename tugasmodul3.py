# Program Biodata Kelompok
# Tugas Modul 3_F5212510025

anggota = [
    {"nama": "Chrizhinta", "nim": "F5212510025", "jurusan": "Teknologi Informasi", "asal": "Indonesia"},
    {"nama": "Ingel", "nim": "F5212510015", "jurusan": "Teknologi Informasi", "asal": "Korea Selatan"},
    {"nama": "Adelia", "nim": "F5212510012", "jurusan": "Teknologi Informasi", "asal": "Sabang"},
]

print("=" * 40)
print("BIODATA KELOMPOK")
print("=" * 40)

for i, orang in enumerate(anggota, start=1):
    print(f"\nAnggota {i}")
    print(f"Nama     : {orang['nama']}")
    print(f"NIM      : {orang['nim']}")
    print(f"Jurusan  : {orang['jurusan']}")
    print(f"Asal     : {orang['asal']}")

print("\n" + "=" * 40)
print(f"Jumlah anggota kelompok: {len(anggota)}")