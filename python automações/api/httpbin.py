import requests

# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"

data = {
    "pessoa":{
        "nome": "Gabriel",
        "profissao": "DevOps"
    }
}

params = {
    "dataIni": "2026-01-01",
    "dataFim": "2025-12-31"
}

# response = requests.get(url)
response = requests.post(url, json=data, params=params)
print(response)
print(response.request)
print(response.text)
