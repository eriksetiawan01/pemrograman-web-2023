import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Mengubah tinggi dari cm ke meter
        bmi = weight / (height * height)

        if bmi < 18.5:
            status = "Kurus"
        elif 18.5 <= bmi < 25:
            status = "Normal"
        else:
            status = "Gemuk"

        result_label.config(text=f"Indeks Massa Tubuh (BMI): {bmi:.2f}\nStatus: {status}")
    except ValueError:
        result_label.config(text="Masukkan angka yang valid!")

root = tk.Tk()
root.title("Kalkulator Berat Badan Ideal")

frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

weight_label = tk.Label(frame, text="Berat (kg):")
weight_label.grid(row=0, column=0, padx=5, pady=5)

weight_entry = tk.Entry(frame, width=20)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

height_label = tk.Label(frame, text="Tinggi (cm):")
height_label.grid(row=1, column=0, padx=5, pady=5)

height_entry = tk.Entry(frame, width=20)
height_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Hitung BMI", command=calculate_bmi)
calculate_button.pack(padx=20, pady=10)

result_label = tk.Label(root, text="Indeks Massa Tubuh (BMI): \nStatus: ")
result_label.pack(padx=20, pady=5)

root.mainloop()
