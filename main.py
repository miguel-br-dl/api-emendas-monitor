import requests
import pandas as pd
import argparse
from datetime import date


BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados/emendas"

def get_ano_corrente():
    """
        Assume o ano corrente, caso não seja passado como parâmetro
    """
    ano_atual = date.today()
    return ano_atual.strftime('%Y')

def executar_api(token, pagina=1, ano=get_ano_corrente()):
    """
        Executa de fato a API, retorna os dados paginados
    """
    headers = {
        "chave-api-dados": token
    }

    params = {
        "pagina": pagina,
        "ano": ano
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"Erro na API: {response.status_code} - {response.text}")

    return response.json()


def filtrar_dados(data, funcao):
    """
        Realiza um filtro simples pela função da emenda parlamentar, 
        exemplo: urbanismo
    """
    filtered = []

    funcao = funcao.lower()

    for item in data:
        descricao = (item.get("funcao") or "").lower()

        if funcao in descricao:
            filtered.append({
                "codigoEmenda": item.get("codigoEmenda"),
                "ano": item.get("ano"),
                "autor": item.get("autor"),
                "numeroEmenda": item.get("numeroEmenda"),
                "localidadeDoGasto": item.get("localidadeDoGasto"),
                "funcao": item.get("funcao"),
                "subfuncao": item.get("subfuncao"),
                "valorEmpenhado": item.get("valorEmpenhado"),
                "valorLiquidado": item.get("valorLiquidado"),
                "valorEmpenhado": item.get("valorEmpenhado"),
                "valorPago": item.get("valorPago")               
            })

    return filtered


def salvar_csv(data, funcao):
    """
        Armazena os dados filtrados em arquivo CSV (que pode virar Excel)
    """
    df = pd.DataFrame(data)

    filename = f"emendas_{funcao}.csv"
    df.to_csv(filename, index=False)

    print(f"Arquivo gerado: {filename}")


def main():
    parser = argparse.ArgumentParser(description="Filtrar emendas parlamentares por ano")
    parser.add_argument("--token", required=True, help="Token da API")
    parser.add_argument("--ano", required=False, help="Ano da busca")
    parser.add_argument("--pagina", required=False, help="Página do dado")
    parser.add_argument("--funcao", required=False, help="Função da emenda a filtrar, ex: urbanismo")

    args = parser.parse_args()

    ano = args.ano if args.ano else get_ano_corrente()
    pagina = args.pagina if args.pagina else 1
    
    print("Buscando dados da API...")
    data = executar_api(args.token, ano=ano, pagina=pagina)

    funcao_str = args.funcao if args.funcao else ''
    print("Filtrando dados por função da emenda...")
    filtrado = filtrar_dados(data, funcao_str)

    if not filtrado:
         print("Nenhum resultado encontrado.")
         return

    print(f"{len(filtrado)} resultados encontrados.")

    print("Gerando CSV...")
    salvar_csv(filtrado, funcao_str)
    

if __name__ == "__main__":
    main()
