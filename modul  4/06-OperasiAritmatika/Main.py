# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi kurang -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi Modulasi % (bagi sisa)
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

# operasi exponen **
hasil = a ** b
print(a, "**", b, "=", hasil)

# prioritas operasi aritmatika

"""
   1. ()
   2. *,**, /, %, //
   3. +, -
"""

x = 3
y = 2
z = 4

hasil = x**y * (z + x) / y - y % z // x
print(hasil)