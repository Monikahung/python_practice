# OPERASI

# Index -> 0(-3)    1(-2)   2(-1)
    # Index pertama adalah 0
    # Index terakhir adalah -1
data_list = ["Monika", "Sihungka", "Siaw Hung"]
print(f"Data list = {data_list}")

# Mengambil data dari list ini
data_list_pertama = data_list[0]
print(f"Data list yang pertama = {data_list_pertama}")

data_list_terakhir = data_list[-1]
print(f"Data list yang terakhir = {data_list_terakhir}")

data_monika = data_list[-3]
print(f"Data Monika = {data_monika}")

# Mengambil info jumlah data dari list
panjang_list = len(data_list)
print(f"Panjang list = {panjang_list}")

## Manipulasi Data List
print(f"Data mula-mula =\n{data_list}")

# Menambahkan item list sesuai posisi tertentu (insert)
data_list.insert(1, "Marcell") # (posisi, item)
print(f"Data setelah ditambahkan =\n{data_list}")

# Menambahkan item list di akhir (append)
data_list.append("Ahung") # (item)
print(f"Data ditambahkan lagi =\n{data_list}")

# Menambahkan list ke dalam list (extend)
data_tambah = ["Ming-ming", "Cel-cel", "Mar-mar"]
data_list.extend(data_tambah) # artinya kita akan menambahkan data yang ada pada list 'data_tambah' ke dalam list 'data_list' sehingga data pada list 'data_tambah' akan berada di belakang data list 'data_tambah'
print(f"Data gabungan =\n{data_list}")

# Mengubah data dalam list
# Mengubah data ke-2 menjadi Hungka
data_list[2] = "Hungka"
print(f"Data setelah diubah data ke-2 =\n{data_list}")

# Menghapus data pada index tertentu di dalam list (remove)
data_list.remove("Ahung") # Catatan: penulisan data yang ingin dihapus harus sesuai dengan data yang ada di dalam list
print(f"Data setelah dihapus =\n{data_list}")

# Menghapus data list paling akhir (pop)
data_list.pop()
print(f"Data yang dihapus ujungnya =\n{data_list}")