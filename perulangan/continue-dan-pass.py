# CONTINUE AND PASS

# Pass

# Pass -> berfungsi sebagai dummy, tidak akan dieksekusi
# Contoh:
angka = 0
while angka < 5:
    angka += 1
    if angka == 3:
        pass # ini tidak akan dieksekusi
    print(angka)

# Continue
angka = 0
print(f"Angka sekarang -> {angka}")

while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print(f"Kamu angka {angka}")
        continue # artinya, jika kondisi ini bernilai benar, maka kondisi ini akan ditampilkan dan langsung balik ke perulangan awal (aksi di bawahnya tidak akan ditampilkan)

    print(f"Halo angka {angka}") # aksi 2

print("Finish")