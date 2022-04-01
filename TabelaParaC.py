from tkinter import *

janela = Tk()
janela.title("Matrizes")
janela.geometry("600x500+400+100")
janela.configure(bg='red') #Para teste
#Janela

widget1 = Frame(janela)
widget1.grid(ipadx= 110)

def getinputx(): #fazer funcionar inicio
    MY=inputx.get("1.0","end")
    print(MY)

inputx=Text(widget1, height=1, width=5)
inputx.pack(side=LEFT, expand=YES)

btnReadx=Button(widget1, height=1, width=10, text="Tipo Matriz X", command=getinputx)
btnReadx.pack(side=LEFT, expand=YES)

class Resultado: 
      
    def __init__(self,root): 
        
        for L in range(TotalL): 
            for C in range(TotalC): 
                        self.e = Entry(root, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                        self.e.grid(row=L, column=C) 
                        self.e.insert(END, lst[L][C]) 
lst = [("",'Coluna1','Coluna2',"Coluna3"), 
       ("Linha1",4 ,4 ,18), 
       ("Linha2",2 ,0 ,20), 
       ("Linha3",6 ,5 ,21), 
       ("Linha4",8 ,8 ,21)] 
   
TotalL = len(lst) 
TotalC = len(lst[0]) 
   
root = Tk() # iniciar tabela
janela.mainloop() 
widget1.pack()