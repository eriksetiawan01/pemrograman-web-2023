import tkinter as tk

def convert_length():
    try:
        input_length = float(entry.get())
        selected_unit = dropdown.get()

        if selected_unit == "cm to km":
            result = input_length / 100000
            result_label.config(text=f"Hasil: {input_length} cm = {result} km")
        elif selected_unit == "cm to mm":
            result = input_length * 10  
            result_label.config(text=f"Hasil: {input_length} cm = {result} mm")
        elif selected_unit == "km to cm":
            result = input_length * 100000
            result_label.config(text=f"Hasil: {input_length} km = {result} cm")
        elif selected_unit == "mm to cm":
            result = input_length / 10
            result_label.config(text=f"Hasil: {input_length} mm = {result} cm")
        elif selected_unit == "m to cm":
            result = input_length * 100
            result_label.config(text=f"Hasil: {input_length} m = {result} cm")
        elif selected_unit == "cm to m":
            result = input_length / 100
            result_label.config(text=f"Hasil: {input_length} cm = {result} m")
        elif selected_unit == "m to km":
            result = input_length / 1000
            result_label.config(text=f"Hasil: {input_length} m = {result} km")
        elif selected_unit == "km to m":
            result = input_length * 1000
            result_label.config(text=f"Hasil: {input_length} km = {result} m")
        else:
            result_label.config(text="Pilih konversi yang benar!")
    except ValueError:
        result_label.config(text="Masukkan angka yang valid!")

root = tk.Tk()
root.title("Konverter Ukuran")

frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

label = tk.Label(frame, text="Masukkan panjang:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=20)
entry.grid(row=0, column=1, padx=5, pady=5)

dropdown = tk.StringVar(root)
dropdown.set("Pilih konversi")
options = [
    "cm to km", "cm to mm", "km to cm", "mm to cm", 
    "m to cm", "cm to m", "m to km", "km to m"
]
menu = tk.OptionMenu(frame, dropdown, *options)
menu.grid(row=1, columnspan=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Konversi", command=convert_length)
convert_button.pack(padx=20, pady=10)

result_label = tk.Label(root, text="Hasil: ")
result_label.pack(padx=20, pady=5)

root.mainloop()
