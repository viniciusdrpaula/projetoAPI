from flask import Blueprint, request, jsonify
from config import db
from alunos.alunos_model import Aluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    aluno = Aluno.query.get_or_404(id_aluno)
    return jsonify(aluno.to_dict())

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    novo_aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        turma_id=data['turma_id'],
        data_nascimento=data['data_nascimento'],
        nota_primeiro_semestre=data['nota_primeiro_semestre'],
        nota_segundo_semestre=data['nota_segundo_semestre'],
        media_final=data['media_final']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.to_dict()), 201

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['PUT'])
def update_aluno(id_aluno):
    data = request.json
    aluno = Aluno.query.get_or_404(id_aluno)
    aluno.nome = data['nome']
    aluno.idade = data['idade']
    aluno.turma_id = data['turma_id']
    aluno.data_nascimento = data['data_nascimento']
    aluno.nota_primeiro_semestre = data['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = data['nota_segundo_semestre']
    aluno.media_final = data['media_final']
    db.session.commit()
    return jsonify(aluno.to_dict())

@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    aluno = Aluno.query.get_or_404(id_aluno)
    db.session.delete(aluno)
    db.session.commit()
    return '', 204
