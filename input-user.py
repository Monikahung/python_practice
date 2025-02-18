# Episode input user

# data yang dimasukkan pasti string
data = input("Masukan data: ")

print("data =", data ,", type =", type(data))

# jika data yang dimasukkan ingin berupa int
data = int(input("Masukan angka integer: "))

print("data =", data, ", type =", type(data))

# jika data yang dimasukkan ingin berupa float
data = float(input("Masukan angka float: "))

print("data =", data, ", type =", type(data))

# jika data yang dimasukkan ingin berupa boolean, maka casting dulu ke int, kemudian ke boolean
biner = bool(int(input("Masukan nilai boolean: ")))

print("data =", biner, ", type =", type(biner))