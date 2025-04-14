import requests

res = requests.get("http://localhost:8000/usuarios/")

data = res.json()

print(data[0]['nome'])