# BREAK

# Contoh 1:
angka = 0
while angka < 5:
    angka += 1
    print(f"Angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print(f"Kamu angka {angka}")
        break # jika kondisi ini bernilai benar, maka kondisi ini akan ditampilkan dan program perulangan langsung selesai

    print(f"Halo angka {angka}") # aksi 2
print("Finish")

# Contoh 2:
inputAngka = int(input("Masukan batasan angka: "))
angka = 0
while True:
    angka += 1
    print(f"Angka sekarang -> {angka}")

    print(f"Halo angka {angka}")

    if angka == inputAngka:
        break # jika angka == inputAngka, maka program perulangan langsung selesai
print("Finish")