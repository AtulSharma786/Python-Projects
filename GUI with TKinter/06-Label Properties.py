from tkinter import *

root = Tk()
root.geometry("444x233")
root.title("GUI")

# important label options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# font=("comicsansms", 19, "bold")
# font=("comicsansms 19 bold")

# padx - x padding
# pady - y padding
# relief - border styling = sunken, raised, groove, ridge

title_label = Label(text='''But still ignored.You know,there’s some interesting stuff in here...
                            There are mountain trolls riding Graph through Hungary,
                            there are giants with winged tattoos on their backs walking
                            through the Greek Seas, and the werewolves	have gone entirely 
                            underground''',
                    bg="grey",
                    fg="white",
                    padx=58,
                    pady=113,
                    font=("comicsansms 19 bold"),
                    borderwidth=2,
                    relief=SUNKEN) # For Border Styling

# important pack options
# anchor -
# side - top, bottom, left, right
# fill -
# padx -
# pady -

title_label.pack(anchor="se", side=LEFT, fill=Y, padx=10, pady=12)


root.mainloop()
