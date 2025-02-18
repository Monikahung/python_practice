# LATIHAN

# Kalkulator Sederhana

print(20*"=" + "\n" + "Kalkulator Sederhana" + "\n" + 20*"=" +"\n")

# input
angka_1 = float(input("Masukan angka 1 = "))
operator = input("Masukan operator (+, -, *, /) = ")
angka_2 = float(input("Masukan angka 2 = "))

# percabangan
if operator == "+" :
    hasil = angka_1 + angka_2
    print(f"Hasil = {hasil}")
elif operator == "-" :
    hasil = angka_1 - angka_2
    print(f"Hasil = {hasil}")
elif operator == "*" :
    hasil = angka_1 * angka_2
    print(f"Hasil = {hasil}")
elif operator == "/" :
    hasil = angka_1 / angka_2
    print(f"Hasil = {hasil}")
else :
    print("Maaf, anda ada kesalahan input")
print("Terima kasih telah menggunakan kalkulator kami")