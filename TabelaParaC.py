from tkinter import *
  
class Table: 
      
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
   
root = Tk() 
t = Table(root) 
root.mainloop() 