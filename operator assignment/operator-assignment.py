# OPERATOR ASSIGNMENT
# Operator yang dapat dilakukan dengan penyingkatan
# Operator tertentu + Assignment

# Nilai awal
a = 5 # ini dikenal dengan assignment
print("\nNilai:", a)

# OPERATOR ARITMATIKA + ASSIGNMENT
print("=====OPERATOR ARITMATIKA + ASSIGNMENT=====")
# Operator tambah (+=)
a += 1 # artinya a = a + 1
print("Nilai a += 1 adalah", a)

# Operator kurang (-=)
a -= 2 # artinya a = a - 2
print("Nilai a -= 2 adalah", a)

# Operator kali (*=)
a *= 5 # artinya a = a * 5
print("Nilai a *= 5 adalah", a)

# Operator bagi (/=)
a /= 2 # artinya a = a / 2
print("Nilai a /= 2 adalah", a)

# Operator eksponen (**=)
a **= 3 # artinya a = a ** 3
print("Nilai a **= 3 adalah", a)

# Operator modulus (%=)
a = 10
a %= 3 # artinya a = a % 3
print("Nilai a %= 3 adalah", a)

# Operator floor division (//=)
a = 10
a //= 3 # artinya a = a // 3
print("Nilai a //= 3 adalah", a)


# OPERATOR BITWISE + ASSIGNMENT
print("\n=====OPERATOR BITWISE + ASSIGNMENT=====")
# Operator OR (|=)
# Pertama
a = True
print("Nilai a adalah", a)
a |= False # artinya a = a | False
print("Nilai a |= False adalah", a)
# Kedua
a = False
print("Nilai a adalah", a)
a |= False # artinya a = a | False
print("Nilai a |= False adalah", a)

# Operator AND (&=)
# Pertama
a = True
print("Nilai a adalah", a)
a &= True # artinya a = a & True
print("Nilai a &= True adalah", a)
# Kedua
a = False
print("Nilai a adalah", a)
a &= True # artinya a = a & True
print("Nilai a &= True adalah", a)

# Operator XOR (^=)
# Pertama
a = True
print("Nilai a adalah", a)
a ^= True # artinya a = a ^ True
print("Nilai a ^= True adalah", a)
# Kedua
a = True
print("Nilai a adalah", a)
a ^= False # artinya a = a ^ False
print("Nilai a ^= False adalah", a)

# Operator Shift Right (>>=)
a = 0b0100
print("Nilai a =", a, ", dengan bit =", format(a, "04b"))
a >>= 2
print("Nilai a >>= 2 =", a, ", dengan bit =", format(a, "04b"))

# Operator Shift Left (<<=)
a = 0b0100
print("Nilai a =", a, ", dengan bit =", format(a, "04b"))
a <<= 1
print("Nilai a <<= 1 =", a, ", dengan bit =", format(a, "04b"))