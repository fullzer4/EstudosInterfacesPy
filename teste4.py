from tkinter import *

app = Tk()
app.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))
app.mainloop()