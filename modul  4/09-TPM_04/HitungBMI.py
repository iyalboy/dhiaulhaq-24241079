# menghitung BMI

# input data tetap
# Data tetap
berat = 55 # berat badan dalam kilogram
tinggi = 171 # tinggi badan dalam sentimeter

# Mengonversi tinggi dari cm ke meter
tinggi = tinggi / 100

#menghitung BMI
bmi = berat / (tinggi ** 2)

# menentukan kategori BMI
if bmi < 18.5:
    kategori = "kekurangan berat badan"
elif 18.5 <= bmi < 24.9:
    kategori = "normal"
elif 25 <= bmi < 29.9:
    kategori = "kelebihan berat badan"
else:
    kategori = "obesitas"

# menampilkan hasil
print(f"scor BMI anda adalah: {bmi:.2f}")
print(f"kategori: {kategori}") 
   