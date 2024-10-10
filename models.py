class Professor:
    def __init__(self, id, nome, idade, materia, observacoes):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

class Turma:
    def __init__(self, id, descricao, professor_id, ativo):
        self.id = id
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

class Aluno:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota1, nota2):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota1 = nota1
        self.nota2 = nota2
        self.media_final = (nota1 + nota2) / 2
