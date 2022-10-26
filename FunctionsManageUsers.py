from tkinter import messagebox, simpledialog


def perguntar():
    opcao = simpledialog.askstring(
        "", "\nEscolha uma opção:\nP: pesquisar um usuário\nE: excluir um usuário\nL: listar usuários\n")
    return opcao


def salvar(dic):
    with open("usuarios.csv", "w") as base_dados_excel:
        dic_keys = dic.keys()
        base_dados_excel.write("Usuário;Senha\n")
        for key in dic_keys:
            info = key + ";" + str(dic.get(key)).strip("['']") + "\n"
            base_dados_excel.write(info)


def login():
    login = simpledialog.askstring("", "Digite seu login: ")
    return login


def inserir(dic, login, password):
    login_status = True
    for key in dic.keys():
        if login == key:
            messagebox.showwarning(
                title="ERRO", message="Login inválido! Login já existe!")
            login_status = False
    if login_status == True:
        dic[login] = [password]
        salvar(dic)
        messagebox.showinfo(
            title="Sucesso!", message="Seu login foi cadastrado com sucesso!")


def deletar(dic):
    key = login()
    if dic.get(key) != None:
        del dic[key]
        messagebox.showinfo(title="", message="Usuário deletado com sucesso!")
    else:
        messagebox.showwarning(title="", message="Usuário não encontrado!")
    salvar(dic)


def listar(dic):
    for chave, valor in dic.items():
        for valor_limpo in valor:
            messagebox.showinfo(
                title="", message="\nLogin: {} \nSenha: {}".format(chave, valor_limpo))


def pesquisar(dic):
    dados = dic.get(login())
    if dados != None:
        messagebox.showinfo(title="", message="Senha: {}".format(dados[0]))
    else:
        messagebox.showwarning(title="", message="Login não encontrado!")
