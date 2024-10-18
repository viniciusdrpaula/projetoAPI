from config import app, db
from alunos.alunos_routes import alunos_blueprint
from professors.professors_routes import professors_blueprint
from turmas.turmas_routes import turmas_blueprint

# Registrando os blueprints
app.register_blueprint(alunos_blueprint)
app.register_blueprint(professors_blueprint)
app.register_blueprint(turmas_blueprint)

# Criando as tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
