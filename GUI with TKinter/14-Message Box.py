from tkinter import *
import tkinter.messagebox as tmsg


def atul():
    print("Wow you have opened a menu")


def help():
    print("I will help you")
    # a = tmsg.showinfo("help", "should I help you")
    a = tmsg.askquestion("Help", "Should I help you")
    print(a)

def gogo():
    ans = tmsg.askretrycancel("Hii", "Go Ahead")
    if ans:
        print("Good")
    else:
        print("Bad")


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
m1.add_command(label="Save As", command=atul)
m1.add_separator()
m1.add_command(label="Print", command=atul)
m1.add_command(label="Save", command=atul)
m1.add_command(label="Help", command=help)
m1.add_command(label="Go Go", command=gogo)

yourmenu.add_cascade(label="file", menu=m1)
root.config(menu=yourmenu)

root.mainloop()
