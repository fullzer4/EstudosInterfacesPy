from tkinter import *

janela = Tk()
janela.title("Matrizes")
janela.geometry("600x500+400+100")

widget1 = Frame(janela)
widget1.grid()

widget2 = Frame(janela)
widget2.grid(ipady= 10)

def getinputx(): #fazer funcionar inicio
    MX=inputx.get("1.0","end")
    print(MX)

inputx=Text(widget1, height=1, width=5)
inputx.pack(side=LEFT, expand=YES)

btnReadx=Button(widget1, height=1, width=10, text="Tipo Matriz X", command=getinputx)
btnReadx.pack(side=LEFT, expand=YES)

MX=inputx.get("1.0", "end")
label = Label(widget2, text = MX).mainloop()
Label.pack(side=LEFT, expand=YES)

widget1.pack()
widget2.pack()