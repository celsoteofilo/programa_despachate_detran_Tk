
import tkinter
from tkinter import *


#cores ------------------------------
from tkinter import messagebox

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

credenciais_novo_nome =[]
credenciais_nova_senha =[]

entrada_cred_nome=[]
entrada_cred_senha=[]



#________________FUNCAO  ENTRADA NOME E SENHA DE USUSARIO

def botao_entrada():

    nome = entra_nome.get()
    senha =entra_senha.get()

    entrada_cred_nome.append((nome))
    entrada_cred_senha.append((senha))

    print(entrada_cred_nome, entrada_cred_senha)
    print(credenciais_novo_nome, credenciais_nova_senha)


    if entrada_cred_nome == credenciais_novo_nome and entrada_cred_senha == credenciais_nova_senha:

        print('SENHA VALIDA !!!')
        messagebox.showinfo('Seja Bem vindo !!!')

    else:
        print('CADASTRE SENHA INVALIDA !!!')
        messagebox.showinfo('NAO CADASTRADO!!! CADASTRE A BAIXO.')


#________________________ FUNCAO ENTRA DE NOVO NOME E  NOVA SENHA
def senha_nova():

    nome = novo_nome.get()
    senha = nova_senha.get()

    credenciais_novo_nome.append((nome))
    credenciais_nova_senha.append((senha))

    print(credenciais_novo_nome, credenciais_nova_senha)

# ___________________ ENTRADAS __________________________________

# ------- ENTRADA  NOME
janela_nome= Label(text= "ENTRE COM NOME:  ")
janela_nome.grid(row=3, column=0,padx=0, pady=0, sticky='nswe')
entra_nome = Entry()
entra_nome.grid(row=3, column=1, pady=0, padx=0, sticky= 'nswe')

# --------ENTRADA SENHA

janela_senha= Label(text= "ENTRE COM SENHA  ")
janela_senha.grid(row=4,column=0,padx=0, pady=0, sticky='nswe')
entra_senha = Entry()
entra_senha.grid(row=4, column=1, pady=0, padx=0, sticky= 'nswe')

# ----- BOTAO CONFIRMAR ENTRADA

botao_confirmar_senha = tkinter.Button(text="ENTRE USUARIO CADASTRADO ", command=botao_entrada)
botao_confirmar_senha.grid(row=5, column=0, pady=2, padx=5, sticky= 'nswe',columnspan=3)


#_______________________ENTRADAS SENHAS NOVAS ____________________________

#----- ENTRADA NOVO NOME

janela_cadastro_nome = Label(text= " DIGITE O NOME PARA CADASTRAR  ")
janela_cadastro_nome.grid(row=6, column=0, padx=0, pady=0, sticky='nswe')
novo_nome= Entry()
novo_nome.grid(row=6, column=1, pady=0, padx=0, sticky= 'nswe')


# ----- ENTRADA NOVA SENHA
janela_cadastro_senha = Label(text= " DIGITE UMA SENHA P/ CADASTRAR  ")
janela_cadastro_senha.grid(row=7, column=0, padx=0, pady=0, sticky='nswe')
nova_senha = Entry()
nova_senha.grid(row=7, column=1, pady=0, padx=0, sticky= 'nswe')

# ------ BOTAO CONFIRMA NOVA SENHA
botao_confirmar_senha = tkinter.Button(text="SALVAR SENHA NOVA. ",command=senha_nova)
botao_confirmar_senha.grid(row=8, column=0, pady=2, padx=5, sticky= 'nswe',columnspan=3)



#______________________________________________________________________________________________


janela.mainloop()
