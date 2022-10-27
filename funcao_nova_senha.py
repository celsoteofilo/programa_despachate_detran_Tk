from tkinter import messagebox

def verificar_senha():

    nome = E_nome.get()
    senha = E_senha.get()

    if nome == "Lucas" and senha == "123456789":
     messagebox.showinfo('login,comfirmado seja bem vindo Lucas')
    elif credenciais [0] == nome and credenciais  [1]  == senha:
      messagebox.showinfo( 'seja bem vindo de volta' + credenciais [0])

    else:
        messagebox.showwarning('Erro verifiqu a senha e o nome')
