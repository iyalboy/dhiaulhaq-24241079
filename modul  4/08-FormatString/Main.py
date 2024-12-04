# format string 

"""
   String : kumpulan dari karakter
   cara membuat string : 
   1. dengan single quote '...'
   2. dengan double quote "..."
"""
# membuat string dengan single quote
nama = 'Nama saya abi manyu'
print(nama)

# membuat string dengan double quote
nama = "Nama saya abi manyu"
print(nama)

print("Nama saya ma'ruf")
print("jangan lupa sholat jum'at")

# maksa harus single quote
# pakai tanda \
print('g\'day')
print('what\'sup')

print('c:\\user\\abi')

nama = "abi"
print("selamat datang", nama)

# format string
format_str = f'selamat datang {nama}'
print(format_str)

# format string angka
angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f'jutaan = {angka:,}'
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f'desimal = {angka:.3f}'
print(format_str)

# persen
angka = 0.55 # 0.55 * 100 = 55%
format_str = f'persen = {angka:.1%}'
print(format_str)

# operasi aritmatika dengan format string
harga = 57250
jumlah = 3

print(f'total bayar :{harga*jumlah:,}')