# OPERASI LOGIKA ATAU BOOLEAN

# not, or, and, xor

# Operator not
# Operator ini dikenal dengan negasi/ingkaran, yang mana nilainya kebalikan dari nilai sebenarnya
print("\n========== OPERATOR NOT ==========")
a = True
c = not a
print("a =", a)
print("========== NOT")
print("c =", c)
print("==============")
a = False
c = not a
print("a =", a)
print("========== NOT")
print("c =", c)

# Operator or
# Operator ini dikenal dengan disjungsi, yang mana bernilai benar/true jika salah satu bernilai benar/true maupun keduanya bernilai benar/true
print("\n========== OPERATOR OR ==========")
a = True
b = True
c = a or b
print("a =", a)
print("b =", b)
print("a or b =", c)
print("==============")
a = True
b = False
c = a or b
print("a =", a)
print("b =", b)
print("a or b =", c)
print("==============")
a = False
b = True
c = a or b
print("a =", a)
print("b =", b)
print("a or b =", c)
print("==============")
a = False
b = False
c = a or b
print("a =", a)
print("b =", b)
print("a or b =", c)
print("==============")

# Operator and
# Operator ini dikenal dengan konjungsi, yang mana bernilai benar/true jika keduanya bernilai benar/true
print("\n========== OPERATOR AND ==========")
a = True
b = True
c = a and b
print("a =", a)
print("b =", b)
print("a and b =", c)
print("==============")
a = True
b = False
c = a and b
print("a =", a)
print("b =", b)
print("a and b =", c)
print("==============")
a = False
b = True
c = a and b
print("a =", a)
print("b =", b)
print("a and b =", c)
print("==============")
a = False
b = False
c = a and b
print("a =", a)
print("b =", b)
print("a and b =", c)
print("==============")

# Operator xor
# Bernilai benar/true jika salah satunya bernilai benar/true
print("\n========== OPERATOR XOR ==========")
a = True
b = True
c = a ^ b
print("a =", a)
print("b =", b)
print("a xor b =", c)
print("==============")
a = True
b = False
c = a ^ b
print("a =", a)
print("b =", b)
print("a xor b =", c)
print("==============")
a = False
b = True
c = a ^ b
print("a =", a)
print("b =", b)
print("a xor b =", c)
print("==============")
a = False
b = False
c = a ^ b
print("a =", a)
print("b =", b)
print("a xor b =", c)
print("==============")