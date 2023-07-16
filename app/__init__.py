from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate




app = Flask(__name__)
app.config.from_object('config')



db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)


from app.controllers import default
from app.models import tables



