data_angka = [1, 4, 3, 7, 6, 2, 3, 4, 1, 2, 4, 5, 9]
print(f"Data list angka =\n{data_angka}")

# Count data (jumlah data)
data_angka_3 = data_angka.count(3)
data_angka_4 = data_angka.count(4)

print(f"Banyak angka 3 = {data_angka_3}")
print(f"Banyak angka 4 = {data_angka_4}")

# Ambil posisi data (index)
data_str = ["Aku", "Kamu", "Dia", "Ia"]
data_str_dia = data_str.index("Dia")
print(f"Index data 'Dia' = {data_str_dia}")
data_str_ia = data_str.index("Ia")
print(f"Index data 'Ia' = {data_str_ia}")

# Mengurutkan list (sort)
print(f"Data angka sebelum sort =\n{data_angka}")
data_angka.sort()
print(f"Data angka setelah sort =\n{data_angka}")

print(f"Data string sebelum sort = {data_str}")
data_str.sort()
print(f"Data string setelah sort = {data_str}")

# Membalik list (reverse)
data_angka.reverse()
print(f"Data angka setelah reverse = {data_angka}")
data_str.reverse()
print(f"Data string setelah reverse = {data_str}")