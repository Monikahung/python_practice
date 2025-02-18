# FORMAT STRING

# Contoh Generic
# string
nama = "Monika"
format_str = f"Hello {nama}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}" # otomatis dicasting menjadi str
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}" # otomatis dicasting menjadi str
print(format_str)

# bilangan bulat
angka = 100
format_str = f"bilangan bulat = {angka:d}" # d artinya bilangan bulat, tidak ditampilkan .0
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f"jutaan = {angka:,}" # tanda ',' untuk menunjukkan angka berordo ribuan
print(format_str)

# bilangan desimal
angka = 2005.598763
format_str = f"bilangan desimal = {angka:.3f}" # .3f (. menunjukkan desimal, 3f artinya 3 angka float)
print(format_str)

# menampilkan leading zero (angka 0 di depan)
angka = 2005.598763
format_str = f"bilangan = {angka:010.3f}" # 0 artinya angka 0 akan mengisi kekosongan yang ada di depan bilangan, 10 artinya angka yang bisa diisi berjumlah 10 (kalau kurang, maka akan kosong di depan), .3f artinya akan belakang desimal ada 3
print(format_str)

# menampilkan tanda positif (+) dan negatif (-)
angka_positif = 10.98765
angka_negatif = -10
format_positif = f"bilangan positif = {angka_positif:+010.3f}" # + untuk menampilkan tanda positif atau negatif, 010 untuk menampilkan leading zero, .3f untuk menampilkan angka float berjumlah 3 angka di belakang desimal
format_negatif = f"bilangan negatif = {angka_negatif:+d}" # + untuk menampilkan tanda positif atau negatif, d berarti bilangan bulat
print(format_positif)
print(format_negatif)

# memformat persen
persentase = 0.045
format_persen = f"persentase = {persentase:.2%}" # .2% artinya koma persen yang ditampilkan berjumlah 2 angka di belakang desimal persen (4.50%)
print(format_persen)

# melakukan operasi aritmatika di dalam tanda kurung kurawal {}
harga = 10000
jumlah = 5
hargaTotal = f"harga total = Rp {harga*jumlah:,.2f}" # tanda , berarti menggunakan koma untuk menunjukkan ordo ribuan, .2f untuk menampilkan float berjumlah 2 angka di belakang desimal
print(hargaTotal)

# memformat angka menjadi binary, octal, dan hexadecimal
angka = 115
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hexadecimal)