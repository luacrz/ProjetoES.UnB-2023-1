from flask import render_template, redirect, url_for, request
from app import app, db
from app.models.tables import User
from flask_login import login_user, logout_user




@app.route("/")
def index():
    return render_template("inicial.jinja2")

@app.route('/home', methods = ['GET']) 
def home():
    return render_template('home.html')



@app.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['senha']
        name = request.form['name']
        role_value = request.form['role']
        role = bool(role_value)
        user = User(username, email, pwd, name, role)
        db.session.add(user)
        db.session.commit()
    return render_template("register.jinja2")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        user = User.query.filter_by(username = username).first()
        if not user or not user.verify_password(pwd):
            return redirect(url_for(('home')))
        print("entrouu")
        login_user(user)
        return redirect(url_for(('home')))
    return render_template("login.jinja2")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

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

