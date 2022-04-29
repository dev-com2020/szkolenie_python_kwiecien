import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Combo")
window.geometry('500x250')

ttk.Label(window, text="Widżet ComboBox",
          background='green', foreground='white',
          font=("Arial", 15)).grid(row=0, column=1)

ttk.Label(window, text="Wybierz miesiąc:",
          font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=25)

lista = tk.StringVar()
miesiac = ttk.Combobox(window, width=27, textvariable=lista)

miesiac['values'] = (' January',
                     ' February',
                     ' March',
                     ' April',
                     ' May',
                     ' June',
                     ' July',
                     ' August',
                     ' September',
                     ' October',
                     ' November',
                     ' December')
miesiac.grid(column=1, row=5)
miesiac.current(0)

window.mainloop()
