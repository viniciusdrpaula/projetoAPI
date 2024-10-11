# models.py
class Professor:
    def __init__(self, id, nome, idade, materia, observacoes=""):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "materia": self.materia,
            "observacoes": self.observacoes
        }

class Turma:
    def __init__(self, id, descricao, professor_id, ativo=True):
        self.id = id
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "professor_id": self.professor_id,
            "ativo": self.ativo
        }

class Aluno:
    def __init__(self, id, nome, idade, turma_id, data_nascimento, nota1, nota2):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento
        self.nota1 = nota1
        self.nota2 = nota2
        self.media_final = self.calcula_media()

    def calcula_media(self):
        return (self.nota1 + self.nota2) / 2

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "turma_id": self.turma_id,
            "data_nascimento": self.data_nascimento,
            "nota1": self.nota1,
            "nota2": self.nota2,
            "media_final": self.media_final
        }

# Listas para armazenar dados em memória
professores = []
turmas = []
alunos = []

# Funções CRUD para Alunos
def lista_alunos():
    return [aluno.to_dict() for aluno in alunos]

def adiciona_aluno(data):
    novo_aluno = Aluno(**data)
    alunos.append(novo_aluno)

def atualiza_aluno(id, data):
    for aluno in alunos:
        if aluno.id == id:
            aluno.nome = data.get('nome', aluno.nome)
            aluno.idade = data.get('idade', aluno.idade)
            aluno.turma_id = data.get('turma_id', aluno.turma_id)
            aluno.data_nascimento = data.get('data_nascimento', aluno.data_nascimento)
            aluno.nota1 = data.get('nota1', aluno.nota1)
            aluno.nota2 = data.get('nota2', aluno.nota2)
            aluno.media_final = aluno.calcula_media()
            return aluno.to_dict()
    raise ValueError("Aluno não encontrado")

def deleta_aluno(id):
    for aluno in alunos:
        if aluno.id == id:
            alunos.remove(aluno)
            return
    raise ValueError("Aluno não encontrado")

# Funções CRUD para Professores
def lista_professores():
    return [professor.to_dict() for professor in professores]

def adiciona_professor(data):
    novo_professor = Professor(**data)
    professores.append(novo_professor)

def atualiza_professor(id, data):
    for professor in professores:
        if professor.id == id:
            professor.nome = data.get('nome', professor.nome)
            professor.idade = data.get('idade', professor.idade)
            professor.materia = data.get('materia', professor.materia)
            professor.observacoes = data.get('observacoes', professor.observacoes)
            return professor.to_dict()
    raise ValueError("Professor não encontrado")

def deleta_professor(id):
    for professor in professores:
        if professor.id == id:
            professores.remove(professor)
            return
    raise ValueError("Professor não encontrado")

# Funções CRUD para Turmas
def lista_turmas():
    return [turma.to_dict() for turma in turmas]

def adiciona_turma(data):
    nova_turma = Turma(**data)
    turmas.append(nova_turma)

def atualiza_turma(id, data):
    for turma in turmas:
        if turma.id == id:
            turma.descricao = data.get('descricao', turma.descricao)
            turma.professor_id = data.get('professor_id', turma.professor_id)
            turma.ativo = data.get('ativo', turma.ativo)
            return turma.to_dict()
    raise ValueError("Turma não encontrada")

def deleta_turma(id):
    for turma in turmas:
        if turma.id == id:
            turmas.remove(turma)
            return
    raise ValueError("Turma não encontrada")
