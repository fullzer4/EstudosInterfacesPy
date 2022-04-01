import tkinter as tk
root = tk.Tk()
root.geometry("400x240")

def getinputx():
    result=inputx.get("1.0","end")
    print(result)

inputx=tk.Text(root, height=10)
inputx.pack()
btnRead=tk.Button(root, height=1, width=1, text="Read", command=getinputx)

btnRead.pack()

root.mainloop()
result=inputx.get("1.0", "end")