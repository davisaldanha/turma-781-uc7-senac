from flask import *
from sqlalchemy.exc import *
from datetime import datetime
from app.services.livro_service import *
from flask_jwt_extended import *

livro_bp = Blueprint('livro', __name__, url_prefix='/livros')

@livro_bp.route('/', methods=['POST'])
@jwt_required()
def create_livro():

    try:
        livro = request.json
        result = LivroService.create(livro)
        return jsonify({
                        "message": f"{result}",
                        "data": None,
                        "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                    }), 201
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

@livro_bp.route('/')
@jwt_required()
def select_livro():
    try:
        result = LivroService.find_all()
        current_user =get_jwt_identity()
        return jsonify({
                    "message": "Livros cadastrados no sistema!",
                    "data": f"{result}",
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S"),
                    "current_user": f"{current_user}"
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

@livro_bp.route('/<int:id>')
@jwt_required()
def select_by_id_livro(id):
    try:
        result = LivroService.find_by_id(id)
        return jsonify({
                    "message": "Livros cadastrados no sistema!",
                    "data": f"{result}",
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

@livro_bp.route('/ativo')
@jwt_required()
def select_is_ativo_livro():
    try:
        result = LivroService.find_is_ativo()
        return jsonify({
                    "message": "Livros com status ativado!",
                    "data": f"{result}",
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

@livro_bp.route('/desativado')
@jwt_required()
def select_is_not_ativo_livro():
    try:
        result = LivroService.find_is_not_ativo()
        return jsonify({
                    "message": "Livros com status ativado!",
                    "data": f"{result}",
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500
    
@livro_bp.route('/<int:id>', methods=['PATCH'])
@jwt_required()
def disable_livro(id):
    try:
        result = LivroService.disable(id)
        return jsonify({
                    "message": f"{result}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500
    
@livro_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_livro(id):
    try:
        up_livro = request.json

        result = LivroService.update(id, up_livro)

        return jsonify({
                    "message": f"{result}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 

@livro_bp.route('/fields')
@jwt_required()
def select_by_fields():
    try:
        
        fields = request.args.to_dict()
        
        result = LivroService.find_by_fields(fields)

        return jsonify({
                    "message": "Livros cadastrados no sistema!",
                    "data": f"{result}",
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500