# OPERASI KOMPARASI

# Operator yang berfungsi untuk membandingkan dua komponen
# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

# Variabel
a = 4
b = 2

# Operator > (lebih besar)
print("\n========== Lebih Besar (>) ==========")
hasil = a > 3
print("a > 3 =", hasil)
hasil = b > 3
print("b > 3 =", hasil)

# Operator < (Lebih kecil)
print("\n========== Lebih Kecil (<) ==========")
hasil = a < 3
print("a < 3 =", hasil)
hasil = b < 3
print("b < 3 =", hasil)

# Operator >= (lebih besar sama dengan)
print("\n========== Lebih Besar Sama Dengan (>=) ==========")
hasil = a >= 3
print("a >= 3 =", hasil)
hasil = b >= 3
print("b >= 3 =", hasil)
hasil = b >= 2
print("b >= 2 =", hasil)

# Operator <= (Lebih kecil sama dengan)
print("\n========== Lebih Kecil Sama Dengan (<=) ==========")
hasil = a <= 3
print("a <= 3 =", hasil)
hasil = b <= 3
print("b <= 3 =", hasil)
hasil = b <= 2
print("b <= 2 =", hasil)

# Operator == (Sama dengan)
print("\n========== Sama Dengan (==) ==========")
hasil = a == 4
print("a == 4 =", hasil)
hasil = b == 4
print("b == 4 =", hasil)

# Operator != (Tidak sama dengan)
print("\n========== Tidak Sama Dengan (!=) ==========")
hasil = a != 4
print("a != 4 =", hasil)
hasil = b != 4
print("b != 4 =", hasil)

# Operator is dan is not
# Operator ini digunakan untuk membandingkan dua variabel, yang mana variabel bersifat memakan memori komputer
# Jika digunakan untuk membandingkan literal (angka konstanta), maka akan muncul peringatan pada terminal

x = 4
y = 4
z = 3

print("\n========== Operator is ==========")
print("nilai x terletak di memori nomor", hex(id(x)))
print("nilai y terletak di memori nomor", hex(id(y)))
print("nilai z terletak di memori nomor", hex(id(z)))
hasil = x is y
print("x is y =", hasil)
hasil = y is z
print("y is z =", hasil)

print("\n========== Operator is not ==========")
print("nilai x terletak di memori nomor", hex(id(x)))
print("nilai y terletak di memori nomor", hex(id(y)))
print("nilai z terletak di memori nomor", hex(id(z)))
hasil = x is not y
print("x is not y =", hasil)
hasil = y is not z
print("y is not z =", hasil)