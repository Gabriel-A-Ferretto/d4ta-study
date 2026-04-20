
protocolo = "TCP"

# compara um único valor
match protocolo:
    case "TCP":
        print("Conexão orientada")
    case "UDP":
        print("Sem conexão")
    case _:
        print("Desconhecido")