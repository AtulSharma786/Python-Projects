from tkinter import *

root = Tk()
root.geometry("655x333")

def hello():
    print("hello tkinter Buttons")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="print now", command=hello) # When button pressed then the function hello is called
b1.pack(side=LEFT)

root.mainloop()
