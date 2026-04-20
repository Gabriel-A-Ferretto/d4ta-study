import time
import threading
import random

# Simulação de serviço (substitua depois)
def checar_servico():
    return random.choice(["online", "online", "online", "offline"])

def escanear():
    print("🔎 Escaneando sistema...")
    time.sleep(2)
    print("✔ Escaneamento concluído")

def gerar_relatorio():
    print("📄 Gerando relatório...")
    time.sleep(2)
    print("✔ Relatório pronto")

# Monitoramento em paralelo
def monitorar():
    while True:
        status = checar_servico()
        if status == "offline":
            print("\n🚨 Serviço caiu! ALERTA!")
            break
        print("✅ OK — aguardando...")
        time.sleep(5)

# Thread para não travar o menu
monitor_thread = threading.Thread(target=monitorar, daemon=True)
monitor_thread.start()

# Menu interativo
while True:
    try:
        opcao = input("\n[1] Escanear  [2] Relatório  [0] Sair\n> ")

        if opcao == "0":
            print("Saindo...")
            break
        elif opcao == "1":
            escanear()
        elif opcao == "2":
            gerar_relatorio()
        else:
            print("❌ Opção inválida")

    except KeyboardInterrupt:
        print("\nEncerrando...")
        break