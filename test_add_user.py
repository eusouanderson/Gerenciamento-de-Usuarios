import requests
import json

# URL do endpoint JSON
url = 'https://server-2ht4.onrender.com/api/usuarios/adicionar'

# Dados no formato JSON 
data = {
    'name': 'Helena',
    'email': 'helena@outlook.com',
    'password': '123',
    
}

# Converter os dados para JSON
json_data = json.dumps(data)

# Definir os cabeçalhos da requisição
headers = {'Content-Type': 'application/json'}

# Enviar a requisição POST com os dados JSON para o link
response = requests.post(url, data=json_data, headers=headers)

# Verificar o resultado da requisição
if response.status_code == 200:
    print("JSON enviado com sucesso!")
else:
    print("Erro ao enviar o JSON. Código de resposta:", response.status_code)
    print("Resposta:", response.text)
