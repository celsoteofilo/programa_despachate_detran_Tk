import webview # importaçao da biblioteca

def janela_habilitacao():
    webview.create_window('CONSULTAR VEICULOS',
                          'https://www.detran.mg.gov.br/habilitacao/prontuario/consultar-pontuacao-cnh' #criei a janela /////title, url='', html='', js_api=None, width=800, height=600
                          , width= 800, height= 900,  # defini a altura e comprimento
                          resizable=True, # resizable=True movintar a tela e false trava tela
                          confirm_close=True,# confirm_close=True, pergunta de confirmaçao fechar janela
                          background_color='#FFA', text_select=True)
    webview.start()



