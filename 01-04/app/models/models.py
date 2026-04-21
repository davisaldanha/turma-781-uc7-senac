from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Livro(Base):
    '''Classe representativa da entidade livros.'''
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    isbn = Column(String(13), unique=True)
    ativo = Column(Boolean, default=True)
    created_at = Column(Date, server_default=func.current_date())
    updated_at = Column(Date, 
                        server_default=func.current_date(),
                        onupdate=func.current_date())
    emprestimos = relationship("Emprestimo", back_populates="livro")
    
    
    def __repr__(self):
        return f'Título: {self.titulo} - Autor: {self.autor} - Ano Publicação: {self.ano_publicacao}'
    
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "ano_publicacao": self.ano_publicacao,
            "isbn": self.isbn,
            'ativo': self.ativo
        }

class Aluno(Base):
    '''Classe representativa da entidade alunos.'''
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    matricula = Column(String, nullable=False, unique=True)
    curso = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
    created_at = Column(Date, server_default=func.current_date())
    updated_at = Column(Date, 
                        server_default=func.current_date(),
                        onupdate=func.current_date())
    emprestimos = relationship("Emprestimo", back_populates="aluno")
    

    def _to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'matricula': self.matricula,
            'curso': self.curso,
            'ativo': self.ativo,
            'created_at': datetime.strftime(self.created_at, '%d-%m-%Y')
        }

class Emprestimo(Base):
    '''Classe representativa da entidade emprestimos.'''
    __tablename__ = "emprestimos"
    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    livros_id = Column(Integer, ForeignKey("livros.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    data_retirada = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=True)
    created_at = Column(Date, server_default=func.current_date())
    updated_at = Column(Date, 
                        server_default=func.current_date(),
                        onupdate=func.current_date())
    
    aluno = relationship("Aluno", back_populates="emprestimos")
    livro = relationship("Livro", back_populates="emprestimos")
    usuario = relationship("Usuario", back_populates="emprestimos")

    def to_dict(self):
        return {
            'id': self.id,
            'aluno_id': self.aluno_id,
            'livro_id': self.livros_id,
            'usuario_id': self.usuario_id,
            'data_retirada': f'{datetime.strftime(self.data_retirada, "%Y-%m-%d")}',
            'data_devolucao': f'{datetime.strftime(self.data_devolucao, "%Y-%m-%d")}'
            if self.data_devolucao else None
        }
    
class Usuario(Base):
    '''Classe representativa da entidade usuarios.'''
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(Date, server_default=func.current_date())
    updated_at = Column(Date, 
                        server_default=func.current_date(),
                        onupdate=func.current_date())
    
    emprestimos = relationship("Emprestimo", back_populates="usuario")

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'username': self.username
        }