import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        messagebox.showinfo("Tambah Tugas", f"Tugas '{task}' ditambahkan!")
    else:
        messagebox.showwarning("Peringatan", "Silakan masukkan tugas!")

def edit_task():
    try:
        index = task_list.curselection()[0]
        edited_task = entry.get()
        if edited_task:
            task_list.delete(index)
            task_list.insert(index, edited_task)
            entry.delete(0, tk.END)
            messagebox.showinfo("Edit Tugas", "Tugas berhasil diedit!")
        else:
            messagebox.showwarning("Peringatan", "Silakan masukkan tugas yang diedit!")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

def save_tasks():
    tasks = list(task_list.get(0, tk.END))
    with open("task_list.txt", "w") as file:
        file.write("\n".join(tasks))

def load_tasks():
    try:
        with open("task_list.txt", "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                task_list.insert(tk.END, task)
    except FileNotFoundError:
        pass

def on_task_select(event):
    try:
        index = task_list.curselection()[0]
        selected_task = task_list.get(index)
        entry.delete(0, tk.END)
        entry.insert(tk.END, selected_task)
    except IndexError:
        pass

root = tk.Tk()
root.title("Manajer Tugas Sederhana")

frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

label = tk.Label(frame, text="Tambah/Edit Tugas:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(frame, text="Tambah", width=10, command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=5)

edit_button = tk.Button(frame, text="Edit", width=10, command=edit_task)
edit_button.grid(row=1, column=2, padx=5, pady=5)

delete_button = tk.Button(frame, text="Hapus", width=10, command=delete_task)
delete_button.grid(row=2, column=2, padx=5, pady=5)

task_list = tk.Listbox(root, width=50, height=15)
task_list.pack(padx=20, pady=10)

task_list.bind("<<ListboxSelect>>", on_task_select)

save_button = tk.Button(root, text="Simpan Tugas", width=15, command=save_tasks)
save_button.pack(padx=20, pady=5)

# Memuat tugas saat aplikasi dibuka
load_tasks()

root.mainloop()
