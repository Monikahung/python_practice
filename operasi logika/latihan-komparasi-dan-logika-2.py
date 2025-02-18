# PR OPERASI KOMPARASI DAN LOGIKA

# ----------0++++++++++5----------8++++++++++11----------
print("\nPROGRAM MEMERIKSA ANGKA")
print("=====================================================================")
print("Ketentuan:\nNilai bernilai benar jika terletak diantara 0-5 atau 8-11")
print("=====================================================================")
inputUser = float(input("Masukan angka sembarang: "))
print("Hasil:")
# 0<angka<5
ketentuanPertama = inputUser > 0
ketentuanKedua = inputUser < 5
hasilSementaraPertama = ketentuanPertama and ketentuanKedua
print("Apakah 0<angka<5?", hasilSementaraPertama)
# 8<angka<11
ketentuanKetiga = inputUser > 8
ketentuanKeempat = inputUser < 11
hasilSementaraKedua = ketentuanKetiga and ketentuanKeempat
print("Apakah 8<angka<11?", hasilSementaraKedua)
# hasil akhir
hasilAkhir = hasilSementaraPertama or hasilSementaraKedua
print("Jadi, angka tersebut bernilai", hasilAkhir)