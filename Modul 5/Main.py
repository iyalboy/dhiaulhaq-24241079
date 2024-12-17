def check_discount():
    # Menanyakan apakah pelanggan memiliki kartu member
    kartu_member = input("Apakah Anda punya kartu member? (ya/tidak): ").strip().lower()

    if kartu_member == "ya":
        # Menanyakan total belanjaan
        total_belanja = float(input("Berapa total belanjaan Anda? (dalam rupiah): "))

        if total_belanja > 500000:
            print("Anda mendapatkan diskon 50 ribu!")
            total_belanja -= 50000
        elif total_belanja > 100000:
            print("Anda mendapatkan diskon 15 ribu!")
            total_belanja -= 15000
        else:
            print("Anda tidak mendapatkan diskon.")

    elif kartu_member == "tidak":
        # Menanyakan total belanjaan
        total_belanja = float(input("Berapa total belanjaan Anda? (dalam rupiah): "))

        if total_belanja > 100000:
            print("Anda mendapatkan diskon 10 ribu!")
            total_belanja -= 10000
        else:
            print("Anda tidak mendapatkan diskon.")

    else:
        print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
        return

    print(f"Total belanjaan setelah diskon: {total_belanja:.2f} rupiah")

# Menjalankan fungsi
check_discount()
