# Deklarasi Fungsi
def hello() :
    print("hello saya adalah STT Terpadu Nurul Fikri")
    print("saya prodi Teknik Informatika") 

# Memanggil Fungsi
hello()
hello()

def panggil():
    hello()
    print("saya kelas ti 04")

# Memanggil Fungsi
panggil()

def say(nama, prodi = "TI"):
    print("hello nama saya adalah", nama)
    print("prodi saya adalah", prodi)


# Memanggil Fungsi
say("ahmad", "SI")
say("erik", "TI")
say("budi")



def jumlah(angka1, angka2):
    print("Hasilnya adalah",angka1+angka2 )

# Memanggil Fungsi
jumlah(3,5)


def luasPersegi(sisi):
    return sisi * sisi

sisi = int(input("Masukkan sisi: "))
print(luasPersegi(sisi))