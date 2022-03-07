import random
import tkinter
import tkinter as tk
from tkinter import *

root = Tk()
root.geometry('185x150')
root.title('Random Password Generator')
root.resizable(False, False)

def password_generator():
    generator_entry2.delete(0, END)
    lenght = int(generator_entry.get())
    password = "".join([random.choice(all) for _ in range(lenght)])
    generator_entry2.insert(0, password)

generatortitle = tk.Label(text='skriv hvor mye tall å generere')
generatortitle.grid(row= 0, column= 1, sticky= N)

generator_entry = tk.Entry(width=8)
generator_entry.grid(row= 1, column= 1, sticky= N)

generator_result = tkinter.Label(text= 'Password')
generator_result.grid(row= 2, column= 1)

generator_entry2 = tk.Entry(width=10,)
generator_entry2.grid(row= 3, column= 1, sticky= S)


generator_btn = tk.Button(text='Generer', command=password_generator)

generator_btn.grid(row= 4, column= 1, sticky= S)

digits = '0123456789'

chars = 'abcdefghijklmn' \
    'opqrstuvwxyz'

up = chars.upper()
special = '_!$%&?'
all = digits+chars+up+special

root.mainloop()
