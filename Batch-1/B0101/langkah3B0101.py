#1. List (Berurutan, bisa berubah / mutable)
hobi = ["Membaca", "Koding", "Berenang"]
print("List Hobi:   ", hobi)
print("Tipe:    ", type(hobi))

#2. TUPLE (Berurutan, TIDAK BISA diubah / immutable)
koordinat = (-6.1751, 106.8650)
print("Tuple Koordinat:   ", koordinat)
print("Tipe:    ", type(koordinat))

#3. DICTIONARY (Pasangan Key : Value)
mahasiswa = {
    "nama": "Alfin",
    "nim": "261080200001",
    "ipk": 4.00
}

print("Dict mahasiswa:   ", mahasiswa)
print("Nama mahasiswa:   ", mahasiswa["nama"])
print("Tipe:    ", type(mahasiswa))

#4. SET (Nilai unik, tidak berurutan, tidak ada duplikat)
angka_unik = {1, 2, 2, 3, 4, 4, 5}
print("Set angka unik (otomatis menghapus duplikat):   ", angka_unik)
print("Tipe:    ", type(angka_unik))