from flask import *
from services.aluno_service import *
from datetime import datetime
from sqlalchemy.exc import *

app = Flask(__name__)

#----------------------
# ENDPOINTS ALUNO
#----------------------

@app.route('/alunos', methods=['POST'])
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
    
@app.route('/alunos')
def select_alunos():
    try:
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

@app.route('/alunos/<int:id>')
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

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete(id: int):
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