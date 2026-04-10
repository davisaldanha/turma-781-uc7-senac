from app.models.models import *
from app.database.database import SessionaLocal
from datetime import date

class EmprestimoService:

    session = SessionaLocal()

    @classmethod
    def create(cls, aluno_id, livro_id):
        cls.session.query(Aluno).where(Aluno.id == aluno_id).one()
        cls.session.query(Livro).where(Livro.id == livro_id).one()

        emprestimo = Emprestimo(aluno_id = aluno_id, livros_id = livro_id, data_retirada = date.today())

        cls.session.add(emprestimo)
        cls.session.commit()

        return 'Empréstimo realizado com sucesso!'
    
    @classmethod
    def find_by_id(cls, id: int):
        result = cls.session.query(Emprestimo).where(Emprestimo.id == id).one()

        return result.to_dict()
    
    @classmethod
    def finish(cls, id: int):
        cls.session.execute(update(Emprestimo).where(Emprestimo.id == id).values(data_devolucao = date.today()))
        cls.session.commit()

        return "Empréstimo finalizado com sucesso!"
    
    @classmethod
    def find_all(cls):
        emprestimos = cls.session.query(Emprestimo).all()

        result = []

        for e in emprestimos:
            result.append(e.to_dict())
        
        return result

    '''
        # --- Backlog --- #
        1 - empréstimos por aluno
        2 - empréstimos por períodos de datas
    '''
