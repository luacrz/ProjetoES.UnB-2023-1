from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.models.tables import teste
from app.controllers import default
from app.models import tables




# Chamando a função para criar o objeto dentro do contexto da aplicação


def create_user():
    with app.app_context():
        Rafaela = tables.User('rafaella', 'rafael@kska', '123a', 'Rafaela', 0)
        db.session.add(Rafaela)
        db.session.commit()

# create_user()   