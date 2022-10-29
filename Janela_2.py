
def test_janela():

    import tkinter
    from _xxsubinterpreters import destroy
    from tkinter import Tk, Label

    janela2 = Tk()
    janela2.geometry("800x800")
    janela2.title('DESPACHANTE DIGITAL - CHECK LIST ')
    janela2.resizable=True   # resizable=True movintar a tela e false trava tela
    janela2.confirm_close=True # confirm_close=True, pergunta de confirmaçao fechar janela


    texto = Label(text= "PREENCHA O CHECK LIST")
    texto.grid(row=0, column=1, pady=0, padx=0, sticky= 'nswe')

    botao_sair= tkinter.Button(janela2,text=" CONSULTAR ", command=janela2.destroy)
    botao_sair.grid(row=1, column=1, pady=5, padx=5, sticky= 'nswe')




    janela2.mainloop()