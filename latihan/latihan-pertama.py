# SOAL
# Anton ingin membeli sebuah tas dengan harga Rp 200.000,00, agar keinginannya tercapai dia berusaha dengan cara menabung setiap harinya, dia ingin 20 hari lagi dia bisa membeli tas tersebut, bantu Anton untuk menentukan berapa besar uang yang dia tabung setiap harinya agar dapat membeli tas tersebut!

# PROGRAM
print("\n" + 5*"=" + "PROGRAM BESARAN UANG TABUNGAN PER HARI" + 5*"=" + "\n")
hargaTotal = 200000
jumlahHari = 20

print(f"Harga sebuah tas yaitu Rp {hargaTotal:,.2f}")
print(f"Anton ingin menabung selama {jumlahHari} hari")

tabunganHari = hargaTotal / jumlahHari
print(f"Jadi, dia harus menabung sebesar Rp {tabunganHari:,.2f} per hari")
print("\n")