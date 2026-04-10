from flask import *
from app.controllers.aluno_controller import aluno_bp
from app.controllers.livro_controller import livro_bp
from app.controllers.emprestimo_controller import emprestimo_bp

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(aluno_bp)
api_bp.register_blueprint(livro_bp)
api_bp.register_blueprint(emprestimo_bp)

def create_app():
    app = Flask(__name__)

    #Registrar o blueprint pai no app
    app.register_blueprint(api_bp)

    return app