# SOAL
# Suatu universitas di Semarang ingin dibuatkan suatu program untuk melakukan pembayaran uang kuliah dan pendaftaran perkuliahan. Pembayaran akan dilakukan sesuai dengan jalur yang telah dipilih. Pilihan pendaftaran kelas sebagai berikut.
    # 1. Reguler
    # 2. Non Reguler
    # 3. Non Reguler Sabtu Minggu
# Kemudian setelah melakukan inputan berupa pilihan pendaftaran kelas, program akan menginputan prodi, sementara prodi yang tersedia hanya TI dan SI dengan kriteria:
    # Jika pilihan [1] dan prodi [TI] maka biaya kuliah Rp 3.0000.000, dan jika [SI] biaya kuliah Rp 2.500.000.
    # Jika pilihan [2] dan prodi [TI] maka biaya kuliah Rp 2.500.000, dan jika [SI] biaya kuliah Rp 2.000.000.
    # Jika pilihan [3] dan prodi [TI] maka biaya kuliah Rp 2.000.000, dan jika [SI] biaya kuliah Rp 1.500.000.
# Output yang diharapkan hanya berupa jumlah uang kuliah yang harus dibayar!

# PROGRAM
print("\n" + 5*"=" + "Program Pendaftaran dan Biaya Kuliah" + 5*"=" + "\n")
print("""Pilihan Pendaftaran Kelas:
1. Reguler
2. Non Reguler
3. Non Reguler Sabtu Minggu""")
jalurPendaftaran = int(input("Masukan pilihan pendaftaran anda (1/2/3): "))

print("""
Pilihan Prodi:
1. TI
2. SI""")
prodi = int(input("Masukan pilihan prodi anda (1/2): "))

print("\n" + 50*"=" + "\n")

if jalurPendaftaran == 1:
    if prodi == 1:
        biayaKuliah = 3000000
        print(f"Biaya kuliah untuk prodi TI jalur Reguler adalah Rp {biayaKuliah:,.2f}")
    elif prodi == 2:
        biayaKuliah = 2500000
        print(f"Biaya kuliah untuk prodi SI jalur Reguler adalah Rp {biayaKuliah:,.2f}")
    else:
        print("Kode prodi yang anda masukan tidak terdeteksi")
elif jalurPendaftaran == 2:
    if prodi == 1:
        biayaKuliah = 2500000
        print(f"Biaya kuliah untuk prodi TI jalur Non Reguler adalah Rp {biayaKuliah:,.2f}")
    elif prodi == 2:
        biayaKuliah = 2000000
        print(f"Biaya kuliah untuk prodi SI jalur Non Reguler adalah Rp {biayaKuliah:,.2f}")
    else:
        print("Kode prodi yang anda masukan tidak terdeteksi")
elif jalurPendaftaran == 3:
    if prodi == 1:
        biayaKuliah = 2000000
        print(f"Biaya kuliah untuk prodi TI jalur Non Reguler Sabtu Minggu adalah Rp {biayaKuliah:,.2f}")
    elif prodi == 2:
        biayaKuliah = 1500000
        print(f"Biaya kuliah untuk prodi SI jalur Non Reguler Sabtu Minggu adalah Rp {biayaKuliah:,.2f}")
    else:
        print("Kode prodi yang anda masukan tidak terdeteksi")
else:
    print("Kode yang anda masukan tidak terdeteksi")