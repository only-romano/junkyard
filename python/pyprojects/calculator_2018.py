#! Калькулятор 2018.

# import section
from tkinter import *

# root section
root = Tk()
root.title("Калькулятор 2018")
root.geometry("315x530+300+250")
root.configure(background='#2b0202')


# functions section
def bc():
    """ 'C' button click."""
    label_text.set('0')
    buffer.set('')


def b0():
    """ '0' button click."""
    w = label_text.get()
    if w == '0':
        pass
    else:
        label_text.set(w + '0')


def b1():
    """ '1' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('1')
    else:
        label_text.set(w + '1')


def b2():
    """ '2' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('2')
    else:
        label_text.set(w + '2')


def b3():
    """ '3' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('3')
    else:
        label_text.set(w + '3')


def b4():
    """ '4' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('4')
    else:
        label_text.set(w + '4')


def b5():
    """ '5' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('5')
    else:
        label_text.set(w + '5')


def b6():
    """ '6' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('6')
    else:
        label_text.set(w + '6')


def b7():
    """ '7' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('7')
    else:
        label_text.set(w + '7')


def b8():
    """ '8' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('8')
    else:
        label_text.set(w + '8')


def b9():
    """ '9' button click."""
    w = label_text.get()
    if w == '0':
        label_text.set('9')
    else:
        label_text.set(w + '9')


def bt():
    """ '.' button click."""
    w = label_text.get()
    if '.' in w:
        pass
    else:
        label_text.set(w + '.')


def bp():
    """ '+' button click."""
    buf = buffer.get()
    text = label_text.get()
    if len(buf.split()) == 0 and float(text) == 0:
        pass
    if len(buf.split()) == 0 and float(text) != 0:
        buffer.set(text + ' + ')
        label_text.set('0')
    if len(buf.split()) == 1 and float(text) == 0:
        buffer.set(buf + ' + ')
    if len(buf.split()) == 1 and float(text) != 0:
        buffer.set(text + ' + ')
        label_text.set('0')
    if len(buf.split()) == 2 and float(text) == 0:
        if '+' in buf:
            pass
        if '+' not in buf:
            buffer.set(buf.split()[0] + ' + ')
    if len(buf.split()) == 2 and float(text) != 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) + float(text)) + ' + ')
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) - float(text)) + ' + ')
        if '*' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) * float(text)) + ' + ')
        if '/' in buf:
            if float(text) != 0:
                label_text.set('0')
                buffer.set(str(float(buf.split()[0]) / float(text)) + ' + ')
            else:
                label_text.set('666')
                buffer.set('666')


def bm():
    """ '-' button click."""
    buf = buffer.get()
    text = label_text.get()
    if len(buf.split()) == 0 and float(text) == 0:
        buffer.set('0 - ')
    if len(buf.split()) == 0 and float(text) != 0:
        buffer.set(text + ' - ')
        label_text.set('0')
    if len(buf.split()) == 1 and float(text) == 0:
        buffer.set(buf + ' - ')
    if len(buf.split()) == 1 and float(text) != 0:
        buffer.set(text + ' - ')
        label_text.set('0')
    if len(buf.split()) == 2 and float(text) == 0:
        if '-' in buf.split()[1]:
            pass
        if '-' not in buf.split()[1]:
            buffer.set(buf.split()[0] + ' - ')
    if len(buf.split()) == 2 and float(text) != 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) + float(text)) + ' - ')
        if '*' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) * float(text)) + ' - ')
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) - float(text)) + ' - ')
        if '/' in buf:
            if float(text) != 0:
                label_text.set('0')
                buffer.set(str(float(buf.split()[0]) / float(text)) + ' - ')
            else:
                label_text.set('666')
                buffer.set('666')


def bmu():
    """ '*' button click."""
    buf = buffer.get()
    text = label_text.get()
    if len(buf.split()) == 0 and float(text) == 0:
        buffer.set('0 * ')
    if len(buf.split()) == 0 and float(text) != 0:
        buffer.set(text + ' * ')
        label_text.set('0')
    if len(buf.split()) == 1 and float(text) == 0:
        buffer.set(buf + ' * ')
    if len(buf.split()) == 1 and float(text) != 0:
        buffer.set(text + ' * ')
        label_text.set('0')
    if len(buf.split()) == 2 and float(text) == 0:
        if '*' in buf:
            pass
        if '*' not in buf:
            buffer.set(buf.split()[0] + ' * ')
    if len(buf.split()) == 2 and float(text) != 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) + float(text)) + ' * ')
        if '*' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) * float(text)) + ' * ')
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) - float(text)) + ' * ')
        if '/' in buf:
            if float(text) != 0:
                label_text.set('0')
                buffer.set(str(float(buf.split()[0]) / float(text)) + ' * ')
            else:
                label_text.set('666')
                buffer.set('666')


