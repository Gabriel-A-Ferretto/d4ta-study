import requests
import pandas as pd
import streamlit as st

def obter_request(url, params=None):
    """Faz uma requisição GET e retorna a resposta em JSON"""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print(f"Erro no request {e}")
        return None
    
def frequencia_nomes(name):
    """Obtém um dicionario de frequência de um nome por decada formato {decada: quantidade}"""
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    dados_nome = obter_request(url) or []
    dados_dict =  {dados["periodo"]: dados["frequencia"] for dados in dados_nome[0].get("res", [])}
    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df


def main():
    st.title("Web App API")
    st.header("Dados da API IBGE")
    in_name = st.text_input("Digite seu nome: ")
    if not in_name:
        st.stop()
    df = frequencia_nomes(in_name)
    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        st.write("Frequência por década")
        st.dataframe(df)
    with col2:
        st.write("Série temporal")
        st.line_chart(df)

if __name__ == "__main__":
    main()
