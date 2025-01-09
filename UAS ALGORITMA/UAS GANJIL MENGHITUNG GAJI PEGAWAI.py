def hitung_gaji():
    print("=== Program Penghitungan Gaji ===")
    
    # Input data pegawai
    nama = input("Masukkan Nama Pegawai: ")
    status = input("Masukkan Status Kepegawaian (Tetap/Tidak Tetap): ").lower()
    gaji_pokok = float(input("Masukkan Gaji Pokok: "))
    durasi_lembur = float(input("Masukkan Durasi Lembur (dalam jam): "))
    
    # Hitung berdasarkan status pegawai
    if status == "tetap":
        tunjangan = 0.7 * gaji_pokok
        uang_lembur = 0.1 * gaji_pokok * durasi_lembur
        gaji_bersih = gaji_pokok + tunjangan + uang_lembur
    elif status == "tidak tetap":
        tunjangan = 0
        uang_lembur = 0.05 * gaji_pokok * durasi_lembur
        gaji_bersih = gaji_pokok + uang_lembur
    else:
        print("Status kepegawaian tidak valid!")
        return
    
    # Tampilkan hasil
    print("\n=== Slip Gaji ===")
    print(f"Nama Pegawai   : {nama}")
    print(f"Status         : {'Tetap' if status == 'tetap' else 'Tidak Tetap'}")
    print(f"Gaji Pokok     : Rp{gaji_pokok:,.2f}")
    print(f"Tunjangan      : Rp{tunjangan:,.2f}")
    print(f"Uang Lembur    : Rp{uang_lembur:,.2f}")
    print(f"Gaji Bersih    : Rp{gaji_bersih:,.2f}")

# Jalankan program
hitung_gaji()
