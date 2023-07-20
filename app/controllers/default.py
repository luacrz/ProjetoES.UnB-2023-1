from flask import render_template, redirect, url_for, request
from app import app, db
from app.models.tables import User
from app.models import tables
from flask_login import login_user, logout_user, current_user
from datetime import datetime




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
        if role_value == "True": role = 1
        else : role = 0
        user = User(username, email, pwd, name, role)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for(('login')))
    return render_template("register.jinja2")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        pwd = request.form['password']
        user = User.query.filter_by(username = username).first()
        if not user or not user.verify_password(pwd):
            return redirect(url_for(('home')))
        login_user(user)
        if current_user.role == 1: return redirect(url_for(('pag_professor')))
        else : return redirect(url_for(('pag_aluno')))
    return render_template("login.jinja2")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/create_exam", methods=['GET', 'POST']) #Página de Criar Exames
def create_exam():
    if request.method == 'POST':
        start_time_str = request.form['start_time']
        end_time_str = request.form['end_time']
        comment = request.form['comment']
        start_time = datetime.fromisoformat(start_time_str)
        end_time = datetime.fromisoformat(end_time_str)
        exam = tables.Exam(start_time=start_time, end_time=end_time, user_id=current_user.id, comment=comment)
        db.session.add(exam)
        db.session.commit()
        return redirect(url_for('pag_professor'))
    
    return render_template("create_exam.html")


@app.route("/create_question", methods=['GET', 'POST']) #Página de Criar Questões
def create_question():
    if request.method == 'POST':
        statement = request.form['statement']
        tipo = request.form['tipo']
        
        if tipo == "VF":
            answer_value = request.form.get('vf-resposta')
            tipo = 1
            if answer_value == "True": answer = 1
            else : answer = 0
        elif tipo == "ABC":
            answer_value = request.form.get('abc-resposta')
            tipo = 2
        elif tipo == "NUM":
            answer_value = request.form.get('num-resposta')
            tipo = 3
        else:
            answer_value = None
            tipo = 0
        
        
        question = tables.Question(statement, tipo, user_id=current_user.id)
        if tipo == 1:
            question.answer_VouF = answer
        elif tipo == 2:
            question.answer_Mult = answer_value
        elif tipo == 3:
            question.answer_ValNum = answer_value

        db.session.add(question)
        db.session.commit()
        
        return redirect(url_for('pag_professor'))
    
    return render_template("create_question.html")



@app.route("/pag_aluno", methods = ['GET', 'POST']) #Página que contém links que redirecionam para as funções do Aluno NÃO IMPLEMENTADO
def pag_aluno():
    return render_template("pag_aluno.html")

@app.route("/pag_professor", methods = ['GET', 'POST']) #Página que contém links que redirecionam para as funções do professor
def pag_professor():
    return render_template("pag_professor.html")

@app.route("/visualizar_notas")
def visualizar_notas():
    return render_template("visualizar_notas.html")

@app.route("/listar_questoes") #Lista todas as questões do Usuário atual
def listar_questoes():
    questoes = tables.Question.query.filter_by(user_id =current_user.id)
    return render_template("listar_questoes.html", questoes=questoes)

@app.route("/listar_exames") #Lista todos os exames do Usuário atual
def listar_exames():
    exames = tables.Exam.query.filter_by(user_id =current_user.id)
    return render_template("listar_exames.html", exames=exames)

@app.route("/selecionar_questoes", methods=["GET", "POST"])
def selecionar_questoes():
    if request.method == "POST":
        questao_ids = request.form.getlist("questao_ids")
        
        return "Relação entre exame e questões criada com sucesso!" 
        
    else:
        questoes = tables.Question.query.filter_by(user_id =current_user.id)
        return render_template("selecionar_questoes.html", questoes=questoes)

@app.route("/add_quest_exam", methods=["GET", "POST"])
def add_quest_exam():
    if request.method == "POST":
        exame_id = request.form.get("exame_id")
        questao_ids = [key.split('_')[2] for key in request.form if key.startswith('questao_ids_')]
        print(questao_ids)
        
        exame = tables.Exam.query.get(exame_id)
        if exame is None:
            return "Exame não encontrado!"
        
        for questao_id in questao_ids:
            questao = tables.Question.query.get(questao_id)
            if questao is not None:
                exame.exam_question.append(questao)

        db.session.commit()
        return redirect(url_for('pag_professor'))

    exames = tables.Exam.query.filter_by(user_id=current_user.id).all()
    questoes = tables.Question.query.filter_by(user_id=current_user.id).all()
    return render_template("add_quest_exam.html", exames=exames, questoes=questoes)

@app.route("/exam/<exame_id>")
def list_exam_questions(exame_id):
    exame = tables.Exam.query.get(exame_id)
    if exame is None:
        return "Exame não encontrado!"

    questoes = exame.exam_question

    return render_template("list_exam_questions.html", questoes=questoes)

@app.route("/submit_answers/<exame_id>", methods=["GET", "POST"])
def submit_answers(exame_id):
    if request.method == "POST":
        respostas = {}
        for key, value in request.form.items():
            if key.startswith('respostas['):
                questao_id = key.split('[')[1].split(']')[0]
                respostas[questao_id] = value

        Respostas_formatadas = ", ".join(f"{questao_id}_{resposta}" for questao_id, resposta in respostas.items())
        print(Respostas_formatadas)
        Exame_finalizado = tables.FinalizedExam(current_user.id, exame_id, Respostas_formatadas)
        db.session.add(Exame_finalizado)
        db.session.commit()
        return redirect(url_for('pag_aluno'))


    exame = tables.Exam.query.get(exame_id)
    questoes = exame.exam_question
    return render_template("responder_prova.html", questoes=questoes, exame_id=exame_id)

@app.route("/procurar_exames") #Lista todos os exames do Usuário atual
def procurar_exames():
    exames = tables.Exam.query.all()
    return render_template("procurar_exames.html", exames=exames)

@app.route("/exames_feitos", methods=["GET"])
def exames_feitos():
    finalized_exams = tables.FinalizedExam.query.all()
    return render_template("exames_feitos.html", finalized_exams=finalized_exams)
