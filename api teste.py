
import  requests


url = 'http://economia.awesomeapi.com.br/json/last/USD-BRL'
formato = '/json/'

bitcoin = input('Entre: enter ')
resposta = requests.get(url)


if(resposta.status_code == 200):
 print()
 print('JSON : ', resposta.json())
 print()
 #print(f'DOLA HOJE : {}')

else:
 print('Nao houve sucesso na requisicao.')