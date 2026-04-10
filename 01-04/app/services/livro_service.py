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
        return livro
    
    @classmethod
    def update(cls, id: int, livro: dict) -> str:
        '''
        Atualiza um objeto livro cadastrado.
        Retorna uma exceção `NoResultFound` caso o id corresponda a nenhum livro.

        Args:
            id (int): id do livro
            livro (dict): dicionário com os dados do livro

        Return:
            Objeto `Livro`.
        '''
        cls.session.query(Livro).where(Livro.id == id).one()
        cls.session.execute(update(Livro).where(Livro.id == id).values(livro))
        cls.session.commit()

        return 'Livro atualizado com sucesso!'
    
    @classmethod
    def find_by_fields(cls, fields: dict) -> list:
        '''
            Retorna os livros filtrados pelos atributos.

            Args:
                fields (dict): atributos para serem filtrados
            
            Return:
                Livros cadastrados
        '''
        result = []
        for k, v in fields.items():
            match k:
                case 'titulo':
                    livros = cls.session.query(Livro).where(Livro.titulo == v).all()
                    
                    for l in livros:
                        result.append(l.to_dict())

                    return result

                case 'autor':
                    livros = cls.session.query(Livro).where(Livro.autor == v).all()
                    
                    for l in livros:
                        result.append(l.to_dict())
                    
                    return result
                
                case 'ano_publicação':
                    livros = cls.session.query(Livro).where(Livro.ano_publicacao == v).all()
                    
                    for l in livros:
                        result.append(l.to_dict())
                    
                    return result
                
                case 'isbn':
                    livros = cls.session.query(Livro).where(Livro.isbn == v).all()
                    
                    for l in livros:
                        result.append(l.to_dict())
                    
                    return result
                    
        
    
    