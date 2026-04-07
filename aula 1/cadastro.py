import time
usuario_correto = "Moveis.corp"
senha_correta = "mdf123"

print("="*10 + " 🔒︎ Sistema de Login da agostinho moveis enterprise " + "="*10)

usuario = input(" Insira o  nome de usuario: ")
senha = input(" Insira a senha de usuario: ")

if usuario == usuario_correto or senha == senha_correta:
    print(f" Login feito com sucesso,  seja bem vindo {usuario_correto}")
elif usuario != usuario_correto or usuario != usuario_correto:
    print("\n Detectamos um hacker invadindo a conta! ")
    print("\n Excluindo a conta em: ")
    print("\n 1 ")
    time.sleep(1)
    print("\n 2 ")
    time.sleep(1)
    print("\n 3 ")
    time.sleep(1)
    print(" Exclusão feita com sucesso! ")

