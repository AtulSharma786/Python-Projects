from tkinter import *
root = Tk()
root.geometry("800x500")


def atul(event):
    print(f"clicked at {event.x} and {event.y}")


widget = Button(text="click me please")
widget.pack()

widget.bind('<Button-1>', atul)
widget.bind('<Double-1>', quit)

root.mainloop()
