import requests

# URL do endpoint JSON
url = 'https://server-2ht4.onrender.com/api/usuarios/adicionar'

# Dados no formato JSON 
data = {
    'name': 'José Pereira',
    'email': 'jose@example.com',
    'password': 'senha3',
    'sector': 'mecanico',
    'phone': '11955443322'
}

# Enviar a requisição POST com os dados JSON para o link
response = requests.post(url, json=data)

# Verificar o resultado da requisição
if response.status_code == 200:
    print("JSON enviado com sucesso!")
else:
    print("Erro ao enviar o JSON. Código de resposta:", response.status_code)
    print("Resposta:", response.text)
