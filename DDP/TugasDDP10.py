# Siswa yang lulus dari hasil_akhir
hasil_akhir = [
{"nama":"Reza", "nilai":70},
{"nama":"Ciut", "nilai":63},
{"nama":"Dian", "nilai":80},
{"nama":"Badu", "nilai":40}]
def mahasiswa_lulus(hasil_akhir):
    mahasiswa_lulus = [mahasiswa["nama"] for mahasiswa in hasil_akhir 
        if mahasiswa["nilai"] > 65]
    return mahasiswa_lulus
print(mahasiswa_lulus(hasil_akhir))


# Soal No. 1
nama_buah = ["Pepaya", "Mangga", "Pisang", "Durian", "Jambu"]
print("Nama Buah :", nama_buah)
reversed_buah = nama_buah[::-1]
for buah in nama_buah:
    reversed_buah =  reversed_buah
print("Kebalikan :", reversed_buah)


# Soal No. 2
nama_buah = ["Pepaya", "Mangga", "Pisang", "Durian", "Jambu"]
print("Daftar Buah :", nama_buah)
duplikasi = []
for buah in nama_buah:
    duplikasi += [buah]*2
print("Duplikat Buah :", duplikasi)


# Soal No. 3
def konsonan(kalimat):
    vocal = "aiueo"
    hasil = ""
    for huruf in kalimat:
        if huruf not in vocal:
            hasil += huruf 
    return hasil
print(konsonan("Nurul Fikri"))