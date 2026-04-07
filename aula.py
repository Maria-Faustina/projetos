
print("="*20 + " Lanchonete Senai " + "="*20)

nome_cliente = str(input(" Por favor, Insira seu nome: "))

print("="*20 + " Nosso Cardapio " + "="*20)
print("\n1. Hamburguer 20.50")
print("\n2. Refri 10.0")
print("="*57)

print("="*20 + " Faça seu pedido "+ "="*20)
total_burge = int(input(" Insira a Quantidade de Hamburgueres: "))
total_refri = int(input(" Insira a quantidade de refris: "))

preco_burgue = float(20.50)
preco_refri = float(10.0)

total = total_burge + total_refri
total_preco = (total_burge)*(preco_burgue) + (total_refri)*(preco_refri)
print("-"*20 + " Cupom Fiscal"+ "-"*20)
print(f" Total de itens: {total} \n Preço = {total_preco} \n {nome_cliente} foi um prazer atender!")
