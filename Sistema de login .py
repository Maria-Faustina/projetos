print("="*20 + "🔒 Sistema de Cadastro Da Augostinhos moveis.corp " + "="*20)
email_validos = "@gmail.com" or "@hotmail.com"

def Validação_Email(email_validos):
  while True:
   email_certo = str(input(" Insira uma email de sua preferencia: "))
   if email_certo not in email_validos:
    print(" Email invalido! ")
    email_certo = str(input(" Insira uma email de sua preferencia: "))
   break
  return email_validos

def Validação_Usuario(email_validos):
  while True:
   email_certo = str(input(" Insira uma email de sua preferencia: "))
   if email_certo not in email_validos:
    print(" Email invalido! ")
    email_certo = str(input(" Insira uma email de sua preferencia: "))
   break
nome_certo = str(input(" Escolha seu nome de usuário: "))
senha_certo = str(input(" Escolha sua senha: "))
cont = 3

print("="*20 + "🔒 Login Da Augostinhos moveis.corp " + "="*20)

for tentativa in range(1,4):
 email_usuario = str(input(f" Digite seu email (tentativas {cont}): "))
 nome_usuario = str(input(f" Digite seu nome (tentativas {cont}): "))
 senha_usuario = str(input(f" Digite sua senha (tentativas {cont})"))
 if nome_certo ==  nome_usuario and senha_usuario == senha_certo and email_certo == email_usuario :
   print(f" Olá, {nome_usuario}! Tudo Bem? ")
   break
 elif nome_certo or senha_certo or email_certo != nome_usuario or nome_certo or email_usuario:
   cont = cont-1

if tentativa == 3:
   print(" Tentativas Acabadas conta excluida!")