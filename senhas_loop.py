usuario_cadastrado = "Jorge"
senha_cadastrada = "121822"

tentativas = 0
acesso_concedido = False

while acesso_concedido == False and tentativas < 3:
    usuario_digitado = input("Usuário: ")
    senha_digitada = input("Senha: ")
    if usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada:
        print(f"Bem-vindo!! {usuario_cadastrado}!")
        acesso_concedido = True

    else:
        tentativas = tentativas + 1
        chances_restantes = 3 - tentativas
        print(f"Errado!!! Você ainda tem {chances_restantes} chances!")

if acesso_concedido == False:
    print(f"SISTEMA BLOQUEADO! Procure seu ADM!!")