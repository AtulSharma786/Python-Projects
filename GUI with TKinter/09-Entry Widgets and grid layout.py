from tkinter import *

root = Tk()
root.geometry("655x333")


def getvals():
    print(uservalue.get())
    print(passvalue.get())


user = Label(root, text="Username")
user.grid()
pwd = Label(root, text="Password")
pwd.grid(row=1)

# boolean var, double var, int var, string var

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()
