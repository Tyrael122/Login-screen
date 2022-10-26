import os
from tkinter import messagebox
from FunctionsManageUsers import *


def manageUsers(login, password, mode):
    '''mode 0 is the 'login in mode', mode 1 is the 'sign in mode'''
    with open("usuarios.csv", "a+") as base_dados:
        base_dados.seek(0)  # Seta o cursor para o começo do arquivo
        dic = {}
        # Verifica se a base de dados existe ou não.
        if os.stat("usuarios.csv").st_size != 0:
            # Se sim (base de dados é diferente de 0), leremos o arquivo .csv e criamos um dicionário a partir dele
            for line in base_dados.readlines()[1:]:
                data = line.split(";")
                dic[data[0]] = data[1].strip("\n")
        if mode == 0:
            if dic.get(login) != None:
                dados = dic.get(login)
                if password == dados:
                    messagebox.showinfo(
                        title="", message="Logado com sucesso!")
                    opcao = perguntar()
                    while opcao == 'I' or opcao == 'P' or opcao == 'E' or opcao == 'L':
                        if opcao == 'I':
                            inserir(dic)
                        elif opcao == 'P':
                            pesquisar(dic)
                        elif opcao == 'E':
                            deletar(dic)
                        elif opcao == 'L':
                            listar(dic)
                        opcao = perguntar()
            else:
                messagebox.showwarning(
                    title="", message="Login inválido! Login não existe!")
        else:
            # Chama a funçao para cadastrar o usuário.
            inserir(dic, login, password)
