from tkinter import *
from datetime import datetime

import pyglet
pyglet.font.add_file("digital-7.ttf")

janela = Tk()

cor1 = "#000000"
cor2 = "#eb463b"


fundo = cor1
cor = cor2

janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

def relogio():

    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana  + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text="", font=("digital-7 100"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("digital-7 17"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()