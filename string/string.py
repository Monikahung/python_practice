# KONSEP
data = "Ini adalah string"
print(data)
print(type(data))

# 1. Cara Membuat String
print("\n=====CARA MEMBUAT STRING=====")
# a. Menggunakan single quote '...'
data = 'String menggunakan single quote'
print(data)
data = '"Halo, apa kabar?"'
print(data)

# b. Menggunakan double quote "..."
data = "String menggunakan double quote"
print(data)
data = "'Halo, apa kabar?'"
print(data)
data = "Hari ini adalah hari Jum'at"
print(data)

# 2. Menggunakan Tanda \
# a. Membuat tanda ' menjadi string (tambahkan tanda \ sebelum ')
print('Hari ini adalah hari Jum\'at')
print('g\'day, isn\'t it?')

# b. Membuat tanda \ menjadi string atau backlash (tambahkan tanda \ sekali lagi)
print("C:\\User\\Python")

# c. Membuat jarak menggunakan tab (gunakan tanda \t)
print("Monika\t\t\tMarcell, maka jaraknya semakin jauh")

# d. Menggunakan backspace (gunakan tanda \b)
print("Monika \bMarcell, maka jaraknya berdekatan")

# e. Membuat newline (baris baru)
print("Baris pertama.\nBaris kedua.") # LF -> Line Feed -> digunakan unix, macos, linux
print("Baris pertama.\rBaris kedua.") # CR -> Carriage Return -> digunakan commodore, acorn, lisp
print("Baris pertama.\r\nBaris kedua.") # CRLF -> Line Feed Carriage Return -> digunakan windows

# 3. String Literal atau Raw
# hati-hati
print('C:\new folder') # akan rumit jika ada banyak tanda \ yang ingin dijadikan string

# gunakan raw string
print(r'C:\new\t\n\b\\folder') # tambahkan r sebelum single double

# multiline literal string
print("""
Nama : Monika
Kelas : 1 TRPL A
""")

# multiline literal string dan raw
print(r"""
Nama : Monika
Kelas : 1 TRPL A/Semester 1
Website : www.monikahung.com\newID
""")