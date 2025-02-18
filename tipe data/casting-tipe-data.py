# Casting adalah mengubah dari satu tipe data ke tipe data lain
# tipe data = int, float, str, bool

# INTEGER
print("====INTEGER====")
data_int = 100
print("data : ", data_int, ", bertipe : ", type(data_int))

# casting ke float, str, dan bool
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan bernilai false jika nilai int = 0
print("data : ", data_float, ", bertipe : ", type(data_float))
print("data : ", data_str, ", bertipe : ", type(data_str))
print("data : ", data_bool, ", bertipe : ", type(data_bool))


# FLOAT
print("====FLOAT====")
data_float = 10.8
print("data : ", data_float, ", bertipe : ", type(data_float))

# casting ke int, str, dan bool
data_int = int(data_float) # angka float dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)
print("data : ", data_int, ", bertipe : ", type(data_int))
print("data : ", data_str, ", bertipe : ", type(data_str))
print("data : ", data_bool, ", bertipe : ", type(data_bool))


# STRING
print("====STRING====")
data_str = "1000"
print("data : ", data_str, ", bertipe : ", type(data_str))

# casting ke int, float, dan bool
data_int = int(data_str) # str yang akan diubah harus berupa angka
data_float = float(data_str) # str yang akan diubah harus berupa angka
data_bool = bool(data_str) # false jika str kosong (tidak ada isi)
print("data : ", data_int, ", bertipe : ", type(data_int))
print("data : ", data_float, ", bertipe : ", type(data_float))
print("data : ", data_bool, ", bertipe : ", type(data_bool))


# BOOLEAN
print("====BOOLEAN====")
data_bool = True
print("data : ", data_bool, ", bertipe : ", type(data_bool))

# casting ke int, float, dan str
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data : ", data_int, ", bertipe : ", type(data_int))
print("data : ", data_float, ", bertipe : ", type(data_float))
print("data : ", data_str, ", bertipe : ", type(data_str))