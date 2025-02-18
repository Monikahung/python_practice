# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan yang tidak ada koma (integer)
data_integer = 1
print(type(data_integer))
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data: Angka dengan koma (float)
data_float = 1.5
print(type(data_float))
print("data : ", data_float, ", bertipe : ", type(data_float))

# tipe data: Kumpulan karakter (string)
data_string = "Monika 08"
print(type(data_string))
print("data : ", data_string, ", bertipe : ", type(data_string))

# tipe data: Biner true/false (boolean)
data_bool = True
print(type(data_bool))
print("data : ", data_bool, ", bertipe : ", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print(type(data_complex))
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10, 5)
print(type(data_c_double))
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))