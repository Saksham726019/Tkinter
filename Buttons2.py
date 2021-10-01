from tkinter import *

root = Tk()
root.title("Motivation")

def myclick():
    my_label = Label(root, text="Keep on going....Whatever it takes !", fg='white', bg='black')# fg is used to change the color of the text and bg for background.
    my_label.pack()                                     # LOL dark theme 🤣. We can aslo use color codes instead of their names.

my_button = Button(root, text="Click Me", command=myclick, fg='white', bg='black')

my_button.pack()

root.mainloop()
