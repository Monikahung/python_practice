# LIST

# Kumpulan data angka (numbers)
data_angka = [1, 2, 3]
print(data_angka)

# Kumpulan data string
data_str = ["Monika", "Sihungka", "Siaw Hung"]
print(data_str)

# Kumpulan data boolean
data_bool = [True, False, True, False]
print(data_bool)

# Kumpulan data campuran
data_campuran = [1, "Monika", "1 TRPL A", True]
print(data_campuran)

## Cara alternatif membuat list

# Membuat list dengan menggunakan range
data_range = range(0, 10)
data_list = list(data_range)
print(data_list)

# Membuat list dengan menggunakan for loop
data_list_for = [i for i in range(0, 10, 2)] # (start, stop, step)
print(data_list_for)

# Membuat list dengan menggunakan for dan if
data_list_for_if = [i for i in range(0, 10) if i != 7] # data i, dimana i berada pada range(0, 10) dan jika i tidak sama dengan 7
print(data_list_for_if)

data_list_for_if = [i for i in range(0, 20) if i % 2 == 0 and i != 0]
print(data_list_for_if)

data_list_for_if = [i ** 2 for i in range(0, 10) if i % 2 != 0]
print(data_list_for_if)