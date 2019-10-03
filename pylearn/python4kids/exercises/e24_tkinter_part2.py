from tkinter import *

window = Tk()

canvas = Canvas(window, width=400, height=700)
canvas.pack()

canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)
canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)  # угол в 360 ничего не нарисует

canvas.create_polygon(210, 10, 310, 10, 310, 110, fill="", outline="black")
canvas.create_polygon(300, 150, 340, 170, 220, 240, 240, 260, fill="", outline="black")

canvas.create_text(260, 300, text="Был один человек из Омска,")
canvas.create_text(280, 320, text="Полюбил и был прошен жёстко.", fill="red")
canvas.create_text(150, 450, text="Он сказал \"Это ужас,", font=('Times', 15))
canvas.create_text(200, 500, text="Но бывает и хуже:", font=('Helvetica', 20))
canvas.create_text(220, 550, text="Бывший мой рыдает", font=('Courier', 22))
canvas.create_text(220, 600, text="В луже\".", font=('Courier', 30))

window.mainloop()
