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