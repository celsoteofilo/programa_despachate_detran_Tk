import tkinter
from tkinter import *
#_______________cores _____________________
from tkinter import messagebox

co0 = "#fof3f5" # preto
co1 = "#feffff" # branco
co2 = "#3fb5a3" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra

#__________________criando janela___________________

janela = Tk()
janela.title("LOGIN")
janela.geometry("500x400")
janela.configure(background=co1)

#___________VARIAVEL ARAMZENANDO SENHAS_____________

#________________Lista entrada nome  e senha

entrada_cred_nome = []
entrada_cred_senha = []

a_novo_nome =[]
a_nova_senha=[]

#________________FUNCAO  ENTRADA NOME E SENHA DE USUSARIO

def botao_entrada():
    nome = entra_nome.get()
    senha = entra_senha.get()


    entrada_cred_nome.append(nome)
    entrada_cred_senha.append(senha)

    print(entrada_cred_nome, entrada_cred_senha)
    print('AS DUAS NOVAS ,ENTRADA ')

    if  entra_nome :
        print('SENHA VALIDA !!!')
        messagebox.showinfo('Seja Bem vindo !!!')

    else:
        print(False)
        print('CADASTRE SENHA INVALIDA !!!')
        messagebox.showinfo('NAO CADASTRADO!!! CADASTRE A BAIXO.')
        entrada_cred_senha.clear()
        entrada_cred_nome.clear()

#________________________ FUNCAO ENTRA DE NOVO NOME E  NOVA SENHA
def senha_nova():

    nome = novo_nome.get()
    senha = nova_senha.get()

    a_novo_nome.append(nome)
    a_nova_senha.append(senha)

    print(a_novo_nome,a_nova_senha)


# ___________________ ENTRADAS __________________________________

# ___________________ENTRADA  NOME__________________________________

janela_nome= Label(text= "ENTRE COM NOME:  ")
janela_nome.grid(row=3, column=0,padx=0, pady=0, sticky='nswe')
entra_nome = Entry()
entra_nome.grid(row=3, column=1, pady=0, padx=0, sticky= 'nswe')

# _________________ENTRADA SENHA__________________________________

janela_senha= Label(text= "ENTRE COM SENHA  ")
janela_senha.grid(row=4,column=0,padx=0, pady=0, sticky='nswe')
entra_senha = Entry()
entra_senha.grid(row=4, column=1, pady=0, padx=0, sticky= 'nswe')

# __________________BOTAO CONFIRMAR ENTRADA__________________________

botao_confirmar_senha = tkinter.Button(text="ENTRE USUARIO CADASTRADO ", command=botao_entrada)
botao_confirmar_senha.grid(row=5, column=0, pady=2, padx=5, sticky= 'nswe',columnspan=3)

#_______________________ENTRADAS SENHAS NOVAS ____________________________

#_________________________ENTRADA NOVO NOME_________________________________

janela_cadastro_nome = Label(text= " DIGITE O NOME PARA CADASTRAR  ")
janela_cadastro_nome.grid(row=6, column=0, padx=0, pady=0, sticky='nswe')
novo_nome= Entry()
novo_nome.grid(row=6, column=1, pady=0, padx=0, sticky= 'nswe')


# __________________________ENTRADA NOVA SENHA_________________________________
janela_cadastro_senha = Label(text= " DIGITE UMA SENHA P/ CADASTRAR  ")
janela_cadastro_senha.grid(row=7, column=0, padx=0, pady=0, sticky='nswe')
nova_senha = Entry()
nova_senha.grid(row=7, column=1, pady=0, padx=0, sticky= 'nswe')

# _______________________BOTAO CONFIRMA NOVA SENHA_______________________________________

botao_confirmar_senha = tkinter.Button(text="SALVAR SENHA NOVA. ",command=senha_nova)
botao_confirmar_senha.grid(row=8, column=0, pady=2, padx=5, sticky= 'nswe',columnspan=3)

janela.mainloop()

