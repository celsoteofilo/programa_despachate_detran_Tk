'''from tkinter.ttk import Entry
import tkinter
from tkinter import Tk, Label

def abrir_janela_2():

    janela2 = Tk()
    janela2.geometry("800x800")
    janela2.title('DESPACHANTE DIGITAL - CHECK LIST ')
    janela2.resizable=True   # resizable=True movintar a tela e false trava tela
    janela2.confirm_close=True # confirm_close=True, pergunta de confirmaçao fechar janela



        #  1 ENTRADA DE NOME:
    entrada = Label(janela2,text= " NOME: ")
    entrada.grid(row=3, column=0, padx=0, pady=0, sticky='nswe')
    entrada1 = Entry(janela2)
    entrada1.grid(row=3, column=1, pady=0, padx=0, sticky= 'nswe')

        # 2 ENTRADA PLACA:
    entrada = Label(janela2,text= " DIGITE A PLACA :  ")
    entrada.grid(row=4, column=0, padx=0, pady=0, sticky='nswe')

    placa = Entry(janela2)
    placa .grid(row=4, column=1, pady=0, padx=0, sticky= 'nswe')

    texto = Label(text= "PREENCHA O CHECK LIST")
    texto.grid(row=0, column=1, pady=0, padx=0, sticky= 'nswe')

    botao_sair= tkinter.Button(text=" SAIR ", command=janela2.destroy)
    botao_sair.grid(row=8, column=1, pady=5, padx=5, sticky= 'nswe')

'''










