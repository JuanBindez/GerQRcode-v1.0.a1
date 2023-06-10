# MIT License
#
# Copyright (c) 2022 - 2023 Juan Bindez  <juanbindez780@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
