from tkinter import *

win = Tk()
win.title("my project")
win.geometry("500x300")
win.resizable(False, False) #заборона зміни розміру вікна
#елементи керування
#напис
nap = Label(win, text="текст для напису", font=("Comic Sans MS", 20), bg="green", fg="white")
nap.place(relx=0.1, rely=0.4)
win.mainloop()