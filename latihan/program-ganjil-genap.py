# PROGRAM MENENTUKAN BILANGAN GANJIL DAN BILANGAN GENAP

print("\n" + 5*"=" + "Program Ganjil Genap" + 5*"=" + "\n")

batasAngka = int(input("Masukan batasan: "))
angkaAwal = 0

print("Bilangan ganjil:")
while angkaAwal <= batasAngka:
    if angkaAwal % 2 != 0:
        print(angkaAwal)
    angkaAwal += 1

angkaAwal = 0

print("\nBilangan genap:")
while angkaAwal <= batasAngka:
    angkaAwal += 1
    if angkaAwal % 2 == 0:
        print(angkaAwal)