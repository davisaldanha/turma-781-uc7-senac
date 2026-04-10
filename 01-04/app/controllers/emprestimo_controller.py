from flask import *
from app.services.emprestimo_service import *
from sqlalchemy.exc import *
from datetime import datetime

emprestimo_bp = Blueprint('emprestimo', __name__, url_prefix='/emprestimos')

@emprestimo_bp.route('/')
def select_emprestimos():
    try:
        result = EmprestimoService.find_all()

        return  jsonify({
                    "message": "Empréstimos cadastrados!",
                    "data": result,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 201
    except Exception as e:
         return jsonify({
                    "message": f"{e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500
    
@emprestimo_bp.route('/<int:id>')
def select_by_id_emprestimos(id: int):
    try:

        result = EmprestimoService.find_by_id(id)._to_dict()

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
    except (SQLAlchemyError, Exception) as e:
        return jsonify({
                    "message": f"Erro interno no servidor: {e}",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 500

@emprestimo_bp.route('/', methods=['POST'])
def create_emprestimo():
    try:
        emprestimo = request.json

        result = EmprestimoService.create(emprestimo['aluno_id'], emprestimo['livro_id'])

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

@emprestimo_bp.route('/finalizar', methods=['PUT'])
def finish_emprestimo():
    try:
        result = EmprestimoService.finish()        

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


