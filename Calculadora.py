from tkinter import *

class Calcular:
    pass

class Clear:
    pass

class Resultado:
    pass

class InterfaceCalculadora:
    def __init__(self, janela):

        botao1 = Button(janela, text=("1"),font=("Arial", 15))
        botao1.place(x=98,y=150)
        botao1.config(width=4, height=3)

        botao2 = Button(janela, text=("2"),font=("Arial", 15))
        botao2.place(x=153,y=150)
        botao2.config(width=4, height=3)

        botao3 = Button(janela, text=("3"),font=("Arial", 15))
        botao3.place(x=208,y=150)
        botao3.config(width=4, height=3)

        botao4 = Button(janela, text=("4"),font=("Arial", 15))
        botao4.place(x=98,y=236)
        botao4.config(width=4, height=3)

        botao5 = Button(janela, text=("5"),font=("Arial", 15))
        botao5.place(x=153,y=236)
        botao5.config(width=4, height=3)

        botao6 = Button(janela, text=("6"),font=("Arial", 15))
        botao6.place(x=208,y=236)
        botao6.config(width=4, height=3)

        botao7 = Button(janela, text=("7"),font=("Arial", 15))
        botao7.place(x=98,y=322)
        botao7.config(width=4, height=3)

        botao8 = Button(janela, text=("8"),font=("Arial", 15))
        botao8.place(x=153,y=322)
        botao8.config(width=4, height=3)

        botao9 = Button(janela, text=("9"),font=("Arial", 15))
        botao9.place(x=208,y=322)
        botao9.config(width=4, height=3)

        botao0 = Button(janela, text=("0"),font=("Arial", 15))
        botao0.place(x=153,y=408)
        botao0.config(width=4, height=3)

        botaoLimpar = Button(janela, text=("C"),font=("Arial", 15), bg=("Red"))
        botaoLimpar.place(x=98,y=408)
        botaoLimpar.config(width=4, height=3)

        botaoIgual = Button(janela, text=("="),font=("Arial", 15),bg=("#5C8EE0"))
        botaoIgual.place(x=208,y=408)
        botaoIgual.config(width=4, height=3)

        botaoMais = Button(janela, text=("+"), font=("Arial", 15))
        botaoMais.place(x=263, y=150)
        botaoMais.config(width=4, height=3)

        botaoMenos = Button(janela, text=("-"), font=("Arial", 15))
        botaoMenos.place(x=263, y=236)
        botaoMenos.config(width=4, height=3)

        botaoVezes = Button(janela, text=("x"), font=("Arial", 15))
        botaoVezes.place(x=263, y=322)
        botaoVezes.config(width=4, height=3)

        botaoDivisao = Button(janela, text=("/"), font=("Arial", 15))
        botaoDivisao.place(x=263, y=408)
        botaoDivisao.config(width=4, height=3)


janela = Tk()
app = InterfaceCalculadora(janela)
icone = PhotoImage(file='2374370.png')
janela.iconphoto(True, icone)
janela.geometry("400x500")
janela.title("Calculadora")
janela.configure(bg="Gray")
janela.mainloop()