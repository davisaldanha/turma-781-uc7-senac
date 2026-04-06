from sqlalchemy import *
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# ----- One-to-One -----
class CartaoBiblioteca(Base):
    __tablename__ = "cartoes"
    id = Column(Integer, primary_key=True)
    numero = Column(String, unique=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))

    aluno = relationship("Aluno", back_populates="cartao", uselist=False)

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cartao = relationship("CartaoBiblioteca", back_populates="aluno", uselist=False)


