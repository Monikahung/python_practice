# Operator Bitwise, Operasi Biner, Binary

# or, and, xor, not, shift right, shift left

a = 9
b = 5

# Bitwise OR (|)
print("\n==========OR==========")
c = a | b
print("Nilai:", a, ", dengan bilangan biner:", format(a, "08b")) # 0 artinya dimulai dari 0, 8 berarti jumlah bilangan biner, b artinya jenis bilangannya yaitu biner
print("Nilai:", b, ", dengan bilangan biner:", format(b, "08b"))
print("----------------------------------------------OR(|)") # operator or ini konsepnya sama seperti operator or pada logika
print("Nilai:", c, ", dengan bilangan biner:", format(c, "08b"))

# Bitwise AND (&)
print("\n==========AND==========")
c = a & b
print("Nilai:", a, ", dengan bilangan biner:", format(a, "08b"))
print("Nilai:", b, ", dengan bilangan biner:", format(b, "08b"))
print("----------------------------------------------AND(&)")
print("Nilai:", c, ", dengan bilangan biner:", format(c, "08b"))

# Bitwise XOR (^)
print("\n==========XOR==========")
c = a ^ b
print("Nilai:", a, ", dengan bilangan biner:", format(a, "08b"))
print("Nilai:", b, ", dengan bilangan biner:", format(b, "08b"))
print("----------------------------------------------XOR(^)")
print("Nilai:", c, ", dengan bilangan biner:", format(c, "08b"))

# Bitwise NOT (~)
print("\n==========NOT==========")
c = ~a
print("Nilai:", a, ", dengan bilangan biner:", format(a, "08b"))
print("----------------------------------------------NOT(~)")
print('Nilai:', c, ", dengan bilangan biner:", format(c, "08b"))
# jika ingin kebalikan dari nilai bilangan biner (0 -> 1, 1 -> 0)
d = 0b00001001 # untuk menjabarkan bilangan biner
e = 0b11111111
print("----------------------------------------------KEBALIKAN BILANGAN BINER")
print("Nilai:", d^e, ", dengan bilangan biner:", format(d^e, "08b"))

# Shift RIGHT (Menggeser nilai bit/bilangan biner ke kanan)
print("\n==========SHIFT RIGHT==========")
c = a >> 2 # artinya menggeser bilangan biner dari a ke kanan sebanyak 2 kali
print("Nilai:", a, ", dengan bilangan biner:", format(a, "08b"))
print("----------------------------------------------SHIFT RIGHT(>>)")
print('Nilai:', c, ", dengan bilangan biner:", format(c, "08b"))

# Shift LEFT (Menggeser nilai bit/bilangan biner ke kiri)
print("\n==========SHIFT LEFT==========")
c = a << 2 # artinya menggeser bilangan biner dari a ke kiri sebanyak 2 kali
print("Nilai:", a, ", dengan bilangan biner:", format(a, "08b"))
print("----------------------------------------------SHIFT LEFT(<<)")
print('Nilai:', c, ", dengan bilangan biner:", format(c, "08b"))