# Documentação do Backend de Gerenciamento de Usuários

Este é um exemplo de aplicativo Flask que implementa um backend para gerenciar usuários. Ele fornece endpoints para obter a lista de usuários, obter informações de um usuário específico, adicionar usuários e deletar usuários através de requisições HTTP.

## Instalação e Configuração

1. Certifique-se de ter o Python instalado em seu sistema. Caso ainda não o tenha, faça o download e a instalação em [python.org](https://www.python.org).

2. Instale o Flask, uma biblioteca necessária para executar o backend:

~~~
pip install Flask

~~~


3. Clone este repositório para obter o código do projeto:

~~~
git clone https://github.com/eusouanderson/Gerenciamento-de-Usuarios

~~~


4. Após a clonagem, navegue para o diretório do projeto:

~~~
cd Gerenciamento-de-Usuarios

~~~


5. Execute o aplicativo:

~~~ 
python app.py

~~~



6. O servidor Flask estará em execução e pronto para receber solicitações na porta 5000.

## Endpoints

### Obter Lista de Usuários

Endpoint: `/api/usuarios` (método GET)

Descrição: Este endpoint retorna a lista completa de usuários existentes.

Exemplo de solicitação:

~~~
GET http://localhost:5000/api/usuarios

~~~


Exemplo de resposta:

```json

    {
        "id": 1,
        "name": "João da Silva",
        "email": "joao@example.com",
        "password": "senha1"
    },
    {
        "id": 2,
        "name": "Maria Souza",
        "email": "maria@example.com",
        "password": "senha2"
    }
    // mais usuários...
```


Obter Informações de um Usuário Específico

Endpoint: /api/usuarios/<int:usuario_id> (método GET)

Descrição: Este endpoint retorna informações de um usuário específico com base no usuario_id fornecido na URL.

Exemplo de solicitação:


```json

GET http://localhost:5000/api/usuarios/1

```

Exemplo de resposta:

```json
{
    "id": 1,
    "name": "João da Silva",
    "email": "joao@example.com",
    "password": "senha1"
}
```

Deletar Usuário

```json

Endpoint: /api/usuarios/delete/<int:usuario_id> (método GET)

```

Descrição: Este endpoint é usado para deletar um usuário com base no usuario_id fornecido na URL. Se o usuario_id for 0, todos os usuários serão deletados.

Exemplo de solicitação:

```json

GET http://localhost:5000/api/usuarios/delete/1

```

Exemplo de resposta:


```json

{
    "id": 2,
    "name": "Maria Souza",
    "email": "maria@example.com",
    "password": "senha2"
}
// mais usuários restantes...

```

Adicionar Usuário

```json
Endpoint: /api/usuarios/adicionar/ (método POST)

```

Descrição: Este endpoint é usado para adicionar novos usuários à lista. Os detalhes do usuário (name, email e password) são enviados no corpo da requisição como dados JSON.

Exemplo de solicitação:

POST http://localhost:5000/api/usuarios/adicionar/
Content-Type: application/json

```json
{
    "name": "José Pereira",
    "email": "jose@example.com",
    "password": "senha3"
}

```

Exemplo de resposta:

```json
{
    "message": "Usuário adicionado com sucesso!"
}
```