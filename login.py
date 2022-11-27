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

# ___________________ ENTRADAS __________________________________


nome_a   = ["celso"]
senha_a = [1,2,3,4,5]

achou_nome = False
achou_senha = False

print(nome_a)
print(senha_a)


def entrada():

    achou_nome = False
    achou_senha = False


    nome_entrada = nome.get()
    senha_entrada = int(senha.get())
#_______________________________________________________________
    for x  in nome_a:

        if x == nome_entrada :
            print('OK Nome encontrado')
            achou_nome =True
            break
    else:
        print('Nome nao encontrado!! ')


    for y  in senha_a:

        if y == senha_entrada :
            print('OK SENHA encontrado')
            achou_senha = True
            break
    else:
        print('SENHA nao encontrado!! ')



    if achou_nome == True  and  achou_senha == True:

       messagebox.showinfo('Seja Bem vindo !!!')

    else:
        messagebox.showinfo('NAO CADASTRADO!!! CADASTRE A BAIXO.')


def salva_senha_nova():


    n_nome = novo_nome.get()
    n_senha = int(nova_senha.get())

    nome_a.append(n_nome)
    senha_a.append(int(n_senha))


    print(nome_a)
    print(senha_a)

# ___________________ENTRADA  NOME__________________________________

janela_nome= Label(text= "ENTRE COM NOME:  ")
janela_nome.grid(row=3, column=0,padx=0, pady=0, sticky='nswe')
nome = Entry()
nome.grid(row=3, column=1, pady=0, padx=0, sticky= 'nswe')

# _________________ENTRADA SENHA__________________________________

janela_senha= Label(text= "ENTRE COM SENHA  ")
janela_senha.grid(row=4,column=0,padx=0, pady=0, sticky='nswe')
senha = Entry()
senha.grid(row=4, column=1, pady=0, padx=0, sticky= 'nswe')

# __________________BOTAO CONFIRMAR ENTRADA__________________________

botao_confirmar_senha = tkinter.Button(text="ENTRE USUARIO CADASTRADO ",command=entrada)
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

botao_confirmar_senha = tkinter.Button(text="SALVAR SENHA NOVA. ",command=salva_senha_nova)
botao_confirmar_senha.grid(row=8, column=0, pady=2, padx=5, sticky= 'nswe',columnspan=3)

janela.mainloop()