def bd():
    """ '/' button click."""
    buf = buffer.get()
    text = label_text.get()
    if len(buf.split()) == 0 and float(text) == 0:
        buffer.set('0 / ')
    if len(buf.split()) == 0 and float(text) != 0:
        buffer.set(text + ' / ')
        label_text.set('0')
    if len(buf.split()) == 1 and float(text) == 0:
        buffer.set(buf + ' / ')
    if len(buf.split()) == 1 and float(text) != 0:
        buffer.set(text + ' / ')
        label_text.set('0')
    if len(buf.split()) == 2 and float(text) == 0:
        if '/' in buf:
            pass
        if '/' not in buf:
            buffer.set(buf.split()[0] + ' / ')
    if len(buf.split()) == 2 and float(text) != 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) + float(text)) + ' / ')
        if '*' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) * float(text)) + ' / ')
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) - float(text)) + ' / ')
        if '/' in buf:
            if float(text) != 0:
                label_text.set('0')
                buffer.set(str(float(buf.split()[0]) / float(text)) + ' / ')
            else:
                label_text.set('666')
                buffer.set('666')


def bsq():
    """ 'x²' button click."""
    buf = buffer.get()
    text = label_text.get()
    if len(buf.split()) == 0 and float(text) == 0:
        buffer.set('0')
    if len(buf.split()) == 0 and float(text) != 0:
        buffer.set(str(float(text) ** 2))
        label_text.set('0')
    if len(buf.split()) == 1 and float(text) == 0:
        buffer.set(str(float(buf) ** 2))
    if len(buf.split()) == 1 and float(text) != 0:
        buffer.set(str(float(text) ** 2))
        label_text.set('0')
    if len(buf.split()) == 2 and float(text) == 0:
        buffer.set(str(float(buf.split()[0]) ** 2))
    if len(buf.split()) == 2 and float(text) != 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) + float(text)) ** 2))
        if '*' in buf:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) * float(text)) ** 2))
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) - float(text)) ** 2))
        if '/' in buf:
            if float(text) != 0:
                label_text.set('0')
                buffer.set(str((float(buf.split()[0]) / float(text)) ** 2))
            else:
                label_text.set(str(1/666))
                buffer.set(str(666 ** 2))


def bk():
    """ '√' button click."""
    buf = buffer.get()
    text = label_text.get()
    if len(buf.split()) == 0 and float(text) == 0:
        buffer.set('0')
    if len(buf.split()) == 0 and float(text) != 0:
        buffer.set(str(float(text) ** 0.5))
        label_text.set('0')
    if len(buf.split()) == 1 and float(text) == 0:
        buffer.set(str(float(buf) ** 0.5))
    if len(buf.split()) == 1 and float(text) != 0:
        buffer.set(str(float(text) ** 0.5))
        label_text.set('0')
    if len(buf.split()) == 2 and float(text) == 0:
        buffer.set(str(float(buf.split()[0]) ** 0.5))
    if len(buf.split()) == 2 and float(text) != 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) + float(text)) ** 0.5))
        if '*' in buf:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) * float(text)) ** 0.5))
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) - float(text)) ** 0.5))
        if '/' in buf:
            if float(text) != 0:
                label_text.set('0')
                buffer.set(str((float(buf.split()[0]) / float(text)) ** 0.5))
            else:
                label_text.set(str(-666))
                buffer.set(str(666 ** 0.5))


def be():
    """ 'equal' button click."""
    buf = buffer.get()
    text = label_text.get()
    if len(buf.split()) == 0:
        pass
    if len(buf.split()) == 1 and float(text) == 0:
        pass
    if len(buf.split()) == 1 and float(text) != 0:
        buffer.set(text)
        label_text.set('0')
    if len(buf.split()) == 2 and float(text) == 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) + float(buf.split()[0])) + ' + ')
        if '*' in buf:
            label_text.set('0')
            buffer.set(str(float(buf.split()[0]) * float(buf.split()[0])) + ' * ')
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set('0 - ')
        if '/' in buf:
            if float(buf.split()[0]) != 0:
                label_text.set('0')
                buffer.set('1 / ')
            else:
                label_text.set(str(-666))
                buffer.set(str(666 ** 0.5))
    if len(buf.split()) == 2 and float(text) != 0:
        if '+' in buf:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) + float(text))))
        if '*' in buf:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) * float(text))))
        if '-' in buf.split()[1]:
            label_text.set('0')
            buffer.set(str((float(buf.split()[0]) - float(text))))
        if '/' in buf:
            if float(text) != 0:
                label_text.set('0')
                buffer.set(str((float(buf.split()[0]) / float(text))))
            else:
                label_text.set(str(666))
                buffer.set(str(666))


