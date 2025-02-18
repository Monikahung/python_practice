# IF AND ELSE STATEMENT

# if, kondisi, aksi

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

nama = input("Siapa nama anda? ")

# PROGRAM IF INLINE
if nama == "Monika" : print("Kamu keren!")
print(f"Terima kasih {nama}.")

# PROGRAM IF INDENTATION (Menggunakan tab/menjorok ke dalam)
if nama == "Monika" :
    print("Kamu keren!") # ini menjorok ke dalam
    print("Kamu juga baik sekali!") # ini menjorok ke dalam
print(f"Terima kasih {nama}.")

# ELSE STATEMENT
if nama == "Monika" :
    print(f"Kamu keren sekali, {nama}!")
else :
    print(f"Maaf, kamu bukan Monika, kamu {nama}.")
print("Akhir dari program.")