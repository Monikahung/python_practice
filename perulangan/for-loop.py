# Perulangan (Loop)

# Perulangan For
# for kondisi:
    # aksi

# For menggunakan list
angka_list = [0, 1, 2, 4]
print(angka_list)
for i in angka_list:
    print(f"Angka list ke {i} -> {i}")
print("Akhir dari program 1\n")

# For menggunakan range
angka_range = range(5) # artinya dimulai dari 0 sampai 4
for i in angka_range:
    print(f"Angka range ke {i} -> {i}")
print("Akhir dari program 2\n")

angka_range_kedua = range(1,5) # artinya dimulai dari 1 sampai 4
for i in angka_range_kedua:
    print(f"Angka range ke {i} -> {i}")
print("Akhir dari program 3\n")

# For menggunakan string
data_str = "Nama saya Monika"
for i in data_str:
    print(i)
print("Akhir dari program 4")