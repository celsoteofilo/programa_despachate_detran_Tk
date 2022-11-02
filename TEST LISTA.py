lista_1= ['a','b','c']
lista_2 = ['1','2','3']

nome = str(input('Entre com   o nome :'))
senha = str(input('ENTRE COM SENHA '))

teste = set(lista_1+lista_2)

if nome  and senha in teste:
    print(f'existe {nome} na lista 1 e 2')

else:
    print(f"Nao existe")

print(teste)

'''
    nome1 = entra_nome.get()
    senha1 = entra_senha.get()

    entrada_cred_nome.append(nome1)
    entrada_cred_senha.append(senha1)

    print(entrada_cred_nome, entrada_cred_senha,'BOTAO DE ENTRADA NOME  E SENHA ARMAZENA ')
    print(credenciais_novo_nome, credenciais_nova_senha,'BOTAO SENHA SALVA _NOVA _ARMAZENA  ')


    print(t_entrada, ' AS DUAS JUNTAS , ENTRADA')

'''