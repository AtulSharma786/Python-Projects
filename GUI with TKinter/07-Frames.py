from tkinter import *

root = Tk()
root.geometry("655x333")

f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y, pady=10)

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X, pady=10)

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack(pady=90)

l = Label(f2, text="welcome to my frame")
l.pack(padx=90)

root.mainloop()
