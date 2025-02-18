# LATIHAN MEMBUAT SEGITIGA

# Segitiga menggunakan for
print("\n", 5*"=", "Program Membuat Segitiga Menggunakan For", 5*"=", "\n")
jumlahSisi = int(input("Masukan jumlah sisi segitiga: "))

# dummy variable
count = 1
for i in range(jumlahSisi):
    print("*" * count)
    count += 1

print("\nAkhir dari program")

# Segitiga menggunakan while
print("\n", 5*"=", "Program Membuat Segitiga Menggunakan While", 5*"=", "\n")
jumlahSisi = int(input("Masukan jumlah sisi segitiga: "))

# dummy varible
count = 1
while True:
    print("*" * count)
    count += 1

    if count > jumlahSisi:
        break

print("\nAkhir dari program")

# Segitiga ganjil
print("\n", 5*"=", "Program Membuat Segitiga Ganjil", 5*"=", "\n")
jumlahSisi = int(input("Masukan jumlah sisi segitiga: "))

# dummy variable
count = 1
while True:
    if count % 2 == 1:
        print("*" * count)
        count += 1
        continue
    else:
        count += 1

    if count > jumlahSisi:
        break

print("\nAkhir dari program")

# Segitiga sama kaki
print("\n" + 5*"=" + "Program Membuat Segitiga Sama Kaki", 5*"=", "\n")
jumlahSisi = int(input("Masukan jumlah sisi segitiga: "))

# dummy variable
count = 1
spasi = int(jumlahSisi)
while True:
    if count % 2 == 1:
        print(" " * int((spasi / 2)), "*" * count, " " * int((spasi / 2)))
        count += 1
        spasi -= 1
        continue
    else:
        count += 1
        spasi -= 1
    
    if count > jumlahSisi:
        break

print("\nAkhir dari program")