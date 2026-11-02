# Tugas Praktikum: Sistem Profil Karakter Game RPG

# 1. Variabel profil karakter
nama_hero = "Arga"                                  # String
level = 5                                           # Integer
hp = 100.0                                          # Float (Health Point)
is_alive = True                                     # Boolean
inventory = ["Pedang Besi", "Busur Kayu", "Belati"] # List (minimal 3 item senjata)
atribut = {"kekuatan": 80, "kecerdasan": 65}        # Dictionary


def cetak_profil():
    print("nama_hero :", nama_hero)
    print("level     :", level)
    print("hp        :", hp)
    print("is_alive  :", is_alive)
    print("inventory :", inventory)
    print("atribut   :", atribut)


# 2. Tampilkan seluruh informasi karakter
print("=== PROFIL KARAKTER ===")
cetak_profil()

# 3. Tampilkan tipe data masing-masing variabel
print("\n=== TIPE DATA ===")
print("nama_hero :", type(nama_hero))
print("level     :", type(level))
print("hp        :", type(hp))
print("is_alive  :", type(is_alive))
print("inventory :", type(inventory))
print("atribut   :", type(atribut))

# 4. Aksi karakter
# a. Mendapatkan item baru
inventory.append("Ramuan HP")

# b. Naik level: konversi ke float, lalu tambahkan 0.5
level = float(level)
level = level + 0.5

# 5. Cetak kembali informasi terbaru
print("\n=== PROFIL KARAKTER (TERBARU) ===")
cetak_profil()