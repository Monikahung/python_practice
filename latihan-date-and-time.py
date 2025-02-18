# DATE AND TIME (LATIHAN)

import datetime as dt

print("\nSilakan masukan tanggal, bulan, dan tahun lahir anda!\n")
tanggalLahir= int(input("Tanggal\t\t\t: "))
bulanLahir = int(input("Bulan\t\t\t: "))
tahunLahir = int(input("Tahun\t\t\t: "))

tanggalLahirAnda = dt.date(tahunLahir, bulanLahir, tanggalLahir)
print(f"\nTanggal lahir\t\t: {tanggalLahirAnda}")
tanggalHariIni = dt.date.today()
print(f"Tanggal hari ini\t: {tanggalHariIni}")

umur = tanggalHariIni - tanggalLahirAnda
umurTahun = umur.days // 365
umurBulan = (umur.days % 365) // 12
umurHari = ((umur.days % 365) % 12)
print(f"Umur anda\t\t: {umurTahun} tahun, {umurBulan} bulan, {umurHari} hari")