from models import *
from database import *
from datetime import date

session = SessionaLocal()

# ----- Inserirmos os alunos
aluno_1 = Aluno(nome="Jovana", matricula="2026001", curso="Engenharia")
aluno_2 = Aluno(nome="Jeremias", matricula="2026002", curso="Design")
aluno_3 = Aluno(nome="Everton", matricula="2026003", curso="Arquitetura")

# ----- Inserirmos os livros
livro_1 = Livro(titulo="Clean Code", autor="Robert C. Martin", 
                ano_publicacao=2008, isbn="123456789101")
livro_2 = Livro(titulo="O Senhor do Anéis", autor="J.R.R Tolkien", 
                ano_publicacao=1954, isbn="123456789102")
livro_3 = Livro(titulo="Python Fluente", autor="Luciano Ramalho", 
                ano_publicacao=2015, isbn="123456789103")

try:
    session.add_all([aluno_1, aluno_2, aluno_3, livro_1, livro_2, livro_3])
    session.commit()
except:
    print("Erro ao cadastrar os dados...!")

# ----- Inserirmos os empréstimos
emp1 = Emprestimo(aluno=aluno_1, 
                  livro=livro_1, 
                  data_retirada=date(2026, 3, 27))
emp2 = Emprestimo(aluno=aluno_2, 
                  livro=livro_2, 
                  data_retirada=date(2026, 3, 2),
                  data_devolucao=date(2026, 3, 10))
emp3 = Emprestimo(aluno=aluno_1, 
                  livro=livro_3, 
                  data_retirada=date(2026, 3, 5))

try:
    session.add_all([emp1, emp2, emp3])
    session.commit()
except Exception as e:
    print("Erro ao cadastrar os empréstimos...!\n", e)
                  