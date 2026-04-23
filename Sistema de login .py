print("="*20 + "🔒 Sistema de Cadastro Da Augostinhos moveis.corp " + "="*20)
def Validacao_Email(email_certo):
 while True:
     if email_certo.endswith(("@hotmail.com","@gmail.com","@hotmail.com","@yahoo.com","@outlook.com")):
          return email_certo
     else:
        email_certo = str(input(" Insira um email valido, Tente novamente!: "))
def Validacao_senha(senha_certo):
 while True:
     if len(senha_certo) >= 1 and len(senha_certo) <= 6:
       return senha_certo
     else:
        senha_certo = str(input(" Escolha seu nome de usuário: "))

email_certo = str(input(" Insira uma email de sua preferencia: "))
Validacao_Email(email_certo)

nome_certo = str(input(" Escolha seu nome de usuário: "))

senha_certo = str(input(" Escolha sua senha: "))
Validacao_senha(senha_certo)


print("="*20 + "🔒 Login Da Augostinhos moveis.corp " + "="*20)
cont = 3
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
#jdjdjdjd