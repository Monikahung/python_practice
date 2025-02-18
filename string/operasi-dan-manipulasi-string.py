# OPERASI DAN MANIPULASI STRING

# 1. Menyambung string (concatenate)
nama_pertama = "Monika"
nama_tengah = "Siaw"
nama_akhir = "Hung"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. Operator untuk string
# a. Mengecek apakah ada komponen char atau string di string
s = "s"
status = s in nama_lengkap
print(s + " ada di " + nama_lengkap + " = " + str(status))
S = "S"
status = S in nama_lengkap
print(S + " ada di " + nama_lengkap + " = " + str(status))
s = "s"
status = s not in nama_lengkap
print(s + " tidak ada di " + nama_lengkap + " = " + str(status))

# b. Mengulang string
print("wk"*10)
print(15*"wk")

# c. Indexing
# Index dihitung dari 0, artinya huruf ke-1 berindex 0
print("Index ke-0: " + nama_lengkap[0])
print("Index ke-7: " + nama_lengkap[7])
# Index yang bernilai negatif, artinya index dihitung dari belakang
print("Index ke-[-1]: " + nama_lengkap[-1])
print("Index ke-[-2]: " + nama_lengkap[-2])
# Jika ingin menampilkan beberapa index yang berurutan, maka gunakan [index_awal:index_akhir+1]
print("Index ke-[0-5]: " + nama_lengkap[0:6])
print("Index ke-[7-10]: " + nama_lengkap[7:11])
# Jika ingin menampilkan beberapa angka dari index yang berbeda dengan pola tertentu, maka gunakan [index_awal:index_akhir+1:kenaikan_index]
print("Index ke-[0, 2, 4, 6, 8, 10, 12, 14]: " + nama_lengkap[0:15:2])
# Jika ingin menampilkan huruf dari index tertentu sampai akhir
print("Index ke-[7-akhir]: " + nama_lengkap[7:])
# Jika ingin menampilkan huruf dari index 0 sampai index tertentu
print("Index ke-[0-5]: " + nama_lengkap[:6])

# d. Menemukan item paling kecil
print("String paling kecil: " + min(nama_lengkap))

# e. Menemukan item paling besar
print("String paling besar: " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII " + str(data) + " adalah " + chr(data))

# 4. Operator dalam bentuk method
data = "Halo nama saya Monika"
jumlah = data.count("a")
print("Jumlah char 'a' pada kalimat " + data + " adalah " + str(jumlah))