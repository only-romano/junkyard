from tkinter import Tk, Label, BOTH
from time import strftime

window = Tk()
time = ''

clock = Label(window, font=('monospace', 66, 'bold'), bg='bisque')
clock.pack(fill=BOTH, expand=1)
window.wm_attributes("-topmost", 1)

def tick():
    global time
    new_time = strftime('%H:%M:%S')
    if new_time != time:
        time = new_time
        clock.config(text=time)
    clock.after(200, tick)

tick()
window.mainloop()
