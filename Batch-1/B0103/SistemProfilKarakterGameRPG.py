# 1. Buat variabel profil karakter game
nama_hero = "Alfulus"       # String
level = 65                  # Integer
hp = 2380.5                 # Float
is_alive = True             # Boolean
inventory = ["Pedang Penderitaan", "Busur Petaka", "Tombak Penghancur", "Perisai Suci", "Jubah Kegelapan", "Cincin Keabadian"]
atribut = {"kekuatan": 285, "kelincahan": 120, "kecerdasan": 80, "ketahanan": 200, "kecepatan": 90, "ketangkasan": 110}

# 2. Tampilkan seluruh informasi karakter
print("--- INFORMASI KARAKTER ---")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

# 3. Tampilkan tipe data masing-masing variabel
print("\n--- TIPE DATA ---")
print("nama_hero :", type(nama_hero))
print("level     :", type(level))
print("hp        :", type(hp))
print("is_alive  :", type(is_alive))
print("inventory :", type(inventory))
print("atribut   :", type(atribut))

# 4. Aksi
# - Karakter dapat item baru
inventory.append("Ramuan HP")

# - Karakter naik level: konversi ke float lalu tambah 0.5
level = float(level)
level = level + 0.5

# 5. Cetak kembali informasi terbaru
print("\n--- INFORMASI TERBARU ---")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)
print("Tipe level sekarang :", type(level))