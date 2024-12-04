# operasi komparasi/perbandingan

# perhatikan 
"""
   bahwa hasil dari operasi komparasi
   selalu bertipe data boolean
   (true/false)
"""
# >, <, >=, <=, ==, !=, is, dan is not

a = 4
b = 2

# lebih dari >
print("===Lebih dari (>)")
hasil = a > 3 # TRUE 
print(a, ">", 3, "=", hasil)
hasil = b > 3 # FALSE
print(b, ">", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

# kurang dari <
print("===kurang dari (<)")
hasil = a < 3 # TRUE 
print(a, "<", 3, "=", hasil)
hasil = b < 3 # FALSE
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

# lebih dari sama dengan >=
print("===lebih dari sama dengan (>=)")
hasil = a >= 3 # TRUE 
print(a, ">=", 3, "=", hasil)
hasil = b >= 3 # FALSE
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)

# kurang dari sama dengan <=
print("===kurang dari sama dengan (<=)")
hasil = a <= 3 # TRUE 
print(a, "<=", 3, "=", hasil)
hasil = b <= 3 # FALSE
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

# sama dengan ==
print("===sama dengan (==)")
hasil = a == 3 # TRUE 
print(a, "==", 3, "=", hasil)
hasil = b == 3 # FALSE
print(b, "==", 3, "=", hasil)
hasil = b == 2
print(b, "==", 2, "=", hasil)

# tidak sama dengan !=
print("===tidak sama dengan (!=)")
hasil = a != 3 # TRUE 
print(a, "!=", 3, "=", hasil)
hasil = b != 3 # FALSE
print(b, "!=", 3, "=", hasil)
hasil = b != 2
print(b, "!=", 2, "=", hasil)