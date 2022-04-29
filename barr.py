from tkinter import *

root = Tk()
root.geometry("150x200")

w = Label(root, text='Scrolle', font=40)
w.pack()

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scroll.set)

for line in range(1, 26):
    mylist.insert(END, "Pozycja" + str(line))

mylist.pack(side=LEFT, fill=BOTH)
scroll.config(command=mylist.yview)
root.mainloop()