# app.py
from flask import Flask, request, jsonify
import controller  # Importa o módulo com a lógica de controle

app = Flask(__name__)

@app.route("/")
def hello():
    return "API para gerenciamento de Alunos, Professores e Turmas"

# Rotas para Alunos
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return controller.listar_alunos()

@app.route("/alunos", methods=["POST"])
def criar_aluno():
    data = request.json
    return controller.criar_aluno(data)

@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    data = request.json
    return controller.atualizar_aluno(id, data)

@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    return controller.deletar_aluno(id)

# Rotas para Professores
@app.route("/professores", methods=["GET"])
def listar_professores():
    return controller.listar_professores()

@app.route("/professores", methods=["POST"])
def criar_professor():
    data = request.json
    return controller.criar_professor(data)

@app.route("/professores/<int:id>", methods=["PUT"])
def atualizar_professor(id):
    data = request.json
    return controller.atualizar_professor(id, data)

@app.route("/professores/<int:id>", methods=["DELETE"])
def deletar_professor(id):
    return controller.deletar_professor(id)

# Rotas para Turmas
@app.route("/turmas", methods=["GET"])
def listar_turmas():
    return controller.listar_turmas()

@app.route("/turmas", methods=["POST"])
def criar_turma():
    data = request.json
    return controller.criar_turma(data)

@app.route("/turmas/<int:id>", methods=["PUT"])
def atualizar_turma(id):
    data = request.json
    return controller.atualizar_turma(id, data)

@app.route("/turmas/<int:id>", methods=["DELETE"])
def deletar_turma(id):
    return controller.deletar_turma(id)

if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)
