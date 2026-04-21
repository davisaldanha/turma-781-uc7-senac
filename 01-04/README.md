# Sistema de Gerenciamento de Biblioteca

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-lightgrey.svg)](https://flask.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.48-red.svg)](https://www.sqlalchemy.org/)
[![JWT](https://img.shields.io/badge/JWT-Extended-green.svg)](https://flask-jwt-extended.readthedocs.io/)

Uma API REST robusta para gerenciar um sistema de biblioteca, construída com Flask e SQLAlchemy. Este projeto demonstra habilidades de desenvolvimento full-stack incluindo autenticação, modelagem de banco de dados e design de API RESTful.

## 📋 Descrição

Esta aplicação fornece uma solução completa de backend para gerenciamento de biblioteca, permitindo aos usuários gerenciar livros, alunos, empréstimos e contas de usuário. Conta com autenticação baseada em JWT, operações CRUD abrangentes e validação de dados usando Pydantic.

## ✨ Funcionalidades

- **Autenticação de Usuário**: Login seguro com tokens JWT
- **Gerenciamento de Livros**: Adicionar, atualizar, excluir e pesquisar livros
- **Gerenciamento de Alunos**: Gerenciar registros de alunos
- **Gerenciamento de Empréstimos**: Rastrear empréstimos e devoluções de livros
- **API RESTful**: Endpoints bem estruturados seguindo princípios REST
- **Validação de Dados**: Validação de entrada usando Pydantic
- **Integração com Banco de Dados**: ORM SQLAlchemy com gerenciamento de relacionamentos

## 🛠️ Pilha de Tecnologias

- **Backend**: Flask 3.1.3
- **Banco de Dados**: SQLAlchemy 2.0.48 (com suporte a SQLite/PostgreSQL)
- **Autenticação**: Flask-JWT-Extended 4.7.1
- **Validação**: Pydantic 2.13.1
- **Ambiente**: Python 3.8+

## 🚀 Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seuusuario/sistema-gerenciamento-biblioteca.git
   cd sistema-gerenciamento-biblioteca
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` no diretório raiz:
   ```
   SECRET_KEY=sua_chave_secreta_aqui
   ```

5. **Execute a aplicação**:
   ```bash
   python run.py
   ```

A API estará disponível em `http://localhost:5000`.

## 📖 Uso

### Autenticação
Primeiro, obtenha um token JWT fazendo login:
```bash
POST /api/auth/login
Content-Type: application/json

{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Use o token nas solicitações subsequentes:
```
Authorization: Bearer <seu_token_jwt>
```

### Endpoints da API

#### Livros
- `GET /api/livros` - Listar todos os livros
- `POST /api/livros` - Criar um novo livro
- `GET /api/livros/{id}` - Obter detalhes do livro
- `PUT /api/livros/{id}` - Atualizar livro
- `DELETE /api/livros/{id}` - Excluir livro

#### Alunos
- `GET /api/alunos` - Listar todos os alunos
- `POST /api/alunos` - Criar um novo aluno
- `GET /api/alunos/{id}` - Obter detalhes do aluno
- `PUT /api/alunos/{id}` - Atualizar aluno
- `DELETE /api/alunos/{id}` - Excluir aluno

#### Empréstimos
- `GET /api/emprestimos` - Listar todos os empréstimos
- `POST /api/emprestimos` - Criar um novo empréstimo
- `GET /api/emprestimos/{id}` - Obter detalhes do empréstimo
- `PUT /api/emprestimos/{id}` - Atualizar empréstimo (devolver livro)

#### Usuários
- `POST /api/usuarios` - Registrar um novo usuário
- `GET /api/usuarios/{id}` - Obter detalhes do usuário

## 📁 Estrutura do Projeto

```
sistema-gerenciamento-biblioteca/
├── app/
│   ├── __init__.py              # Fábrica da aplicação Flask
│   ├── controllers/             # Manipuladores de rotas
│   │   ├── aluno_controller.py
│   │   ├── emprestimo_controller.py
│   │   ├── livro_controller.py
│   │   └── usuario_controller.py
│   ├── database/
│   │   └── database.py          # Conexão com banco de dados
│   ├── exceptions/
│   │   └── exceptions.py        # Exceções personalizadas
│   ├── models/
│   │   └── models.py            # Modelos SQLAlchemy
│   ├── services/                # Lógica de negócio
│   │   ├── aluno_service.py
│   │   ├── emprestimo_service.py
│   │   ├── livro_service.py
│   │   └── usuario_service.py
│   └── validations/
│       └── validations.py       # Validação de dados
├── config.py                    # Configurações
├── requirements.txt             # Dependências Python
├── run.py                       # Ponto de entrada da aplicação
└── README.md                    # Documentação do projeto
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**Seu Nome**  
- GitHub: [@seuusuario](https://github.com/seuusuario)
- LinkedIn: [Seu LinkedIn](https://linkedin.com/in/seuperfil)

---

*Este projeto foi desenvolvido como parte do curso Técnico em Desenvolvimento no SENAC.*