# Variables section
label_text = StringVar()
buffer = StringVar()


# Default values section
label_text.set('0')
buffer.set('')


# Labels section
label = Label(textvariable=label_text, justify=RIGHT, font=("Arial", 35, "bold"),
              background="#ccc", foreground="#555", width=10, anchor='e')
label.grid(row=1, column=0, columnspan=4, ipady=4, padx=10, pady=5)

label2 = Label(textvariable=buffer, justify=RIGHT, font=("Georgia", 20),
               background="#2b0202", foreground="#ccc", width=18, anchor='w')
label2.grid(row=0, column=0, columnspan=4, ipady=8, padx=10, pady=5)


# Buttons section
btn0 = Button(text="0", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b0)
btn0.grid(row=6, column=0, ipadx=10, ipady=6, padx=10, pady=10)

btn1 = Button(text="1", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b1)
btn1.grid(row=3, column=0, ipadx=10, ipady=6, padx=10, pady=10)

btn2 = Button(text="2", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b2)
btn2.grid(row=3, column=1, ipadx=10, ipady=6, padx=10, pady=10)

btn3 = Button(text="3", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b3)
btn3.grid(row=3, column=2, ipadx=10, ipady=6, padx=10, pady=10)

btn4 = Button(text="4", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b4)
btn4.grid(row=4, column=0, ipadx=10, ipady=6, padx=10, pady=10)

btn5 = Button(text="5", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b5)
btn5.grid(row=4, column=1, ipadx=10, ipady=6, padx=10, pady=10)

btn6 = Button(text="6", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b6)
btn6.grid(row=4, column=2, ipadx=10, ipady=6, padx=10, pady=10)

btn7 = Button(text="7", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b7)
btn7.grid(row=5, column=0, ipadx=10, ipady=6, padx=10, pady=10)

btn8 = Button(text="8", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b8)
btn8.grid(row=5, column=1, ipadx=10, ipady=6, padx=10, pady=10)

btn9 = Button(text="9", background="#555", foreground="#ccc",
              font=("Verdana", 15, "bold"), command=b9)
btn9.grid(row=5, column=2, ipadx=10, ipady=6, padx=10, pady=10)

btn_t = Button(text=".", background="#555", foreground="#ccc",
               font=("Verdana", 15, "bold"), command=bt)
btn_t.grid(row=6, column=1, ipadx=14, ipady=6, padx=10, pady=10)

btn_c = Button(text="C", background="#555", foreground="#ccc",
               font=("Verdana", 15, "bold"), command=bc)
btn_c.grid(row=6, column=2, ipadx=9, ipady=6, padx=10, pady=10)

btn_p = Button(text="+", background="#555", foreground="#ccc",
               font=("Verdana", 15, "bold"), command=bp)
btn_p.grid(row=6, column=3, ipadx=8, ipady=6, padx=10, pady=10)

btn_m = Button(text="-", background="#555", foreground="#ccc",
               font=("Verdana", 15, "bold"), command=bm)
btn_m.grid(row=5, column=3, ipadx=11, ipady=6, padx=10, pady=10)

btn_mu = Button(text="*", background="#555", foreground="#ccc",
                font=("Verdana", 15, "bold"), command=bmu)
btn_mu.grid(row=4, column=3, ipadx=9, ipady=6, padx=10, pady=10)

btn_d = Button(text="/", background="#555", foreground="#ccc",
               font=("Verdana", 15, "bold"), command=bd)
btn_d.grid(row=3, column=3, ipadx=9, ipady=6, padx=10, pady=10)

btn_sq = Button(text="x²", background="#555", foreground="#ccc",
                font=("Verdana", 15, "bold"), command=bsq)
btn_sq.grid(row=2, column=0, ipadx=5, ipady=6, padx=10, pady=10)

btn_k = Button(text="√", background="#555", foreground="#ccc",
               font=("Verdana", 15, "bold"), command=bk)
btn_k.grid(row=2, column=1, ipadx=9, ipady=6, padx=10, pady=10)

btn_e = Button(text="equal", background="#555", foreground="#ccc",
               font=("Verdana", 15, "bold"), command=be)
btn_e.grid(row=2, column=2, columnspan=2, ipadx=24, ipady=6, padx=10, pady=10)

root.mainloop()
