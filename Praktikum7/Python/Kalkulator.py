angka1 = float(input("Masukkan angka 1: "))
angka2 = float(input("Masukkan angka 2: "))
operator = input("Pilih operator (+, -, *, /, **): ")

operasi = {
    '+': angka1 + angka2,
    '-': angka1 - angka2,
    '*': angka1 * angka2,
    '/': angka1 / angka2 if angka2 != 0 else "Tidak bisa dibagi dengan nol.",
    '**': angka1 ** angka2
}

hasil = operasi.get(operator, "Operator tidak valid.")
if hasil != "Operator tidak valid.":
    print(f"Angka pertama: {angka1}")
    print(f"Angka kedua: {angka2}")
    print(f"Pilihan Operator: {operator}")
    print(f"Hasil operator {angka1} {operator} {angka2} = {hasil}")
else:
    print(hasil)