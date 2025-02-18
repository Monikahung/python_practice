# Operator Aritmatika
a = 10
b = 3

# Operator Standar

# operator tambah (+)
hasil = a + b
print(a, '+', b, '=', hasil)

# operator kurang (-)
hasil = a - b
print(a, '-', b, '=', hasil)

# operator kali (*)
hasil = a * b
print(a, '*', b, '=', hasil)

# operator bagi (/)
hasil = a / b
print(a, '/', b, '=', hasil)

# operator eksponen/pangkat (**)
hasil = a ** b
print(a, '**', b, '=', hasil)

# operator modulus/sisa hasil bagi (%)
hasil = a % b
print(a, '%', b, '=', hasil)

# operator floor division (//)
hasil = a // b
print(a, '//', b, '=', hasil)


# Prioritas Operasi, Operational Precedence
# ( ) -> ** -> *, /, %, // -> +, -
# tanda kurung -> eksponen -> kali, bagi, modulus, floor division -> tambah, kurang

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, '=', hasil)

hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, '=', hasil)