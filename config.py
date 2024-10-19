import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['HOST'] = '127.0.0.1'
app.config['PORT'] = 5000
app.config['DEBUG'] = True

db = SQLAlchemy(app)