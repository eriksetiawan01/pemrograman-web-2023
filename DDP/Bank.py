# class Myclass:
#     x = 5
# p1 = Myclass()
# print(p1)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("Reza", 30)
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(sell, name, age):
#         sell.name = name
#         sell.age = age
#     def myfunc(sell): print("Hello my name is " + sell.name)
# p1 = Person("John", 36)
# p1.myfunc()

class Bank:
#member1 variabel
    norek = ' '
    nama = ' '
    saldo = 0
    jmlNasabah = 0 # variabel static
    BANK = 'Bank Syariah Nurul Fikri' # variabel konstanta
#member2 konstruktor
    def __init__(self,no,nasabah,saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlNasabah += 1

#member3 method
    def nabung(self,uang):
#self.saldo = self.saldo + uang
        self.saldo += uang
    def tarik(self,uang):
#self.saldo = self.saldo - uang
        self.saldo -= uang
    def cetak(self):
        # print(Bank.BANK,
        #     '\n==========================',
        #     '\nNo. Rekening\t:',self.norek,
        #     '\nNama Nasabah\t:',self.nama,
        #     '\nSaldo\t\t: Rp. ',format(self.saldo, ','),
        #     '\n--------------------------'
        #     )
        print(Bank.BANK)
        print("No. Rekening : ",self.norek)
        print("Nama Nasabah : ",self.nama)
        print("Saldo : Rp. ", format(self.saldo,","))
        print("==========================")