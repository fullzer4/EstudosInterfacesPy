from doctest import master
from tkinter import *

from setuptools import Command

#Blibiotecas

#=======================================================
#
#                     Funções inicio
#
#=======================================================

def Multiplicar(): #testar
    print("Multiplicar Funcionando")

def Somar(): #testar
    print("Somar Funcionando")

def Subtrair(): #testar
    print("Subtrair Funcionando")

def FInvertida(): #testar
    print("Invertida Funcionando")

def AcharX(): #testar
    print("AcharX Funcionando")

#=======================================================
#
#                    Tkinter inicio
#
#=======================================================

janela = Tk()
janela.title("Matrizes")
janela.geometry("600x500+400+100")
#Janelas

widget1 = Frame(master)
widget1.pack()
#Divisaobotoes

Multiplicar = Button(widget1, text="Multiplicar")
Multiplicar["font"] = ("Verdana", "10", "italic", "bold")
Multiplicar.pack ()
#Multiplicar

Somar = Button(widget1, text="Somar")
Somar["font"] = ("Verdana", "10", "italic", "bold")
Somar.pack ()
#Somar

Subtrair = Button(widget1, text="Subtrair")
Subtrair["font"] = ("Verdana", "10", "italic", "bold")
Subtrair.pack ()
#Subtrair

Invertida = Button(widget1, text="Invertida")
Invertida["font"] = ("Verdana", "10", "italic", "bold")
Invertida.pack ()
#Invertida

AcharX = Button(widget1, text="AcharX")
AcharX["font"] = ("Verdana", "10", "italic", "bold")
AcharX.pack ()
#AcharX

janela.mainloop()
#Inciar