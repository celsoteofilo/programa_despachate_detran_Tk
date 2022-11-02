


'''
def sacola():
    for x in range(3):
    item = input('Entre com o iten: ')
        sacola = []
        lista = item.get()
        sacola.append((lista))
    print(sacola)



def autenticar(nomes,senhas,nome,senha):
  return nomes[0]==nome and senhas[0]==senha

def cadastrar(nomes,senhas):
  nome=input("Digite nome do usuário para novo cadastra")
  senha=input("Digite senha para novo cadastra")
  nomes.append(nome)
  senhas.append(senha)
  print("Usuário cadastrado")
nomes=[0]
senhas=[0]
nome=input("Digite o nome: ")
senha=input("Digite a senha: ")
if(autenticar(nomes,senhas,nome,senha)):
  print('Valido')
else:
  print("Usuário não cadastrado")
  opcao=input("Deseja cadastrar, se sim digite 1, senão digite não")
  if(opcao=='1'):
    cadastrar(nomes,senhas)
    print(nomes,senhas)

'''