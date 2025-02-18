# PROGRAM MENAMPILKAN PERKALIAN
print("\n" + 5*"=" + "Program Menampilkan Perkalian" + 5*"=" +"\n")

angkaPerkalian = int(input("Masukan perkalian ke: "))
sampaiPerkalian = int(input("Masukan batas perkalian: "))

i = 1
while i <= sampaiPerkalian:
    print(f"{angkaPerkalian} * {i} = {angkaPerkalian * i}")
    i += 1