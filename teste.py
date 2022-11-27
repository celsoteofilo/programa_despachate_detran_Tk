
nome   = ["celso"]
senha = [1,2,3,4,5]

achou_nome = False
achou_senha = False

nome_entrada = str(input('Qual nome : '))
senha_entrada = int(input('Qual e a senha: '))


for x  in nome:

    if x == nome_entrada :
        print('OK Nome encontrado')
        achou_nome =True
        break
else:
    print('Nome nao encontrado!! ')


for y  in senha:

    if y == senha_entrada :
        print('OK SENHA encontrado')
        achou_senha = True
        break
else:
    print('SENHA nao encontrado!! ')



if achou_nome == True  and  achou_senha == True:

    print(" OK OK OS 2 ")
else:
    print('NAO ACHOU ')

# __________________

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

