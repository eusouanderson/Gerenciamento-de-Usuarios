from collections import UserString
from flask import Flask, jsonify, request
from bd import read_users, save_user, delete_users

app = Flask(__name__)

# Lista de usuarios importado do banco de dados
usuarios = read_users()

# Endpoint para obter a lista completa de usuários .
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = read_users()
    return jsonify(usuarios)

# Endpoint para obter informações de um usuário específico pelo ID
@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):

    usuarios = read_users()
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    
# Endpoint para deletar usuário pelo ID, ou 0 para apagar todos
@app.route('/api/usuarios/delete/<int:usuario_id>', methods=['GET']) 
def delete(usuario_id):
    
    
    delete_users(usuario_id)
    
    usuarios = read_users()
    if usuarios:
        return jsonify(usuarios)
    else:
        return "Lista de usuarios vazia"

# Endpoint para adicionar usuários 
@app.route('/api/usuarios/adicionar/', methods=['POST', 'GET'])
def add_users():
    try:
        data = request.get_json()
        if 'name' in data and 'email' in data and 'password' in data:
            user_name = data['name']
            user_email = data['email']
            user_password = data['password']
            phone = data['phone']
            user_sector = data['sector']
        save_user(name= user_name, email= user_email, password= user_password, sector=user_sector, phone=phone)
        return jsonify({'message': 'Usuário adicionado com sucesso!'})
    except:
        return jsonify({'error': 'Dados inválidos. Certifique-se de enviar name, email, password, phone e sector no corpo da requisição.' }), 400
    finally:
        usuarios = read_users()
        return jsonify(usuarios)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)