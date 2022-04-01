from doctest import master
from tkinter import *

#Blibiotecas

#=======================================================
#
#                     Funções inicio
#
#=======================================================

def FMultiplicar(): #testar
    print("Multiplicar Funcionando")

def FSomar(): #testar
    print("Somar Funcionando")

def FSubtrair(): #testar
    print("Subtrair Funcionando")

def FInvertida(): #testar
    print("Invertida Funcionando")

def FAcharX(): #testar
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
widget1.grid(ipadx= 110, ipady= 10)
#Divisaobotoes

Multiplicar = Button(widget1, text="Multiplicar", command=FMultiplicar)
Multiplicar["font"] = ("Verdana", "10", "italic", "bold")
Multiplicar.pack (side=LEFT, expand=YES)

#Multiplicar

Somar = Button(widget1, text="Somar", command=FSomar)
Somar["font"] = ("Verdana", "10", "italic", "bold")
Somar.pack (side=LEFT, expand=YES)
#Somar

Subtrair = Button(widget1, text="Subtrair", command=FSubtrair)
Subtrair["font"] = ("Verdana", "10", "italic", "bold")
Subtrair.pack (side=LEFT, expand=YES)
#Subtrair

Invertida = Button(widget1, text="Invertida", command=FInvertida)
Invertida["font"] = ("Verdana", "10", "italic", "bold")
Invertida.pack (side=LEFT, expand=YES)
#Invertida

AcharX = Button(widget1, text="AcharX", command=FAcharX)
AcharX["font"] = ("Verdana", "10", "italic", "bold")
AcharX.pack (side=LEFT, expand=YES)
#AcharX

janela.mainloop()
#Inciar

