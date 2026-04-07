import webbrowser
nome_usuario = input(" Insira seu nome: ").strip().lower()
idade_usuario = int(input(" Insira sua idade: "))

if idade_usuario >= 18:
    print(" Direcionando para o site...")
    webbrowser.open("https://www.youtube.com/watch?v=XqGOd-G6L_4&list=RDXqGOd-G6L_4&start_radio=1")
else: 
    print(f"{nome_usuario} você não é sigma sufuciente para isso, espere mais ")