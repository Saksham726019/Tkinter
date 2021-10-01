from tkinter import *

root = Tk()
root.title("Radio button")

r = IntVar()
r.set(0)


def clicked(value):
    my_label = Label(root, text=value)
    my_label.pack()


Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda : clicked(r.get())).pack()

my_label = Label(root, text=r.get())
my_label.pack()

my_button = Button(root, text="CLick Me!", command=lambda : clicked(r.get()))
my_button.pack()

root.mainloop()
