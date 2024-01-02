class Hewan:
    nama = ""
    makanan = ""
    hidup = ""
    berkembang_biak = ""
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print("Nama \t\t :", self.nama,
              "\nJenis Makanan \t :", self.makanan,
              "\nHidup \t\t :", self.hidup,
              "\nBerkembang Biak\t :", self.berkembang_biak)

class Badak(Hewan):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, jenis_hewan):
        super().__init__(nama, makanan, hidup, berkembang_biak)  
        self.bernafas = bernafas
        self.jenis_hewan = jenis_hewan

    def cetak(self):
        super().cetak()
        print("Bernafas\t :", self.bernafas, "\nJenis Hewan\t :", self.jenis_hewan,
              "\n========================================")

class Ikan(Hewan):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, jenis_hewan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.jenis_hewan = jenis_hewan

    def cetak(self):
        super().cetak()
        print("Bernafas\t :", self.bernafas, "\nJenis Hewan\t :", self.jenis_hewan, 
              "\n========================================")

class Ular(Hewan):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernafas, jenis_hewan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernafas = bernafas
        self.jenis_hewan = jenis_hewan

    def cetak(self):
        super().cetak()
        print("Bernafas\t :", self.bernafas, "\nJenis Hewan\t :", self.jenis_hewan, 
              "\n========================================")

x = Badak("Badak","Herbivora","di Darat","Vivipar(Melahirkan)", "Paru-paru", "Melata Besar")
x.cetak()

x = Ikan("Ikan Mas","Omnivora","di Air","Ovivar(Bertelur)", "Insang", "vertebrata")
x.cetak()

x = Ular("Kobra","Karnivora","di Darat","Ovovivipar(Bertelur & Melahirkan)", "Paru-paru", "Reptilia")
x.cetak()

