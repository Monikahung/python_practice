# WIDTH AND MULTILINE

# Data
data_nama = "Monika Hung"
data_umur = 18
data_tinggi = 153
data_nomor_sepatu = 42

# String Standar
data_string = f"Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Nomor Sepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# String dengan menggunakan enter/newline (\n)
data_string = f"Nama = {data_nama}, \nUmur = {data_umur}, \nTinggi = {data_tinggi}, \nNomor Sepatu = {data_nomor_sepatu}"
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# String dengan menggunakan multiline (kutip tiga """ """)
data_string = f"""Nama         = {data_nama}
Umur         = {data_umur}
Tinggi       = {data_tinggi}
Nomor Sepatu = {data_nomor_sepatu}"""
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# Mengatur lebar
data_string = f"""Nama         = {data_nama:>11}
Umur         = {data_umur:>11}
Tinggi       = {data_tinggi:>11}
Nomor Sepatu = {data_nomor_sepatu:>11}""" # >11 artinya tanda > melambangkan string menjadi rata kanan, 11 artinya banyak string berjumlah 11 (kalau kurang, maka di sebelah kiri string akan kosong, kalau lebih, maka aturan ini tidak berlaku)
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)

# Percobaan
data_string = f"""Nama         = {data_nama.center(15)}
Umur         = {str(data_umur).center(15)}
Tinggi       = {str(data_tinggi).center(15)}
Nomor Sepatu = {str(data_nomor_sepatu).center(15)}"""
print("\n" + 5*"=" + "Data String" + 5*"=")
print(data_string)