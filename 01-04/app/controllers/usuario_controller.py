from flask import *
from app.services.usuario_service import *
from datetime import datetime
from sqlalchemy.exc import *
from app.validations.validations import *
from flask_jwt_extended import *


usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuarios')

@usuario_bp.route('/cadastro', methods=['POST'])
def create_usuario():
    try:
        usuario = request.json

        valid_password(usuario.get('password'))

        return jsonify({'message': UsuarioService.create(usuario)}), 201
    except PasswordLengthError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro ao cadastrar o usuário.'}), 500
    
@usuario_bp.route('/login', methods=['POST'])
def login_usuario():
    try:
        username = request.json.get('username')
        password = request.json.get('password')

        if not username or not password:
            return jsonify({'error': 'Username e senha são obrigatórios.'}), 400
        
        if UsuarioService.login(username, password):
            access_token = create_access_token(identity=username)
            return jsonify({'message': 'Login realizado com sucesso',
                            'access_token': access_token}), 200
        else:
            return jsonify({'error': 'Credenciais inválidas.'}), 401
    except UserNotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Ocorreu um erro ao realizar o login.'}), 500
