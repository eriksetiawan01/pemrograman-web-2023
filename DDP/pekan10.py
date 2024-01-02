# nilai = [65, 60, 75, 0, 98]

# print(nilai[-1])

# nilai = [65, 60, 75, 0, 98]
# nilai.append(80)
# print(nilai)

# nilai = [65, 60, 75, 0, 98]
# nilai.pop()
# print(nilai)

# nilai = {65, 60, 75, 0, 98}
# nilai.add(50)
# print(nilai)


# nilai = {65, 60, 75, 0, 98}
# nilai.remove(65)
# print(nilai)


# set1 = {1, 2, 3}
# set2 = {2, 4, 6}
# set3 = set1.union(set2)
# print(set3)

# set1 = {1, 2, 3}
# set2 = {2, 4, 6}
# set1.update(set2)
# print(set1)

# data_diri = {
# "nama":"Reza",
# "matpel":"DDP"}
# data_diri["semester"] = 1
# print(data_diri["nama"])

# data_diri = {
# "nama":"Reza",
# "matpel":"DDP"}
# data_diri["nama"]="anam"
# print(data_diri["nama"])

# data_diri = {
# "nama":"Reza",
# "matpel":"DDP"}
# data_diri["alamat"]="depok"
# print(data_diri)

# data_diri = {
# "nama":"Reza",
# "matpel":"DDP"}
# data_diri["alamat"]="depok"
# data_diri.pop("alamat")
# print(data_diri)

# data_diri = {
# "nama":"Reza",
# "matpel":"DDP"}
# data_diri["alamat"]="depok"


# keluarga = {"nama" : "joko", "anaknya" : ['ani', 'ina', 'ini']}
# print(keluarga)

# hasi_akhir = [
#     {"nama" : "erik", "nilai" : 85},
#     {"nama" : "virgi", "nilai" : 90},
#     {"nama" : "dian", "nilai" : 70},
#     {"nama" : "badu", "nilai" : 60}
# ]
# print(hasi_akhir)

# hasi_akhir = [
#     {"nama" : "erik", "nilai" : 85},
#     {"nama" : "virgi", "nilai" : 90},
#     {"nama" : "dian", "nilai" : 70},
#     {"nama" : "badu", "nilai" : 60}
# ]
# print(hasi_akhir[0])

# hasi_akhir = [
#     {"nama" : "erik", "nilai" : 85},
#     {"nama" : "virgi", "nilai" : 90},
#     {"nama" : "dian", "nilai" : 70},
#     {"nama" : "badu", "nilai" : 60}
# ]
# print(hasi_akhir[0]["nama"])

# hasi_akhir = [
#     {"nama" : "erik", "nilai" : 85},
#     {"nama" : "virgi", "nilai" : 90},
#     {"nama" : "dian", "nilai" : 70},
#     {"nama" : "badu", "nilai" : 60}
# ]
# print(hasi_akhir[1]["nilai"])

# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# print(daftar_buah[-1])
      
# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# print(daftar_buah[1:3])

# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# print(daftar_buah[:3])

# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# print(daftar_buah[:])

# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# print(daftar_buah[0:5:2])

# #soal no. 1 
# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# print(daftar_buah[::-1])

# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# for buah in daftar_buah :
#     print(buah)

# x = str(input("Masukan Data :" ))
# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# if x in daftar_buah:
#     print(x, "ada di list")
# else :
#     print("semangka tidak ada")

# Soal no. 2
# list_buah = []
# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# for buah in daftar_buah:
#     list_buah = list_buah + [buah]*2
# print(list_buah)

# data_diri = {
#     "nama":"reza",
#     "alamat":"depok"
# }

# for x in data_diri.values():
#     print(x)

# daftar_buah = ["semangka", "durian", "nanas", "apel", "pisang"]
# hasil_duplikasi = []
# for buah in daftar_buah:
#     hasil_duplikasi += [buah, buah]
# print(hasil_duplikasi)

# duplikasi = [buah for daftar_buah in daftar_buah for _ in range(2)]
# print(duplikasi)

# Soal No. 1 Full Cara 1
# hasil_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}
# ]

# lulus_saja = []

# for nama_mahasiswa in hasil_akhir:
#     if nama_mahasiswa["nilai"] > 65:
#         lulus_saja.append(nama_mahasiswa["nama"])

# print(lulus_saja)

# hasil_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}
# ]

# lulus_saja = []

# for nama_mahasiswa in hasil_akhir:
#     if nama_mahasiswa["nilai"] > 65:
#         lulus_saja.ekstend(nama_mahasiswa["nama"])

# print(lulus_saja)

# cara 2
# def siswa_lulus(hasil_akhir):
#     siswa_lulus = [siswa["nama"] for siswa in hasil_akhir if siswa["nilai"] > 65]
#     return siswa_lulus

# hasil_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}]
# print(siswa_lulus(hasil_akhir))

# cara 3
# hasil_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}]

# siswa_lulus = [siswa["nama"] for siswa in hasil_akhir if siswa ["nilai"] > 65]
# print(siswa_lulus)

# Soal No. 1
# daftar_buah = ["pepaya", "mangga", "pisang", "durian", "jambu"]
# print(daftar_buah[::-1])

# reversed_buah = []
# for buah in daftar_buah:
#     reversed_buah = [buah] + reversed_buah
# print(reversed_buah)

# daftar_buah.reverse()
# print(daftar_buah)

# daftar_buah = ["pepaya", "mangga", "pisang", "durian", "jambu"]

# clone_buah = []
# for buah in daftar_buah :
#     clone_buah += [buah]*2
# print(clone_buah)

# list buah = []
# daftar_buah = ["Semangka", "Durian", "Nanas", "Apel", "Pisang"]
# for buah in daftar_buah: 
#     list buah [buah]*2
# print(list_buah)

# nama_buah = ["Pepaya", "Mangga", "Pisang", "Durian", "Jambu"]
# print(nama_buah)

# duplikasi = []
# for buah in nama_buah:
#     duplikasi += [buah]*2
# print(duplikasi)

