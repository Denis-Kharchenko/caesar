from tkinter import *
from tkinter import Checkbutton


def btn_click():
    z = 0
    a = ent1.get()
    d = ''
    s = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    se = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    be = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if cb.get() == 0:
        c = int(ent2.get())
        for i in range(len(a)):
            if a[i] in s:
                z = s.find(a[i])
                d += s[z + c]
            elif a[i] in b:
                z = b.find(a[i])
                d += b[z + c]
            elif a[i] in se:
                z = se.find(a[i])
                d += se[z + c]
            elif a[i] in be:
                z = be.find(a[i])
                d += be[z + c]
            else:
                d += a[i]
                continue
        ent3.delete(0, END)
        ent3.insert(0, d)
    else:
        a = str(ent1.get()).split(' ')
        d = []
        for i in range(len(a)):
            d.append(' ')
            for j in range(len(a[i])):
                c = len(a[i])
                c -= a[i].count(',') + a[i].count('.') + a[i].count('!') + a[i].count('"') + a[i].count('?') + a[
                    i].count(':') + a[i].count(';')
                if a[i][j] in s:
                    z = s.find(a[i][j])
                    d.append(s[z + c])
                elif a[i][j] in b:
                    z = b.find(a[i][j])
                    d.append(b[z + c])
                elif a[i][j] in se:
                    z = se.find(a[i][j])
                    d.append(se[z + c])
                elif a[i][j] in be:
                    z = be.find(a[i][j])
                    d.append(be[z + c])
                else:
                    d.append(a[i][j])
                    continue
        del d[0]

        ent3.delete(0, END)
        ent3.insert(0, ''.join(d))


def btn_click2():
    a = ent1.get()
    z = 0
    d = ''
    s = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
    se = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    be = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    if cb.get() == 0:
        c = int(ent2.get())
        for i in range(len(a)):
            if a[i] in s:
                z = s.find(a[i])
                d += s[z - c]
            elif a[i] in b:
                z = b.find(a[i])
                d += b[z - c]
            elif a[i] in se:
                z = se.find(a[i])
                d += se[z - c]
            elif a[i] in be:
                z = be.find(a[i])
                d += be[z - c]
            else:
                d += a[i]
                continue
        ent3.delete(0, END)
        ent3.insert(0, d)
    else:
        a = str(ent1.get()).split(' ')
        d = []
        for i in range(len(a)):
            d.append(' ')
            for j in range(len(a[i])):
                c = len(a[i])
                c -= a[i].count(',') + a[i].count('.') + a[i].count('!') + a[i].count('"') + a[i].count('?') + a[
                    i].count(':') + a[i].count(';')
                if a[i][j] in s:
                    z = s.find(a[i][j])
                    d.append(s[z - c])
                elif a[i][j] in b:
                    z = b.find(a[i][j])
                    d.append(b[z - c])
                elif a[i][j] in se:
                    z = se.find(a[i][j])
                    d.append(se[z - c])
                elif a[i][j] in be:
                    z = be.find(a[i][j])
                    d.append(be[z - c])
                else:
                    d.append(a[i][j])
                    continue
        del d[0]

        ent3.delete(0, END)
        ent3.insert(0, ''.join(d))


root = Tk()
root.title('Шифр Цезаря')
root.geometry('300x250+500+100')

frame = Frame(root)
frame.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)

title = Label(frame, text='Введите текст', width=10)
title2 = Label(frame, text='Введите ключ', width=10)
ent1 = Entry(frame)
ent2 = Entry(frame)
ent3 = Entry(frame)
chk_state = IntVar()
cb = IntVar()
chk = Checkbutton(frame, text='Усилить Шифр!', variable=cb, onvalue=1, offvalue=0)

title.grid(row=0, column=0)
title2.grid(row=1, column=0)
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)
ent3.place(x=40, y=150)
chk.place(x=0, y=50)

btn1 = Button(frame, text='Зашифровать!', command=btn_click).place(x=100, y=100)
btn2 = Button(frame, text='Расшифровать!', command=btn_click2).place(x=0, y=100)

root.mainloop()
