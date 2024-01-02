# Soal NO. 1
# Deklarasi Fungsi
def profil(nama, alamat, gender, umur, hoby):
    print("Nama Lengkap :", nama)
    print("Alamat :", alamat)
    print("Jenis Kelamin :", gender)
    print("Umur :", umur)
    print("Hobi :", hoby)

# Memanggil Fungsi
profil("Erik Setiawan", "Bogor", "Laki-laki", 19, "Swimming")


# Soal No. 2
def kelulusan(n):
    if n <=60:
        print("Gagal")
    elif n >= 61 and n <= 70:
        print("Baik")
    elif n >= 71 and n <= 80:
        print("Sangat Baik")
    elif n >= 81 and n <= 100:
        print("Istimewa")
kelulusan(int(input("Masukan Angka :")))


# Soal NO. 3
def bilangan(n):
    for n in range(1, n, 2):
        print(n)
bilangan(int(input("Masukan Bilangan:")))