from flask import Blueprint, request, jsonify
from config import db
from professors.professors_model import Professor

professors_blueprint = Blueprint('professors', __name__)

@professors_blueprint.route('/professors', methods=['GET'])
def get_professores():
    professores = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professores])

@professors_blueprint.route('/professors/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    professor = Professor.query.get_or_404(id_professor)
    return jsonify(professor.to_dict())

@professors_blueprint.route('/professors', methods=['POST'])
def create_professor():
    data = request.json
    novo_professor = Professor(
        nome=data['nome'],
        idade=data['idade'],
        materia=data['materia'],
        observacoes=data.get('observacoes')
    )
    db.session.add(novo_professor)
    db.session.commit()
    return jsonify(novo_professor.to_dict()), 201

@professors_blueprint.route('/professors/<int:id_professor>', methods=['PUT'])
def update_professor(id_professor):
    data = request.json
    professor = Professor.query.get_or_404(id_professor)
    professor.nome = data['nome']
    professor.idade = data['idade']
    professor.materia = data['materia']
    professor.observacoes = data.get('observacoes')
    db.session.commit()
    return jsonify(professor.to_dict())

@professors_blueprint.route('/professors/<int:id_professor>', methods=['DELETE'])
def delete_professor(id_professor):
    professor = Professor.query.get_or_404(id_professor)
    db.session.delete(professor)
    db.session.commit()
    return '', 204
