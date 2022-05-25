from cProfile import label
import pyqrcode
import png
from pyqrcode import QRCode
from tkinter import *
from tkinter import messagebox
import time


def converter():

    entrada = entrada_de_dados.get()
    saida = nome_de_saida_do_arquivo.get()

    url = pyqrcode.create(entrada)

    url.svg(saida, scale = 8)
    url.png(saida, scale = 6)
    time.sleep(2)
    messagebox.showinfo("QRcode Converter", "Seu QRCODE Esta Pronto")



#inicio do bloco da interface grafica
window = Tk()

window.title("Gerador De QRcode")
window.geometry("400x400")


label = Label(window, text="Cole Aqui")
label.grid(row=0, column=0)
entrada_de_dados = Entry(window, width=10)
entrada_de_dados.grid(row=0, column=1)

label = Label(window, text="Nome De Saída do aquivo")
label.grid(row=1, column=0)
nome_de_saida_do_arquivo = Entry(window, width=10)
nome_de_saida_do_arquivo.grid(row=1, column=1)

botao = Button(window, text="Converter", command=converter)
botao.grid(row=4, column=1)


window.mainloop()
#fim do bloco da interface grafica
