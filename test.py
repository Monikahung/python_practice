import time
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

print("Hello Everyone")
# kesimpulan: baris kosong tidak diterjemahkan oleh python

# ini adalah comment

a = 10 # ini adalah comment juga
"""ini adalah
comment multiline"""
print(a)

print(time.time() - start_time, "detik")


# kita bisa mengcompile python ke yang namanya bytecode
# cara mengcompile, buka terminal dan tuliskan python -m py_compile test.py