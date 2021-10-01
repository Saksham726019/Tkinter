from tkinter import *

root = Tk()
root.title("Radio button")
root.iconbitmap("Avengers icon.ico")

Avengers = StringVar()
Avengers.set("Please chose an avenger to show their real name!")

my_label = Label(root, text=Avengers.get())
my_label.pack()


Real_Names = [
    ("Ironman", "Robert Downey Junior"), # Here, the format is, ("<text>", "value").
    ("Captain America", "Chris Evans"),
    ("Thor", "Chris Hemsworth"),
    ("HULK", "Mark Ruffalo"),
    ("Hawkeye", "Jeremy Renner"),
    ("Black Widow", "Scarlet Johansson")
]


for text, names in Real_Names: # The word names isn't compulsory, we can use any words but make sure to keep the same word in "value" of Radiobutton.
    Radiobutton(root, text=text, variable=Avengers, value=names).pack(anchor=W)


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


my_button = Button(root, text="OK", padx=10, pady=5, bg="red", fg="Black", command=lambda : clicked(Avengers.get()))
my_button.pack()

root.mainloop()
