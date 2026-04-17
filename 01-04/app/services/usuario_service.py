from app.models.models import *
from app.database.database import SessionaLocal
from werkzeug.security import *
from app.exceptions.exceptions import *

class UsuarioService:

    session = SessionaLocal()

    @classmethod
    def create(cls, usuario: dict) -> str:
        '''
        Realiza o cadastro do usuário no banco de dados.

        Args:
            usuario (dict): usuário que será cadastrado
        
        Return:
            Mensagem com a confirmação do cadastro realizado.
        '''
        usuario['password'] = generate_password_hash(usuario.get('password'))
        n_usuario = Usuario(**usuario)
        cls.session.add(n_usuario)
        cls.session.commit()
        return "Usuário cadastrado com sucesso!"
    
    @classmethod
    def login(cls, username: str, password: str) -> bool:
        '''
        Realiza o login do usuário.

        Args:
            username (str): nome de usuário
            password (str): senha do usuário

        Return:
            True se o login for bem-sucedido, False caso contrário.
        '''

        usuario = cls.session.query(Usuario).where(Usuario.username == username).first()
        if not usuario:
            raise UserNotFoundError(username)
        elif check_password_hash(usuario.password, password):
            return True
        return False