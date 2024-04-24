import requests

# URL do endpoint
url = 'https://jsonplaceholder.typicode.com/posts'

# Fazendo uma solicitação GET
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro ao acessar a API:', response.status_code)

