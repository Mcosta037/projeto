import requests

url =requests.get("https://economia.awesomeapi.com.br/last/EUR-USD")

cotacao =url.json()
cotacao_dolar =float(cotacao['EURUSD']['bid'])
print(cotacao_dolar)
