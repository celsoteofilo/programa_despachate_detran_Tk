from main import entrada, entrada_cep, placa_veiculo, entrada_chassi, botao_combobox, banco_de_dados


def get_dados():


    nome= entrada.get()
    cep = entrada_cep.get()
    placa = placa_veiculo.get()
    chassi = entrada_chassi.get()
    t_veiculo = botao_combobox.get()

    banco_de_dados.append(nome,cep,placa,chassi,t_veiculo)+1


