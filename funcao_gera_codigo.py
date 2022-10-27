# FUNCAO GERAR CODIGO DE REGISTRO

from main import *

from main import entrada, botao_combobox, placa_veiculo, entrada_chasssi, entrada_cep, lista_codigos, \
    lista_produto_padrao, texto_cadastro

def inserir_codigo():

    import datetime
    #criando puxada de informaçoe

    nome = entrada.get()
    veiculo = botao_combobox.get()
    placa = placa_veiculo.get()
    chassi =  entrada_chasssi.get()
    cep = entrada_cep.get()


    #puxando data e hora

    data_criacao = dt.datetime.now()
    data_criacao.strftime('%d/%m/%y--%H:%M')

    #criando um codigo

    codigo = len(lista_codigos)+1   # lendo o codigo + 1
    codigo_str = "COD-{}".format(codigo)   #  formatando o codigo
    lista_codigos.append((codigo_str,nome,placa,cep,veiculo,placa,data_criacao)) # montando a lista em seguencia
    lista_produto_padrao.append((placa,data_criacao))


    texto = f'''
            
    Pessoa Cadastrado : {nome}
    Tipo :  {veiculo}
    Placa Veiculo : {placa}
    Numero do Chassi {entrada_chasssi}
    codigo gerado: {codigo} 

    '''
    texto_cadastro["text"] = texto

