from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Clean Code", "autor": "Robert Martin", "ano": 2008, "disponivel": True, "categoria": "Arquitetura"},
    {"id": 2, "titulo": "Python Crash Course", "autor": "Eric Matthes", "ano": 2019, "disponivel": True, "categoria": "Python"}
]

# Endpoint GET - Listar Livros
@app.route("/livros")
def listar_livros():
    return jsonify({
        "message": "Livros carregados com sucesso!",
        "data": livros,
        "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
    }), 200

# Endpoint GET - Listar livros disponíveis
@app.route("/livros/disponiveis")
def listar_disponiveis():
    livros_disponivieis = []
    for livro in livros:
        if livro.get('disponivel') == True:
            livros_disponivieis.append(livro)
    

    if not len(livros_disponivieis) == 0:
        return jsonify({
                    "message": "Livros disponíveis no catálogo!",
                    "data": livros_disponivieis,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200

    return jsonify({
                    "message": "Nenhum livro disponível no catálogo!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }),

#Endpoint GET - Pesquisar livros por título
@app.route('/livros/busca')
def buscar_livros():
    busca = request.args.get('titulo')
    
    livros_corresp = []

    for livro in livros:
        if busca.capitalize() in livro.get('titulo') :
            livros_corresp.append(livro)
            
    
    if not len(livros_corresp) == 0:
        return jsonify({
                    "message": "Livros disponíveis no catálogo!",
                    "data": livros_corresp,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200

    return jsonify({
                    "message": "Nenhum livro disponível no catálogo!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200

# Endpoint POST - cadastrar livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    dados = request.json

    novo_livro = {
        "id": len(livros) + 1,
        "titulo": dados['titulo'],
        "autor": dados['autor'],
        "ano": dados['ano'],
        "disponivel": dados['disponivel'],
        "categoria": dados['categoria']
    }

    livros.append(novo_livro)

    return jsonify({
        "message": "Livro cadastrado com sucesso!",
        "data": novo_livro,
        "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
    }), 201

#Endpoint PUT - atualizar livro
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    dados = request.json #capturar o objeto json no body da requisição

    for livro in livros:
        if livro["id"] == id:
            livro.update(dados)

            return jsonify({
                    "message": "Livro atualizado com sucesso!",
                    "data": livro,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200
    
    return jsonify({
                    "message": "Livro não encontrado!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 404
    

# Endpoint DELETE - Deletar Livro
@app.route("/livros/<int:id>", methods=['DELETE'])
def deletar_livro(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return jsonify({
                    "message": "Livro excluído com sucesso!",
                    "data": livro,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 200

    return jsonify({
                    "message": "Livro não encontrado!",
                    "data": None,
                    "timestamp": datetime.today().strftime("%d-%m-%Y - %H:%M:%S")
                }), 404



    

if __name__ == '__main__':
    app.run(debug=True)