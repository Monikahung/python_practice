# Latihan Membuat Rumah

print("\n", 5*"=", "Program Membuat Rumah Sederhana", 5*"=", "\n")

panjangTotal = int(input("Masukan angka: "))

print("Tampilan:\n")

# Variabel spesifik
panjangDepan = int(panjangTotal / 3)
panjangBelakang = int((2 * panjangTotal) / 3)

count = 1
spasi = int(panjangDepan)
while True:
    if count % 2 == 1:
        print(" " * int(spasi / 2) + "*" * count + "=" * panjangBelakang)
        spasi -= 1
        count += 1
        continue
    else:
        spasi -= 1
        count += 1

    if count > panjangDepan:
        break

count = 1
while True:
    if panjangDepan % 2 == 1:
        if count % 2 == 1:
            print("+" * panjangDepan + "#" * int(panjangTotal - panjangDepan))
            count += 1
        else:
            count += 1
    else:
        if count % 2 == 1:
            print(" " + "+" * int(panjangDepan - 1) + "#" * int(panjangTotal - panjangDepan))
            count += 1
        else:
            count += 1
    
    if count > panjangDepan:
        break

print("\nRumah terselesaikan\n")