from janela_2 import entrada1, placa


def confirma_dados():



    banco =dict()
    dados1 = list()

    banco ['id'] = entrada1.get()
    banco ['placa'] = placa.get()

    dados1.append(banco.copy())
    print(f' ESTE E O PRINTE list()  {dados1}')
    print(f' ESTE E O PRINTE dict()  {banco}')

