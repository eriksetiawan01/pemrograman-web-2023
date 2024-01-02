print("1 = Luas Trapesium")
print("2 = Keliling Trapesium")
Pilihan = int(input("Masukan Pilihan 1 or 2 : "))
Luas = "Luas Trapesium"
Keliling = "Keliling Trapesium"

match Pilihan :
    case 1 :
        print(Luas)
        sisi_atas = float(input("Masukkan panjang sisi atas trapesium: "))
        sisi_bawah = float(input("Masukkan panjang sisi bawah trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
        print(f"Luas trapesium adalah: {luas}")

    case 2 :
        print(Keliling)
        sisi_atas = float(input("Masukkan panjang sisi atas trapesium: "))
        sisi_bawah = float(input("Masukkan panjang sisi bawah trapesium: "))
        sisi_kiri = float(input("Masukkan panjang sisi kiri trapesium: "))
        sisi_kanan = float(input("Masukkan panjang sisi kanan trapesium: "))
        keliling = sisi_atas + sisi_bawah + sisi_kiri + sisi_kanan
        print(f"Keliling trapesium adalah: {keliling}")