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
janela.configure(bg='red') #Para teste
#Janela

widget1 = Frame(janela)
widget1.grid(ipadx= 110)

widget2 = Frame(janela)
widget2.grid(ipadx= 10, ipady= 10)

widget3 = Frame(janela)
widget3.grid(ipady= 10)
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


def getinputx(): #fazer funcionar inicio
    MX=inputx.get("1.0","end")
    print(MX)

def getinputy(): #fazer funcionar inicio
    MY=inputy.get("1.0","end")
    print(MY)

inputx=Text(widget2, height=1, width=5)
inputx.pack(side=LEFT, expand=YES)

btnReadx=Button(widget2, height=1, width=10, text="Tipo Matriz X", command=getinputx)
btnReadx.pack(side=LEFT, expand=YES)

inputy=Text(widget2, height=1, width=5)
inputy.pack(side=LEFT, expand=YES)

btnReady=Button(widget2, height=1, width=10, text="Tipo Matriz Y", command=getinputy)
btnReady.pack(side=LEFT, expand=YES)

mainloop()
MX=inputx.get("1.0", "end")
MY=inputy.get("1.0","end")

widget1.pack()
widget2.pack()
widget3.pack()



