from tkinter import *

window = Tk()
lebar = 500
tinggi = 400
x = 400
y = 100

window.resizable(0,0)
window.geometry(f"{lebar}x{tinggi}+{x}+{y}")
window.mainloop()