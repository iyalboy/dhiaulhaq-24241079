# Input
kartu_member = input("Apakah Anda punya kartu member? (ya/tidak): ").strip().lower()
belanja = float(input("Masukkan total belanja Anda (Rp): "))

# variabel
diskon_persen = 0
diskon = 0

# Logika perhitungan diskon
if kartu_member == "ya":
    if belanja > 500000:
        diskon_persen = 0.2 * belanja  # Diskon 20% untuk member dengan belanja > 500rb
    else:
        diskon_persen = 0.1 * belanja # Diskon 10% untuk member dengan belanja <= 500rb
else:
    if belanja > 500000:
        diskon_persen = 0.05 * belanja # Diskon 5% untuk non-member dengan belanja > 500rb
    else:
        print("Maaf anda tidak dapat diskon :).") # Tidak ada diskon untuk non-member dengan belanja <= 500rb

# Menghitung nominal diskon dan total bayar
diskon = (diskon_persen / 100) * belanja
total_bayar = belanja - diskon

# Output hasil
print("\n===== Detail Transaksi =====")
print(f"Total Belanja : Rp{belanja:,.0f}")
print(f"Diskon Persen : {diskon_persen}%")
print(f"Diskon        : Rp{diskon:,.0f}")
print(f"Bayar         : Rp{total_bayar:,.0f}")
