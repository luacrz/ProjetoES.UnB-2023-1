from app import app, db
from app.models.tables import User



@app.route("/")
def index():
    return "ok!"

@app.route("/test", defaults={'name': None})
@app.route("/test/<name>")
def teste(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá, usuário!"
    