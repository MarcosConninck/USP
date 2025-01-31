import requests

response = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
data = response.json()
dolar_tax = data['USDBRL']['bid']
print(f'taxa do dolar: {dolar_tax}')
print(response.status_code)
