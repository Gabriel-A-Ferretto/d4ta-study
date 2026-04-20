def analisar_evento(evento):
    nivel     = evento.get("nivel")
    origem    = evento.get("origem")
    tentativas = evento.get("tentativas", 0)

    if nivel == "CRITICAL":
        print(f"[ALERTA CRÍTICO] Origem: {origem} — escalar imediatamente")
    elif nivel == "HIGH" and tentativas > 10:
        print(f"[POSSÍVEL BRUTE FORCE] {tentativas} tentativas de {origem}")
    elif nivel == "HIGH":
        print(f"[ALERTA ALTO] Investigar: {origem}")
    elif nivel in ("MEDIUM", "LOW"):
        print(f"[INFO] Registrado — nível {nivel} de {origem}")
    else:
        print("[DESCONHECIDO] Evento sem nível definido")

# Teste
analisar_evento({"nivel": "HIGH", "origem": "10.0.0.5", "tentativas": 15})
# Saída: [POSSÍVEL BRUTE FORCE] 15 tentativas de 10.0.0.5