

'''
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

    nome1 = entra_nome.get()
    senha1 = entra_senha.get()

    entrada_cred_nome.append(nome1)
    entrada_cred_senha.append(senha1)

    print(entrada_cred_nome, entrada_cred_senha,'BOTAO DE ENTRADA NOME  E SENHA ARMAZENA ')
    print(credenciais_novo_nome, credenciais_nova_senha,'BOTAO SENHA SALVA _NOVA _ARMAZENA  ')


    print(t_entrada, ' AS DUAS JUNTAS , ENTRADA')

'''

'''
dados  = list()
dados.append('pedro')
dados.append(25)

print(dados[0])
print(dados[1])


#________________ DICIONARIOS _________________

dados = dict()                         # foorma de chara o dicionario
dados = {'nome':'Pedro','idade':25}    #  formas de adiconar em dicionario
dados['sexo'] = 'M'                    #  aqui e  forma de adionar

dados['test'] = 'T'                    # forma de deletar um dado de um dicionario
del dados['test']


print(dados['nome'])                   # formas de printas as telas
print(dados['idade'])
print(dados['sexo'])

print(dados)


# ________________ DICIONARIO 2___________________
filme = {'titulo': 'Idiana ',
         'ano': 1977,
         'diretor' : 'George'}



print(filme['titulo'])                   # formas de printas as telas
print(filme['ano'])
print(filme['diretor'])

print(filme.values())                   # ira retornar todos valores (['Idiana ', 1977, 'George'])
print(filme.keys())                     # ira retornas as chave itens dentro(['titulo', 'ano', 'diretor'])
print(filme.items())                    # Ira retornar os 2  valores e itens ([('titulo', 'Idiana '), ('ano', 1977), ('diretor', 'George')])


for x,y in filme.items():               # Posso fazer um for me retorna    ==> O  diretor  e George
    print(f'O  {x}  e {y}')

for x in filme.keys():                  # ira retornar ==>  O diretor
    print(f' O {x}')

print(dados)


#_________________ DICIONARIO 3 _____________________________

pessoas ={'nome': 'Celso', 'idade': '40', 'sexo': 'Masculino'}
pessoas['cor'] = 'parda'

del pessoas['cor']                          # posso apagar a  item  de 'pessoas  '

pessoas['nome'] = 'cleia'                   #  poddo  Trocar o nome  'celso' para 'Cleia '



print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


print('---------------------------')
for k in pessoas.keys():
    print(k)
print('---------------------------')


for v in pessoas.values():
    print(v)
print('---------------------------')

for k,v in pessoas.items():
    print(f'{k} = {v}')
print('---------------------------')


#_________________ DICIONARIO 4 _____________________________

# DICIONARIO DENTRO DE UMA LISTA   ..

brasil = []

estado = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 ={'uf': 'Belo horizonte', 'sigla': 'MG'}


brasil.append(estado)
brasil.append(estado2)

print(estado)
print(estado2)

print('______________________________________________________')
print(brasil)
print(brasil[1])
print(brasil[0])


print('______________________________________________________')

print(brasil[0] ['uf'])
print(brasil[0] ['sigla'])


print(brasil[1] ['uf'])
print(brasil[1] ['sigla'])


print('______________________________________________________')

'''

#_________________ DICIONARIO 5 _____________________________
# DICIONARIO  ler 3 estados -- ACRESENTANDO ITENS .

estado = dict()
brasil =list()

for  c in range (1,3):
    estado ['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str (input('Sigla do Estado : '))
    brasil.append(estado.copy())
for e in brasil:
    print(e)
    for k, v in e.items():
        print(f' O Campo {k} tem valor {v}', end = " ")
