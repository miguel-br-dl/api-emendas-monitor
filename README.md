# API Emendas Parlamentares Monitor

Script em Python para coletar dados de emendas parlamentares informadas publicamente via API. Filtrar por palavra-chave na funlção da ementa parlamentar (opcional) e gerar relatórios em CSV filtrados por esta palavra-chave.

## 💡 Motivação

Acessar dados públicos é relativamente simples, mas transformá-los rapidamente em algo útil nem sempre é.

Este script automatiza esse processo, permitindo filtrar informações relevantes e gerar relatórios prontos para análise.

## 🚀 Funcionalidades

- Consumo de API pública (Portal da Transparência)
- Filtro por palavra-chave
- Exportação para CSV
- Estrutura simples e fácil de adaptar

## 🛠️ Tecnologias

- Python
- requests
- pandas

## ▶️ Como usar

1. Instale as dependências:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Execute o script (exemplo):
```bash
python main.py --token <SEU_TOKEN> --ano 2024 --funcao "saúde" 
```

Opções:

- `--token`: Token de API (obrigatório)
- `--ano`: Ano em que a emenda parlamentar foi empenhada (opcional)
- `--funcao`: Palavra-chave que representa a função da emenda parlamentar empenhada (opcional)
- `--pagina`: Página da API (opcional, padrão 1)

## 📄 Saída

Gera um arquivo `emendas_<funcao>.csv` no diretório atual com os campos:

- `codigoEmenda`
- `ano`
- `autor`
- `numeroEmenda`
- `localidadeDoGasto`
- `funcao`
- `subfuncao`
- `valorEmpenhado`
- `valorLiquidado`
- `valorEmpenhado`
- `valorPago`

## 🛠️ Requisitos

- Python 3.10+
- Token válido do Portal da Transparência (em https://portaldatransparencia.gov.br/api-de-dados)

## 🔍 Possíveis usos

- Monitoramento de oportunidades
- Análise de dados públicos
- Geração automatizada de relatórios
- Integração com outros sistemas

## 🔧 Melhorias futuras

- Suporte a paginação automática (varrer todas páginas)
- Configuração via arquivo YAML/JSON
- Suporte a múltiplas palavras-chave e filtros avançados

## 📬 Contato

Se quiser adaptar essa solução para um caso específico, fique à vontade para entrar em contato.