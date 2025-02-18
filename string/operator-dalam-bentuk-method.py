# OPERATOR DALAM BENTUK METHOD

## Mengubah case dari string
# Mengubah semua ke upper case (huruf kapital)
salam = "bro"
print("Normal = " + salam)
salam = salam.upper()
print("Upper = " + salam)

# Mengubah semua ke lower case (huruf kecil)
sapaan = "Aku kece ABIEEZZZZZ"
print("Normal = " + sapaan)
sapaan = sapaan.lower()
print("Lower = " + sapaan)

data = "JANJI DIA SEMANIS MADU"
print("Normal = " + data)
data = data.casefold()
print("Casefold = " + data)

# Mengubah huruf pertama pada kata/kalimat menjadi huruf kapital
judul = "janji dia semanis madu"
print("Normal = " + judul)
judul = judul.capitalize() # huruf 'j' pada kata janji akan menjadi kapital
print("Capitalize = " + judul)
#---------------------------------------------------#


## Pengecekan dengan isX method
# Pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + " is lower = " + str(apakah_lower))

# Pengecekan upper case
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() -> untuk mengecek semuanya huruf
data = "Halo semuanya, apa kabar?" # hasilnya boolean False karena terdapat spasi dan tanda tanya
periksa = data.isalpha()
print(data + " is alpha = " +str(periksa))

# isalnum() -> untuk mengecek huruf dan angka
data = "Halo123456789"
periksa = data.isalnum() # hasilnya boolean True
print(data + " is alnum = " + str(periksa))

# isdecimal() -> untuk mengecek angka
data = "119"
periksa = data.isdecimal() # hasilnya boolean True
print(data + " is decimal = " + str(periksa))

# isspace() -> mengecek spasi, tab, dan newline
data = "\n\t"
periksa = data.isspace() # hasilnya boolean True
print(data + " is space = " + str(periksa))

# istitle() -> mengecek semua kata dimulai dengan huruf kapital
judul = "It Is Okay To Be Orkay"
cek_judul = judul.istitle() # hasilnya boolean (True)
print(judul + " is title = " + str(cek_judul))

judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya boolean (False)
print(judul + " is title = " + str(cek_judul))
#---------------------------------------------------#


## Mengecek komponen startswith() endswith()
cek_start = "Halo Semuanya".startswith("Halo") # artinya kita ingin mengecek apakah string "Halo Semuanya" dimulai dengan string "Halo"
print("start = " + str(cek_start))

cek_end = "Halo Semuanya".endswith("Semuanya") # artinya kita ingin mengecek apakah string "Halo Semuanya" diakhiri dengan string "Semuanya"
print("end = " + str(cek_end))
#---------------------------------------------------#


## Penggabungan komponen join() split()
dataPisah = ['aku', 'kamu', 'dia'] # dalam bentuk list
gabungan = ','.join(dataPisah) # untuk menggabungkan string dengan tanda ','
print(dataPisah)
print(gabungan)

gabungan = ' '.join(dataPisah) # untuk menggabungkan string dengan tanda spasi
print(gabungan)

dataGabungan = "aku kamu dia"
print(dataGabungan.split(' ')) # untuk mengembalikan bentuk string menjadi bentuk list
#---------------------------------------------------#


## Mengubah karakter pada string menggunakan replace()
data = "Hello World!"
perubahan = data.replace("World", "Dunia")
print(perubahan) # outputnya: Hello Dunia!
#---------------------------------------------------#


## Alokasi karakter rjust(), ljust(), center()
# rjust() -> membuat string menjadi rata ke kanan
kanan = "Monika".rjust(20)
print("'" + kanan + "'")

# ljust() -> membuat string menjadi rata ke kiri
kiri = "Monika".ljust(20, "=") # bisa ditambahkan argumen untuk mengisi spasi
print("'" + kiri + "'")

# center() -> membuat string berada di tengah
tengah = "Monika".center(20, "-")
print("'" + tengah + "'")

# kebalikannya -> strip()
tengah = tengah.strip("-") # tanda "-" akan hilang
print("'" + tengah + "'")

kanan = kanan.strip() # tanda spasi yang berada di sebelah kiri string akan hilang
print("'" + kanan + "'")
#---------------------------------------------------#