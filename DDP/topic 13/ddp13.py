class Orang:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def makan(self):
        print("saya bisa makan")

    def cetak(self):
        print("Nama saya ",self.fname,self.lname)

class Mahasiswa(Orang):
    def __init__(self, fname, lname,prodi,angkatan):
        super().__init__(fname, lname)
        self.prodi = prodi
        self.angkatan = angkatan

    def cetak(self):
        super().cetak()
        print("saya prodi",self.prodi, "angkatan",self.angkatan)

class Pegawai(Orang):
    def bekerja(self):
        print("saya bekerja")

x = Orang("Anto","Budi")
x.cetak()
# x.bekerja()

y = Mahasiswa("Dwi","Astuti","Teknik Informatika",2023)
y.cetak()
y.makan()
# y.print()

agus = Pegawai("Agus","Rahmat")
agus.bekerja()