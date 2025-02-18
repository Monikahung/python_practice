# SOAL
# Buatlah sebuah sistem kasir pada perusahaan boneka. Spesifikasi yang dibutuhkan yaitu program dapat menghitung potongan harga dari pembelian boneka, dengan kriteria:
    # Jika pelanggan membeli 1-12 boneka, harga per boneka Rp 20.000,00.
    # Jika pelanggan membeli 13-24 boneka, harga per boneka Rp 19.500,00.
    # Jika pelanggan membeli 25-50 boneka, harga per boneka Rp 18.000,00.
    # Jika pelanggan membeli lebih dari 50 boneka, harga per boneka Rp 17.000,00.
# Input program berupa nama pembeli dan jumlah boneka yang dibeli. Hasil output yang diinginkan berupa nama pembeli, jumlah boneka yang dibeli, dan total harga yang harus dibayar oleh pembeli setelah mendapatkan potongan harga.

# PROGRAM
print("\n" + 5*"=" + "Program Harga Boneka" + 5*"=" + "\n")

namaPembeli = input("Masukan nama anda: ")
jumlahBoneka = int(input("Masukan jumlah boneka yang dibeli: "))

if jumlahBoneka <= 12:
    harga = jumlahBoneka * 20000
    print("\n" + 50*"=")
    print(f"Nama pembeli: {namaPembeli}")
    print(f"Jumlah boneka: {jumlahBoneka}")
    print(f"Total harga: Rp {harga:,.2f}")
elif jumlahBoneka <= 24:
    harga = jumlahBoneka * 19500
    print("\n" + 50*"=")
    print(f"Nama pembeli: {namaPembeli}")
    print(f"Jumlah boneka: {jumlahBoneka}")
    print(f"Total harga: {harga:,.2f}")
elif jumlahBoneka <= 50:
    harga = jumlahBoneka * 18000
    print("\n" + 50*"=")
    print(f"Nama pembeli: {namaPembeli}")
    print(f"Jumlah boneka: {jumlahBoneka}")
    print(f"Total harga: {harga:,.2f}")
else:
    harga = jumlahBoneka * 17000
    print("\n" + 50*"=")
    print(f"Nama pembeli: {namaPembeli}")
    print(f"Jumlah boneka: {jumlahBoneka}")
    print(f"Total harga: {harga:,.2f}")