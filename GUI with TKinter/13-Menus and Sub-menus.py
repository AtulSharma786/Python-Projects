from tkinter import *


def atul():
    print("hii")


root = Tk()
root.geometry("800x500")

# use this to create non drop down menu
# mymenu = Menu(root)
# mymenu.add_command(label="file", command=atul)
# mymenu.add_command(label="exit", command=quit)
# root.config(menu=yourmenu)

yourmenu = Menu(root)
m1 = Menu(yourmenu, tearoff=0)
m1.add_command(label="New", command=atul)
m1.add_command(label="save As", command=atul)
m1.add_separator()
m1.add_command(label="print", command=atul)
m1.add_command(label="save", command=atul)

yourmenu.add_cascade(label="file", menu=m1)
root.config(menu=yourmenu)

root.mainloop()
