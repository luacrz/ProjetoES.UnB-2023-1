from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate




app = Flask(__name__)
app.config.from_object('config')



db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)

from app.models.tables import teste
from app.controllers import default
from app.models import tables





# Chamando a função para criar o objeto dentro do contexto da aplicação


def create_user():
    with app.app_context():
        Rafaela = tables.User('rafaella', 'rafael@kska', '123a', 'Rafaela', 0)
        db.session.add(Rafaela)
        db.session.commit()

#usuário: “pedro”, email: “pedro@unb.br”, senha: “asdfg”, perfil: professor
#usuário: “ester”, email: “ester@unb.br” senha: “asdfg”, perfil: estudante
#create_user()  
#user = db.session.execute(db.select(tables.User).filter_by(id=1)).scalar_one()
#db.session.delete(user)
#db.session.commit() 