from flask import render_template
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

@app.route("/register", methods = ['GET', 'POST'])
def register():
    return render_template("register.jinja2")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    return render_template("login.jinja2")

@app.route("/create_exam", methods = ['GET', 'POST'])
def create_exam():
    return render_template("create_exam.jinja2")

@app.route("/create_question", methods = ['GET', 'POST'])
def create_question():
    return render_template("create_question.jinja2")


@app.route("/pag_aluno", methods = ['GET', 'POST'])
def pag_aluno():
    return render_template("pag_aluno.jinja2")

@app.route("/pag_professor", methods = ['GET', 'POST'])
def pag_professor():
    return render_template("pag_aluno.jinja2")
