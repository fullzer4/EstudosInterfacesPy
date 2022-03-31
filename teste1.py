from cgitb import text
from ipaddress import collapse_addresses
from re import M
from tkinter import *

master = Tk() #criar uma janela

master.title("Matrizes") #titulo
#master.iconbitmap(default="icone") #mudar o icone
master.geometry("600x500+400+100") # largura x altura + dist esq + dist top ("onde vai iniciar o programa")

Button(text="Multiplicar").grid(row=0,column=0)
Button(text="Somar").grid(row=0,column=1)
Button(text="Subtrair").grid(row=0,column=2)
Button(text="Inverso").grid(row=0,column=3)
Button(text="Achar o X").grid(row=0,column=4)
Entry().grid(row=1,column=0)

master.mainloop() #rodar