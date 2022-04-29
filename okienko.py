from tkinter import *

root = Tk()


# logika
def clicked():
    res = "Napisałeś:" + txt.get()
    a.configure(text=res)


# setup
root.title("Witaj w mojej apce!")
root.geometry('350x200')

# wygląd

menu = Menu(root)
item = Menu(menu)
item.add_command(label='Nowy')
menu.add_cascade(label='Plik', menu=item)
root.config(menu=menu)

a = Label(root, text="HELLO")
a.grid()

btn = Button(root, text="Kliknij!", fg="blue", command=clicked)
btn.grid(column=2, row=1)

txt = Entry(root, width=10)
txt.grid(column=1, row=1)

root.mainloop()
