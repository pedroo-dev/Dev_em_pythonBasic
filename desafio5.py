# Peça ao usuário para inserir um nome de usuário e uma senha.
# Verifique se o nome de usuário é "admin" e a senha é "admin123".
# Exiba uma mensagem de boas-vindas se as credenciais estiverem
# corretas, caso contrário, exiba uma mensagem de erro.

USUARIO = "admin"
SENHA = "admin123"

def isAdmin(login, senha):
    if (login == USUARIO and senha == SENHA):
        return True
    else:
        return False

def main ():
    login = input(" Digite seu login: ")
    senha = input(" Digite sua senha: ")

    verifica = isAdmin(login, senha)
    if verifica == True:
        print(" Ola Admin, Seja Bem-Vindo !! ")
    else:
        print(" Erro ")


if __name__ == "__main__":
    main()






