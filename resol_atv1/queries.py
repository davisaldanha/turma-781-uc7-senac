from models import *
from database import *
from datetime import date
from sqlalchemy import func

session = SessionaLocal()

# 1. Todos os livros emprestados por um aluno específico
print('----- 1 -----')
aluno = session.query(Aluno).filter_by(nome="Jeremias").first()

for e in aluno.emprestimos:
    print(e.livro.titulo)

# 2. Todos os alunos que pegaram um determinado livro
print('----- 2 -----')
livro = session.query(Livro).filter_by(titulo="O Senhor do Anéis").first()

for e in livro.emprestimos:
    print(e.aluno.nome)

# 3. Livros ainda não devolvidos
print('----- 3 -----')
emp_abertos = session.query(Emprestimo).filter(Emprestimo.data_devolucao == None).all()

for e in emp_abertos:
    print(e.livro.titulo, " -> emprestado para ", e.aluno.nome)

# 4. Quantos empréstimos cada aluno já realizou
result = session.query(Aluno.nome, func.count(Emprestimo.id)).join(Emprestimo).group_by(Aluno.nome).all()

for aluno, qtd in result:
    print(aluno, "realizou", qtd, "empréstimos!")