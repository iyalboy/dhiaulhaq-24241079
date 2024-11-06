# input bilangan 
angka = int(input("masukkan bilangan: "))

# cek ganjil atau genap 
# f = formatted string berfungsi untuk menyisipkan variabel langsung ke dalam string dengan cara yang lebih sederhana 
if angka % 2 == 0: 
    print (f"{angka} adalah bilangan genap")
else:
     print(f"{angka} adalah bilangan ganjil")
