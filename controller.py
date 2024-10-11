# controllers.py
from models import Aluno, Professor

dados = {"alunos": [], "professores": []}

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    lista_alunos = dados['alunos']
    for dicionario in lista_alunos:
        if dicionario['id'] == id_aluno:
            return dicionario
    raise AlunoNaoEncontrado

def aluno_existe(id_aluno):
    try:
        aluno_por_id(id_aluno)
        return True
    except AlunoNaoEncontrado:
        return False

def adiciona_aluno(dict_aluno):
    aluno = Aluno(
        id=dict_aluno['id'],
        nome=dict_aluno['nome'],
        idade=dict_aluno['idade'],
        turma_id=dict_aluno['turma_id'],
        data_nascimento=dict_aluno['data_nascimento'],
        nota1=dict_aluno['nota1'],
        nota2=dict_aluno['nota2']
    )
    dados['alunos'].append(vars(aluno))

def lista_alunos():
    return dados["alunos"]

def apaga_tudo():
    dados['alunos'] = []
