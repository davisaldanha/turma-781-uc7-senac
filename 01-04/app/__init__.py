from flask import *
from app.controllers.aluno_controller import aluno_bp
from app.controllers.livro_controller import livro_bp
from app.controllers.emprestimo_controller import emprestimo_bp
from app.controllers.usuario_controller import usuario_bp
from flask_jwt_extended import JWTManager
from config import config
from datetime import timedelta

api_bp = Blueprint('api', __name__, url_prefix='/api')
api_bp.register_blueprint(aluno_bp)
api_bp.register_blueprint(livro_bp)
api_bp.register_blueprint(emprestimo_bp)
api_bp.register_blueprint(usuario_bp)

#Gerenciador do JWT
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    #Configurações da chave secreta para o JWT e o tempo de expiração dos tokens
    app.config['JWT_SECRET_KEY'] = config.secret_key
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)

    #Inicializa o JWT com a aplicação
    jwt.init_app(app)

    #Registrar o blueprint pai no app
    app.register_blueprint(api_bp)

    return app