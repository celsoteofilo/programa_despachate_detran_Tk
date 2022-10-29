


import tkinter
from tkinter import *
from tkinter import messagebox
#cores ------------------------------
co0 = "#fof3f5" # preto
co1 = "#feffff" # branco
co2 = "#3fb5a3" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra

#criando janela ------------------------------

janela = Tk()
janela.title("LOGIN")
janela.geometry("500x400")
janela.configure(background=co1)

#----------- VARIAVEL ARAMZENANDO SENHAS  ----------

credenciais_nome  =['celso']
credenciais_senha =['123']




#-------- ENTRADA  USUARI CADASTRADO NORMAL -------------------


def botao_entrada(credenciais_nome, credencias_senha):

    print(credenciais_nome[0:10])

    if credenciais_nome [0:10] == entra_nome and credenciais_senha [0:10] == entra_senha:
        print('SENHA VALIDA !!!')
        messagebox.showinfo('Seja Bem vindo !!!')

    else:
        print('CADASTRE SENHA INVALIDA !!!')
        messagebox.showinfo('NAO CADASTRADO!!! CADASTRE A BAIXO.')



# entrada de nome

janela_nome= Label(text= "ENTRE COM NOME:  ")
janela_nome.grid(row=3, column=0,padx=0, pady=0, sticky='nswe')
entra_nome = Entry()
entra_nome.grid(row=3, column=1, pady=0, padx=0, sticky= 'nswe')

# ------ entrda senha

janela_senha= Label(text= "ENTRE COM SENHA  ")
janela_senha.grid(row=4,column=0,padx=0, pady=0, sticky='nswe')

entra_senha = Entry()
entra_senha.grid(row=4, column=1, pady=0, padx=0, sticky= 'nswe')


botao_confirmar_senha = tkinter.Button(text="ENTRE. ",command=botao_entrada(credenciais_nome,credenciais_senha))
botao_confirmar_senha.grid(row=5, column=0, pady=2, padx=5, sticky= 'nswe',columnspan=3)



#----- CADASTRO DE NOVAS SENHAS -------------------

def senha_nova():

    nome = novo_nome.get()
    senha = nova_senha.get()

    credenciais_nome.append((nome)) # montando a lista em seguencia
    credenciais_senha.append((senha))

    print(credenciais_nome,credenciais_senha)


janela_cadastro_senha = Label(text= " DIGITE O NOME PARA CADASTRAR  ")
janela_cadastro_senha.grid(row=6, column=0, padx=0, pady=0, sticky='nswe')
novo_nome= Entry()
novo_nome.grid(row=6, column=1, pady=0, padx=0, sticky= 'nswe')



janela_cadastro_senha = Label(text= " DIGITE UMA SENHA P/ CADASTRAR  ")
janela_cadastro_senha.grid(row=7, column=0, padx=0, pady=0, sticky='nswe')
nova_senha = Entry()
nova_senha.grid(row=7, column=1, pady=0, padx=0, sticky= 'nswe')


botao_confirmar_senha = tkinter.Button(text="Salvar. ",command=senha_nova)
botao_confirmar_senha.grid(row=8, column=0, pady=2, padx=5, sticky= 'nswe',columnspan=3)



janela.mainloop()
