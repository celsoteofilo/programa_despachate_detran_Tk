
from main import entrada_cep, texto_cadastro
from funcao_chamar_pag_cep import *

def cep_busca():
    import requests

    cep = entrada_cep.get()

    cep = cep.replace("-", "").replace(".", "").replace(" ", "")

    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'

        requisicao = requests.get(link)

        print(requisicao)

        dic_requisicao = requisicao.json()

        uf = dic_requisicao['uf']
        cidade = dic_requisicao['localidade']
        bairro = dic_requisicao['bairro']
        logradouro = dic_requisicao['logradouro']
        complemento = dic_requisicao['complemento']

        print(dic_requisicao)
    else:
        print("CEP Inválido")


    texto_cep = f'''
   
    CEP INFORMADO : {cep}
    RUA: {logradouro}
    BAIRRO : {bairro}
    CIDADE :  {cidade}
    COMPLEMENTO {complemento}
    UF : {uf}
   
    '''
    texto_cadastro["text"] = texto_cep
