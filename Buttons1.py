from tkinter import *

root = Tk()

my_button = Button(root, text="Click Me", padx=10, pady=10, state=DISABLED)
# padx is used to change the size of the button in x-axis and pady in y-axis.
# DISABLED state is used to make the button unusable wheres ACTIVE state makes it usable.

my_button.pack()

root.mainloop()
