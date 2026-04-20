portas = [80, 443, 22]
servicos = ["http", "https", "ssh"]
for porta, servico in zip(portas, servicos):
    print(f"Porta {porta} → {servicos}")
    