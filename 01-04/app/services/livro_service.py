from app.models.models import *
from app.database.database import SessionaLocal
from datetime import date

class LivroService:

    session = SessionaLocal()

    @classmethod
    def create(cls, livro: dict) -> str:
        '''
        Realiza o cadastro do livro no banco de dados.

        Args:
            livro (dict): livro que será cadastrado

        Return:
            Mensagem com a confirmação do cadastro realizado.
        '''
        n_livro = Livro(**livro)
        cls.session.add(n_livro)
        cls.session.commit()

        return "Livro cadastrado com sucesso!"
    
    @classmethod
    def find_all(cls) -> list:
        '''
        Retorna os livros cadastrados.

        '''
        livros = cls.session.query(Livro).all()

        result = []

        for l in livros:
            result.append(l.to_dict())
        
        return result
    
    @classmethod
    def find_is_ativo(cls) -> list:
        '''
        Retorna todos os livros com status ativado.
        '''
        livros = cls.session.query(Livro).where(Livro.ativo == True).all()

        result = []

        for l in livros:
            result.append(l.to_dict())
        
        return result
    
    @classmethod
    def find_is_not_ativo(cls) -> list:
        '''
        Retorna todos os livros com status desativado.
        '''
        livros = cls.session.query(Livro).where(Livro.ativo == False).all()

        result = []

        for l in livros:
            result.append(l.to_dict())
        
        return result
    
    @classmethod
    def disable(cls, id: int) -> str:
        '''
        Altera o status de um livro para desativado. 
        Retorna uma exceção `NoResultFound` caso o id corresponda a nenhum livro.

        Args:
            id (int): id do livro

        Return:
            Mensagem de confirmação, livro desativado.
        '''
        cls.session.query(Livro).where(Livro.id == id).one()
        cls.session.execute(update(Livro).where(Livro.id == id).values(ativo = False))
        cls.session.commit()

        return 'Livro desativado com sucesso!'
    
    @classmethod
    def find_by_id(cls, id: int) -> Livro:
        '''
        Retorna o livro correspondente ao id.
        Retorna uma exceção `NoResultFound` caso o id corresponda a nenhum livro.

        Args:
            id (int): id do livro

        Return:
            Objeto `Livro`.
        '''
        livro = cls.session.query(Livro).where(Livro.id == id).one()
        return livro.to_dict()
    
    @classmethod
    def update(cls, id: int, livro: dict) -> str:
        '''
        Atualiza um objeto livro cadastrado.
        Retorna uma exceção `NoResultFound` caso o id corresponda a nenhum livro.

        Args:
            id (int): id do livro
            livro (dict): dicionário com os dados do livro

        Return:
            Mensagem de confirmação da modificação do objeto.
        '''
        cls.session.query(Livro).where(Livro.id == id).one()
        cls.session.execute(update(Livro).where(Livro.id == id).values(livro))
        cls.session.commit()

        return 'Livro atualizado com sucesso!'
    
    @classmethod
    def find_by_fields(cls, fields: dict) -> Any:
        '''
            Retorna os livros filtrados pelos atributos.

            Args:
                fields (dict): atributos para serem filtrados
            
            Return:
                Livros cadastrados
        '''
        sql = 'SELECT * FROM livros WHERE '

        _length = len(fields.items())
        _cont = 0

        for k, v in fields.items():
            _cont += 1

            if 'ano_publicacao' in k and _cont == _length:
                sql += f"{k} = {v}"
                continue
            elif 'ano_publicacao' in k:
                sql += f"{k} = {v} AND "
                continue

            if _cont == _length:
                sql += f"{k} LIKE '%{v}%'"
                break

            sql += f"{k} LIKE '%{v}%' AND "

        con = cls.session.connection()            
            
        return [i for i in con.exec_driver_sql(sql)]
