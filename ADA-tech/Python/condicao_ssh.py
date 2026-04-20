# Checando se o valor está em um conjunto
servico = "ssh"
if servico in ["http", "https", "ssh", "ftp"]:
    print(f"Serviço {servico.upper()} reconhecido")
else:
    print("Não encontrado \n 404")