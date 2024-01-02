class Gempa:
    lokasi = ""
    skala = "0"

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Tempat :", self.lokasi, "\nSkala :", self.skala,"\nDampak gempa : tidak terasa\n==============================")
        elif 2 <= self.skala < 4:
            print("Tempat :", self.lokasi, "\nSkala :", self.skala, "\nDampak gempa : bangunan retak-retak\n==============================")
        elif 4 <= self.skala < 6:
            print("Tempat :", self.lokasi, "\nSkala :", self.skala, "\nDampak gempa : bangunan roboh\n==============================")
        else:
            print("Tempat :", self.lokasi, "\nSkala :", self.skala, "\nDampak gempa : bangunan roboh dan berpotensi tsunami\n==============================")
