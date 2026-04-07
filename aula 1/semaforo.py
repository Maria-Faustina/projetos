print("="*4 +"\n🔴\n🟡\n🟢""\n","="*4)

semaforo = input(" Insira a cor do semaforo: ".strip().lower())

if semaforo == "verde":
    print(" Sinal Fechado 🟢")
elif semaforo == "amarelo":
    print(" Alerta de transição 🟡")
elif semaforo == "vermelho":
    print(" Sinal Aberto 🔴") 