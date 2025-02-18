# SOAL
# Buatlah program untuk menentukan umur seseorang, dengan inputan tahun sekarang dan tahun lahir, kemudian buat kondisi untuk menentukan kategori usianya, dengan kriteria sebagai berikut:
    # Jika umur 0 - 4 tahun maka kategori usianya adalah Balita.
    # Jika umur 5 - 11 tahun maka kategori usianya adalah Kanak-kanak.
    # Jika umur 12 - 25 tahun maka kategori usianya adalah Remaja.
    # Jika umur 26 - 45 tahun maka kategori usianya adalah Dewasa.
    # Jika umur 46 - 65 tahun maka kategori usianya adalah Lansia.
    # Jika umur 66 - diatasnya tahun maka kategori usianya adalah Manula.

# PROGRAM
print("\n" + 5*"=" + "Program Kategori Umur Seseorang" + 5*"=" + "\n")

tahunSekarang = int(input("Masukan tahun sekarang\t: "))
tahunLahir = int(input("Masukan tahun lahir anda: "))
umur = tahunSekarang - tahunLahir

print("\n" + 50*"=" + "\n")
print(f"Umur anda yaitu {umur}")

if umur <= 4:
    print("Kategori: Balita")
elif umur <= 11:
    print("Kategori: Kanak-kanak")
elif umur <= 25:
    print("Kategori: Remaja")
elif umur <= 45:
    print("Kategori: Dewasa")
elif umur <= 65:
    print("Kategori: Lansia")
else:
    print("Kategori: Manula")