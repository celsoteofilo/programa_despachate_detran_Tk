from tkinter import messagebox

from login import *


#________________FUNCAO  ENTRADA NOME E SENHA DE USUSARIO
from programa_despachate_detran_Tk.venv.Copia_seguranca_login import credenciais_novo_nome, credenciais_nova_senha


def botao_entrada():

    nome = entra_nome.get()
    senha =entra_senha.get()

    entrada_cred_nome.append((nome)) # montando a lista em seguencia
    entrada_cred_senha.append((senha))



#________________________ FUNCAO ENTRA DE NOVO NOME E  NOVA SENHA
def senha_nova():

    nome = novo_nome.get()
    senha = nova_senha.get()

    credenciais_novo_nome.append((nome)) # montando a lista em seguencia
    credenciais_nova_senha.append((senha))

    print(credenciais_novo_nome, credenciais_nova_senha)




#__________________________ BOTAO DE CONFIRMACAO PARA TESTA A SENHA _
def botao_teste_senhas():

    print(credenciais_novo_nome[0:10],credenciais_nova_senha[0:10])

    if entrada_cred_nome [0:10] == credenciais_novo_nome[0:10] and entrada_cred_senha [0:10] == entrada_cred_senha[0:10]:
        print('SENHA VALIDA !!!')
        messagebox.showinfo('Seja Bem vindo !!!')

    else:
        print('CADASTRE SENHA INVALIDA !!!')
        messagebox.showinfo('NAO CADASTRADO!!! CADASTRE A BAIXO.')
