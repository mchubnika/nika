from tkinter import *
from tkinter import ttk

win = Tk()
win.title("my project")
win.geometry("500x300")
win.resizable(False, False) #заборона зміни розміру вікна
#елементи керування
#напис
nap = Label(win, text="текст для напису", font=("Comic Sans MS", 20), bg="green", fg="white")
nap.place(relx=0.2, rely=0.1, anchor="center")
#поле для введення
ent=Entry(win, font=('Comic Sans MS', 20), width=4)
ent.place(relx=0.1, rely=0.2)
#кнопка
but=Button(win, text="click", font=('Comic Sans MS', 20), width=7, height=3, fg="#004512", bg="blue")
but.place(relx=0.1, rely=0.35)
#випадаючий список
comb= ttk.Combobox(win, font=('Comic Sans MS', 15), width=10, values=["option1", "option2", "option3", "option4", "option5"])
comb.place(relx=0.4, rely=0.35)

win.mainloop()