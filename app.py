from collections import UserString
from flask import Flask, jsonify
import time
import subprocess
from bd import read_users, save_user, delete_users

app = Flask(__name__)

# Lista de usuarios importado do banco de dados
usuarios = read_users()

# Endpoint para obter a lista completa de usuários
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

# Endpoint para obter informações de um usuário específico pelo ID
@app.route('/api/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuario = next((user for user in usuarios if user['id'] == usuario_id), None)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404
    
# Endpoint para deletar usuário pelo ID, ou 0 para apagar todos
@app.route('/api/usuarios/delete/<int:usuario_id>', methods=['GET']) 
def delete(usuario_id):
    delete_users(usuario_id)
    if usuarios:
        return jsonify(usuarios)
    else:
        return "Lista de usuarios vazia"

# Endpoint para adicionar usuários 
@app.route('/api/usuarios/adicionar/<string:usuario_name>', methods=['POST', 'GET'])
def add_users(usuario_name):
    save_user(name=usuario_name, email='eusouanderson', password='123')
    updateBD()
    return jsonify(usuarios)

def updateBD():
    
    try:
        users = read_users()
    except Exception as e:
        print(f"Erro a atualizar BD {e}")
    finally:
        del users


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)