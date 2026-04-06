from flask import *
from services.aluno_service import *
from datetime import datetime

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

