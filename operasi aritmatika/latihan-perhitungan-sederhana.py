# LATIHAN KONVERSI SATUAN TEMPERATURE

print("\nProgram Python Konversi Suhu\n")
# Program Konversi Suhu dari Celcius ke Suhu Lainnya
celcius = float(input("Masukan suhu dalam satuan Celcius: "))
print("Suhu: ", celcius, "Celcius")

# reamur
reamur = (4/5)*celcius
print("Suhu dalam Reamur: ", reamur, "Reamur")
# fahrenheit
fahrenheit = ((9/5)*celcius)+32
print("Suhu dalam Fahrenheit: ", fahrenheit, "Fahrenheit")
# kelvin
kelvin = celcius+273
print("Suhu dalam Kelvin: ", kelvin, "Kelvin")

print("\n")

# Program Konversi Suhu dari Reamur ke Suhu Lainnya
reamur = float(input("Masukan suhu dalam satuan Reamur: "))
print("Suhu: ", reamur, "Reamur")

# celcius
celcius = (5/4)*reamur
print("Suhu dalam Celcius: ", celcius, "Celcius")
# fahrenheit
fahrenheit = ((9/4)*reamur)+32
print("Suhu dalam Fahrenheit: ", fahrenheit, "Fahrenheit")
# kelvin
kelvin = ((5/4)*reamur)+273
print("Suhu dalam Kelvin: ", kelvin, "Kelvin")

print("\n")

# Program Konversi Suhu dari Fahrenheit ke Suhu Lainnya
fahrenheit = float(input("Masukan suhu dalam satuan Fahrenheit: "))
print("Suhu: ", fahrenheit, "Fahrenheit")

# celcius
celcius = (5/9)*(fahrenheit-32)
print("Suhu dalam Celcius: ", celcius, "Celcius")
# reamur
reamur = (4/9)*(fahrenheit-32)
print("Suhu dalam Reamur: ", reamur, "Reamur")
# kelvin
kelvin = ((5/9)*(fahrenheit-32))+273
print("Suhu dalam Kelvin: ", kelvin, "Kelvin")

print("\n")

# Program Konversi Suhu dari Kelvin ke Suhu Lainnya
kelvin = float(input("Masukan suhu dalam satuan Kelvin: "))
print("Suhu: ", kelvin, "Kelvin")

# celcius
celcius = kelvin-273
print("Suhu dalam Celcius: ", celcius, "Celcius")
# reamur
reamur = (4/5)*(kelvin-273)
print("Suhu dalam Reamur: ", reamur, "Reamur")
# fahrenheit
fahrenheit = ((9/5)*(kelvin-273))+32
print("Suhu dalam Fahrenheit: ", fahrenheit, "Fahrenheit")