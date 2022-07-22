from msilib.schema import Font
from tkinter import messagebox
from tkinter import *
import tkinter
from turtle import bgcolor

from setuptools import Command


window = Tk()


window.title("convertisseur")
window.geometry("3x6")
window.minsize(1000, 500)
window.iconbitmap("y/code.ico")
window.config(background='white')


frame = Frame(window, bg='red')
frame2 = Frame(window, bg='white')
frame_menu = Frame(window)



mon_menu = tkinter.Menu(frame_menu, )
frame_menu.pack()


def ver():
    hel=hel
    if hel == 'yes':
        window.destroy()
    else:
        pass




Titre_Label = Label(frame,
                    text="Convertisseur",
                    fg="black",
                    bg='#F2BF98',
                    font="monospace 40")
Titre_Label.pack()


euro = Entry(frame2,
             fg="black",
             bg="#F2BF98",
             font="monospace 10")
euro.pack(side=LEFT)


gauche = Label(frame2,
               text="  EURO",
               fg="black",
               bg="#F2BF98",
               font="monospace 40")
frame2.pack(side=LEFT)


droit = Label(frame,
              text="DH  ",
              fg="black",
              bg="#F2BF98",
              font="monospace 40")
droit.pack(side=RIGHT)


widht = 600
height = 600
image = PhotoImage(file="y/unn.png").zoom(1)
canvas = Canvas(frame, width=widht, height=height,
                bg="#F2BF98", bd=0, highlightthickness=0)
canvas.create_image(widht/2, height/2, image=image)
canvas.pack()

frame.pack(expand=YES)

window.mainloop()

