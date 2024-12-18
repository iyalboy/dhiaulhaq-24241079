
def check_discount():
    # Menanyakan apakah pelanggan memiliki kartu member
    kartu_member = input("Apakah Anda punya kartu member? (ya/tidak): ").strip().lower()

    if kartu_member == "ya":
        # Menanyakan total belanjaan
        total_belanja = float(input("Berapa total belanjaan Anda? (dalam rupiah): "))

        if total_belanja > 500000:
            diskon = 0.2 * total_belanja
            print(f"Anda mendapatkan diskon Rp. {diskon}")
        elif total_belanja <= 500000:
            diskon = 0.1 * total_belanja
            print(f"Anda mendapatkan diskon Rp. {diskon}")
        else:
            print("Anda tidak mendapatkan diskon.")

    elif kartu_member == "tidak":
        # Menanyakan total belanjaan
        total_belanja = float(input("Berapa total belanjaan Anda? (dalam rupiah): "))

        if total_belanja > 100000:
            diskon = 0.05 * total_belanja
            print(f"Anda mendapatkan diskon Rp. {diskon}")
        else:
            print("Anda tidak mendapatkan diskon.")

    else:
        print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
        return

    print(f"Total belanjaan setelah diskon: {total_belanja-diskon:.2f} rupiah")

# Menjalankan fungsi
check_discount()
