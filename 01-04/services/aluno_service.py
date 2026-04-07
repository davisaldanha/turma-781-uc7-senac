from models.models import *
from database.database import SessionaLocal

class AlunoService():

    session = SessionaLocal()

    @classmethod
    def create(cls, aluno: dict) -> Any:
        n_aluno = Aluno(**aluno)
        cls.session.add(n_aluno)
        cls.session.commit()
        return 'Usuário cadastrado com sucesso!'
    
    @classmethod
    def update(cls, aluno: dict, id: int) -> Any:
        #up_aluno = Aluno(**aluno)
        cls.session.query(Aluno).where(Aluno.id == id).one()
        cls.session.execute(update(Aluno).where(Aluno.id == id).values(aluno))
        cls.session.commit()
        return 'Usuário atualizado com sucesso!'
    
    @classmethod
    def delete(cls, id:int) -> Any:
        cls.session.query(Aluno).where(Aluno.id == id).one()
        cls.session.execute(delete(Aluno).where(Aluno.id == id))
        cls.session.commit()
        return 'Usuário deletado com sucesso!'
    
    @classmethod
    def soft_delete(cls, id: int) -> Any:
        cls.session.query(Aluno).where(Aluno.id == id).one()
        cls.session.execute(update(Aluno).where(Aluno.id == id).values(ativo = False))
        cls.session.commit()
        return 'Usuário deletado com sucesso!'
    
    @classmethod
    def find_all(cls) -> list:
        alunos = cls.session.query(Aluno).all()
        result = []
        
        for a in alunos:
            result.append(a._to_dict())

        return result
    
    @classmethod
    def find_by_id(cls, id: int) -> Aluno:
        result = cls.session.query(Aluno).where(Aluno.id == id).one()
        return result
    
    @classmethod
    def find_by_course(cls, curso: str) -> list:
        alunos = cls.session.query(Aluno).where(Aluno.curso == curso).all()

        result = []
        
        for a in alunos:
            result.append(a._to_dict())

        return result
    
    @classmethod
    def find_by_register(cls, matricula: str) -> Aluno:
        result = cls.session.query(Aluno).where(Aluno.matricula == matricula).one()
        return result._to_dict()
    