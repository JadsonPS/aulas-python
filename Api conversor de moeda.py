import requests

url = 'https://api.exchangerate-api.com/v6/latest'

requisicao = requests.get(url)

#print(requisicao.status_code)
dados = requisicao.json()
print(dados)

valor_reais = float(input('Informe o valor em R$ a ser convertido\n'))
cotacao = dados['rates']['BRL']

print(f'R${valor_reais} em dólar valem US${(valor_reais/ cotacao):.2f}')
