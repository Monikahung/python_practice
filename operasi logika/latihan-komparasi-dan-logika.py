# LATIHAN OPERASI KOMPARASI DAN LOGIKA

# Latihan membuat program untuk memeriksa kebenaran nilai dari rentang angka

# ++++++++++3----------10++++++++++
print("\n==========PROGRAM MEMERIKSA NILAI<3 ATAU NILAI>10==========")
inputUser = float(input("Masukan angka<3 atau angka>10: "))
print("Hasil:")
# angka<3
kurangDari = inputUser < 3
print("Apakah angka<3?", kurangDari)
# angka>10
lebihDari = inputUser > 10
print("Apakah angka>10?", lebihDari)
# angka<3 or angka>10
hasil = kurangDari or lebihDari
print("Jadi, angka yang anda masukan bernilai", hasil)

# ----------3++++++++++10----------
print("\n==========PROGRAM MEMERIKSA 3<NILAI<10==========")
inputUser = float(input("Masukan 3<angka<10: "))
print("Hasil:")
# angka>3
lebihDari = inputUser > 3
print("Apakah angka>3?", lebihDari)
# angka<10
kurangDari = inputUser < 10
print("Apakah angka<10?", kurangDari)
# 3<angka<10
hasil = lebihDari and kurangDari
print("Jadi, angka yang anda masukan bernilai", hasil)