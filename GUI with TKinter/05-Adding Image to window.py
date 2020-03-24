from tkinter import *
# The commented section is for set jpg image

# from PIL import Image, ImageTk

root = Tk()

root.geometry("1000x800")
root.maxsize(1000,800)

photo1 = PhotoImage(file="photo.png")

# for jpg image
# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)

label1 = Label(image=photo1)
label1.pack()

root.mainloop()
