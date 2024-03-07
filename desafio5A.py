USUARIO = "admin"
SENHA = "admin123"


def isAdmin(login, senha):
    if (login == USUARIO and senha == SENHA):
        return True
    else:
        return False


def imprimeLogin(verifica):
    if verifica:
        print(" Ola Admin, seja bem-vindo ")
    else:
        print(" Erro ")


def main():
    login = input(" Digite seu login: ")
    senha = input(" Digite sua senha: ")

    imprimeLogin(isAdmin(imprimeLogin, senha))

    verifica = isAdmin(login, senha)
    if verifica == True:
        print(" Ola Admin, Seja Bem-Vindo !! ")
    else:
        print(" Erro ")

    if __name__ == "__main__":
    main()
