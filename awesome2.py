import requests

n5 = int(input("Que moeda deseja converter 1-EUR, 2-USD, 3-BRL: "))
if n5 == 1:
    n3 = "EUR"
elif n5 == 2:
    n3 = "USD"
elif n5 == 3:
    n3 = "BRL"
else:
    print("Erro❌")
    exit()

n4 = int(input("Para que moeda deseja converter 1-Real, 2-Dólar, 3-Iene, 4-Franco Suíço, 5-Kuwaitiano: "))
if n4 == 1:
    n2 = "BRL"
elif n4 == 2:
    n2 = "USD"
elif n4 == 3:
    n2 = "JPY"
elif n4 == 4:
    n2 = "CHF"
elif n4 == 5:
    n2 = "KWD"
else:
    print("Erro❌")
    exit()

# Montagem correta da URL
url =requests.get(f"https://economia.awesomeapi.com.br/last/{n3}-{n2}")
cotacao = url.json()

print(cotacao)


