# PR OPERASI KOMPARASI DAN LOGIKA

# ++++++++++0----------5++++++++++8----------11++++++++++
print("\n==========PROGRAM MEMERIKSA NILAI==========")
print("=======================================================================")
print("Ketentuan:\nNilai bernilai benar jika nilai<0, 5<nilai<8, atau nilai>11")
print("=======================================================================")
inputUser = float(input("Masukan angka sembarang: "))
print("Hasil:")
# angka<0
hasilPertama = inputUser < 0
print("Apakah angka<0?", hasilPertama)
# 5<angka<8
ketentuanPertama = inputUser > 5
ketentuanKedua = inputUser < 8
hasilKedua = ketentuanPertama and ketentuanKedua
print("Apakah 5<angka<8?", hasilKedua)
# angka>11
hasilKetiga = inputUser > 11
print("Apakah angka>11?", hasilKetiga)
# hasil akhir
hasilAkhir = hasilPertama or hasilKedua or hasilKetiga
print("Jadi, angka tersebut bernilai", hasilAkhir)