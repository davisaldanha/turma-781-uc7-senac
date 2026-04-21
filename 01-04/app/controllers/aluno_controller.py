from flask import *
from flask_jwt_extended import jwt_required
from app.services.aluno_service import *
from datetime import datetime
from sqlalchemy.exc import *

aluno_bp = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_bp.route('/', methods=['POST'])
@jwt_required()
def create_aluno():
    try:
        aluno = request.json
        result = AlunoService.create(aluno)
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
    
@aluno_bp.route('/')
@jwt_required()
def select_alunos():
    try:
        matricula = request.args.get('matricula')
        curso = request.args.get('curso')

        if matricula: 
            result = AlunoService.find_by_register(matricula)

            return jsonify({
                        "message": "Aluno pesquisado com sucesso!",
                        "data": f"{result}",
                        "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                    }), 200

        if curso: 
            result = AlunoService.find_by_course(curso)
            return jsonify({
                        "message": f"Alunos do curso {curso}",
                        "data": f"{result}",
                        "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                    }), 200

        result = AlunoService.find_all()
        return jsonify({
                    "message": "Alunos cadastrados no sistema!",
                    "data": f"{result}",
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except Exception as e:
        return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

@aluno_bp.route('/<int:id>')
@jwt_required()
def select_by_id_aluno(id: int):
    try:

        result = AlunoService.find_by_id(id)._to_dict()

        return jsonify({
                    "message": "Aluno encontrado com sucesso!",
                    "data": result,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except NoResultFound:
        return jsonify({
                    "message": f"Aluno não foi encontrado!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 404
    except SQLAlchemyError as e:
        return jsonify({
                    "message": f"Erro interno no servidor: {e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

@aluno_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_aluno(id: int):
    try:
        AlunoService.delete(id)

        return jsonify({
                    "message": f"Aluno removido com sucesso!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200

    except NoResultFound:
        return jsonify({
                    "message": f"Aluno não foi encontrado!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 404
    except (SQLAlchemyError, Exception) as e:
        return jsonify({
                    "message": f"Erro interno no servidor: {e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500
    
@aluno_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_aluno(id: int):
    try:
        up_aluno = request.json

        result = AlunoService.update(up_aluno, id)

        return jsonify({
                    "message": result,
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    except NoResultFound:
        return jsonify({
                    "message": f"Aluno não foi encontrado!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 404
    except (SQLAlchemyError, Exception) as e:
        return jsonify({
                    "message": f"Erro interno no servidor: {e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

    
'''
# --- Backlog --- #
Criar endpoint/serviço para pesquisar aluno por matricula
Criar endpoint/serviço para pesquisar alunos por curso
'''