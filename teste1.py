from cgitb import text
from ipaddress import collapse_addresses
from re import M
from tkinter import *

janela = Tk() #criar uma janela

janela.title("Matrizes") #titulo
#janela.iconbitmap(default="icone") #mudar o icone
janela.geometry("600x500+400+100") # largura x altura + dist esq + dist top ("onde vai iniciar o programa")
