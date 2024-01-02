import math
# 1
def tambah(bil1,bil2):
    hasil = bil1+bil2
    print("hasil tambah dari",bil1,"+",bil2,"=",hasil)
# 2
def kurang(bil1, bil2):
    hasil = bil1-bil2
    print("hasil pengurangan dari",bil1,"-",bil2,"=",hasil)
# 3
def kali(bil1, bil2):
    hasil = bil1 * bil2
    print("hasil perkalian dari",bil1,"*",bil2,"=",hasil)
# 4
def bagi(bil1, bil2):
    hasil = bil1 / bil2
    print("hasil pembagian dari",bil1,"/",bil2,"=",hasil)
# 5
def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print("hasil pemangkatan dari",bil1,"^",bil2,"=",hasil)
# 6
def log(bil):
    print("log10 dari ", bil, "=", math.log10(bil))
# 7
def akar(bil):
    print("akar dari", bil, "=", math.sqrt(bil))
# 8
def sin(sudut):
    radian = math.radians(sudut)
    print("Sinus dari", sudut, "=", math.sin(radian))
# 9
def cos(sudut):
    radian = math.radians(sudut)
    print("Cosinus dari", sudut, "=", math.cos(radian))
# 10
def tan(sudut):
    radian = math.radians(sudut)
    print("Tangen dari", sudut, "=", math.tan(radian))