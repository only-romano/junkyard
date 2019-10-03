from tkinter import *

window = Tk()
canvas = Canvas(window, width=600, height=400)
canvas.pack()

my_image = PhotoImage(file="test.gif")
canvas.create_image(0, 0, anchor=NW, image=my_image)

window.mainloop()
