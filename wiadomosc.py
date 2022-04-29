from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text="Tutaj wiadomość", font=50)
w.pack()

msg = Message(root, text="To jest \nprzykładowe okienko\n z wiadomością...", justify=CENTER, pady=20, bg="pink")
msg.pack()

root.mainloop()
