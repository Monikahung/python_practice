from sympy import symbols, integrate, sympify

# Mendefinisikan variabel simbolik
x = symbols('x')

# Meminta pengguna untuk memasukkan fungsi integral
input_fungsi = input("Masukkan fungsi integral (gunakan x sebagai variabel): ")

# Mengonversi input pengguna menjadi ekspresi simbolik
fungsi = sympify(input_fungsi)

# Menghitung integral dari fungsi tersebut
hasil_integral = integrate(fungsi, x)

# Menampilkan hasil integral
print("Hasil integral dari fungsi {} adalah: {}".format(fungsi, hasil_integral))