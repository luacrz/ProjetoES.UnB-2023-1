from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models.tables import User, Exam # Importe a classe Exam
from app.models import tables
from flask_login import login_user, logout_user, current_user
from datetime import datetime


def calcular_nota_exame(exam_id, user_id):
    finalized_exam = tables.FinalizedExam.query.filter_by(user_id=user_id, exam_id=exam_id).first()

    if finalized_exam is None:
        return 0.0

    answers_replied = finalized_exam.answers_replied.split(", ")
    nota_total = 0.0

    for resposta in answers_replied:
        questao_id, resposta_aluno = resposta.split('_')
        questao = tables.Question.query.get(questao_id)
        if questao is not None:
            if questao.question_type == 1:
                resposta_correta = "V" if questao.answer_VouF else "F"
                if resposta_aluno == resposta_correta:
                    nota_total += questao.exam_questions.filter_by(Exam_id=exam_id).first().nota
            elif questao.question_type == 2:
                resposta_correta = questao.answer_Mult
                if resposta_aluno == resposta_correta:
                    nota_total += questao.exam_questions.filter_by(Exam_id=exam_id).first().nota
            elif questao.question_type == 3:
                resposta_correta = str(questao.answer_ValNum)
                if resposta_aluno == resposta_correta:
                    nota_total += questao.exam_questions.filter_by(Exam_id=exam_id).first().nota

    return nota_total

def calcular_nota_maxima_exame(exam_id):
    exam_questions = tables.ExamQuestion.query.filter_by(Exam_id=exam_id).all()

    nota_maxima = 0.0

    for exam_question in exam_questions:
        nota_maxima += exam_question.nota

    return nota_maxima
    




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
            flash("Credenciais inválidas")
            return redirect(url_for(('login')))
        login_user(user)
        if current_user.role == 1: return redirect(url_for(('pag_professor')))
        else : return redirect(url_for(('pag_aluno')))
    return render_template("login.jinja2")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/create_exam", methods=['GET', 'POST'])
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

        return redirect(url_for('add_quest_exam', exam_id=exam.id))
    
    return render_template("create_exam.html")


@app.route("/create_question", methods=['GET', 'POST'])
def create_question():
    tipo = None
    if request.method == 'POST':
        statement = request.form['statement']
        tipo = request.form['tipo']
        if tipo == 'ABC' and not request.form.get('abc-resposta'):
            return render_template("create_question.html", tipo=tipo, error="Campo de resposta A/B/C/D é obrigatório para Múltipla Escolha.")
        if tipo == "VF":
            answer_value = request.form.get('vf-resposta')
            tipo = 1
            if answer_value == "True":
                answer = 1
            else:
                answer = 0
        elif tipo == "ABC":
            answer_value = request.form.get('abc-resposta')
            tipo = 2
            resposta_A = request.form.get('resposta-A')
            resposta_B = request.form.get('resposta-B')
            resposta_C = request.form.get('resposta-C')
            resposta_D = request.form.get('resposta-D')
        elif tipo == "NUM":
            answer_value = request.form.get('num-resposta')
            if answer_value == "":
                answer_value = None
            else:
                answer_value = float(answer_value)  # Convertendo para float
            tipo = 3
        else:
            answer_value = None
            tipo = 0

        question = tables.Question(statement, tipo, user_id=current_user.id)
        if tipo == 1:
            question.answer_VouF = answer
        elif tipo == 2:
            question.answer_Mult = answer_value
            question.answer_Mult_A = resposta_A
            question.answer_Mult_B = resposta_B
            question.answer_Mult_C = resposta_C
            question.answer_Mult_D = resposta_D
        elif tipo == 3:
            question.answer_ValNum = answer_value

        db.session.add(question)
        db.session.commit()

        return redirect(url_for('pag_professor'))

    return render_template("create_question.html", tipo=tipo)






@app.route("/pag_aluno", methods = ['GET', 'POST']) #Página que contém links que redirecionam para as funções do Aluno NÃO IMPLEMENTADO
def pag_aluno():
    return render_template("pag_aluno.html")

@app.route("/pag_professor", methods = ['GET', 'POST']) #Página que contém links que redirecionam para as funções do professor
def pag_professor():
    return render_template("pag_professor.html")

@app.route("/visualizar_notas")
def visualizar_notas():
    return render_template("visualizar_notas.html")

@app.route("/listar_questoes") # Lista todas as questões do Usuário atual
def listar_questoes():
    questoes = tables.Question.query.filter_by(user_id=current_user.id)
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


@app.route("/add_quest_exam/<int:exam_id>", methods=["GET", "POST"])
def add_quest_exam(exam_id):
    if request.method == "POST":
        questao_ids = [key.split('_')[2] for key in request.form if key.startswith('questao_ids_')]

        exame = tables.Exam.query.get(exam_id)
        if exame is None:
            return "Exame não encontrado!"

        for questao_id in questao_ids:
            questao = tables.Question.query.get(questao_id)
            if questao is not None:
                nota = request.form.get('nota_' + str(questao_id))
                if nota:
                    nota = float(nota)
                else:
                    nota = 2

                exame_question = tables.ExamQuestion(Exam_id=exame.id, Question_id=questao.id, nota=nota)
                exame.exam_questions.append(exame_question)

        db.session.commit()
        return redirect(url_for('pag_professor'))

    questoes = tables.Question.query.filter_by(user_id=current_user.id).all()
    return render_template("add_quest_exam.html", exam_id=exam_id, questoes=questoes)






@app.route("/exam/<int:exam_id>")
def list_exam_questions(exam_id):
    exam = tables.Exam.query.get(exam_id)
    if exam is None:
        return "Exame não encontrado!"

    exam_questions = tables.ExamQuestion.query.filter_by(Exam_id=exam_id).all()

    # Criar uma lista para armazenar as questões relacionadas ao exame
    questoes = []
    
    for exam_question in exam_questions:
        # Obter a questão associada ao ExamQuestion
        questao = tables.Question.query.get(exam_question.Question_id)
        
        # Adicionar a questão à lista de questões
        if questao is not None:
            questoes.append(questao)

    return render_template("list_exam_questions.html", exam=exam, questoes=questoes)




@app.route("/submit_answers/<int:exame_id>", methods=["GET", "POST"])
def submit_answers(exame_id):
    exame = tables.Exam.query.get(exame_id)

    if exame is None:
        flash("Exame não encontrado", "error")
        return redirect(url_for('procurar_exames'))

    user_id = current_user.id
    exam_realizado = tables.FinalizedExam.query.filter_by(user_id=user_id, exam_id=exame.id).first()
    if exam_realizado is not None:
        flash(f"Você já realizou o exame {exame_id} anteriormente", "error")
        return redirect(url_for('procurar_exames'))

    if request.method == "POST":
        respostas = {}
        for key, value in request.form.items():
            if key.startswith('respostas['):
                questao_id = key.split('[')[1].split(']')[0]
                respostas[questao_id] = value

        Respostas_formatadas = ", ".join(f"{questao_id}_{resposta}" for questao_id, resposta in respostas.items())
        Exame_finalizado = tables.FinalizedExam(user_id, exame_id, Respostas_formatadas)
        db.session.add(Exame_finalizado)
        db.session.commit()

        flash(f"Exame enviado", "error")
        return redirect(url_for('procurar_exames'))


    current_time = datetime.now()
    if current_time > exame.end_time:
        flash(f"O exame {exame_id} já expirou", "error")
        return redirect(url_for('procurar_exames'))

    if current_time < exame.start_time:
        flash(f"O exame {exame_id} ainda não abriu", "error")
        return redirect(url_for('procurar_exames'))

    questoes = db.session.query(tables.Question, tables.ExamQuestion.nota).filter(
        tables.ExamQuestion.Exam_id == exame.id,
        tables.ExamQuestion.Question_id == tables.Question.id
    ).all()

    return render_template("responder_prova.html", questoes=questoes, exame=exame)

    exame = tables.Exam.query.get(exame_id)

    if exame is None:
        flash("Exame não encontrado", "error")
        return redirect(url_for('procurar_exames'))

    user_id = current_user.id
    exam_realizado = tables.FinalizedExam.query.filter_by(user_id=user_id, exam_id=exame.id).first()
    if exam_realizado is not None:
        flash(f"Você já realizou o exame {exame_id} anteriormente", "error")
        return redirect(url_for('procurar_exames'))

    current_time = datetime.now()
    # if current_time > exame.end_time:
    #     flash(f"O exame {exame_id} já expirou", "error")
    #     return redirect(url_for('procurar_exames'))

    if current_time < exame.start_time:
        flash(f"O exame {exame_id} ainda não abriu", "error")
        return redirect(url_for('procurar_exames'))

    if request.method == "POST":
        respostas = {}
        for key, value in request.form.items():
            if key.startswith('respostas['):
                questao_id = key.split('[')[1].split(']')[0]
                respostas[questao_id] = value

        Respostas_formatadas = ", ".join(f"{questao_id}_{resposta}" for questao_id, resposta in respostas.items())
        Exame_finalizado = tables.FinalizedExam(user_id, exame_id, Respostas_formatadas)
        db.session.add(Exame_finalizado)
        db.session.commit()

        return redirect(url_for('pag_aluno'))

    questoes = db.session.query(tables.Question, tables.ExamQuestion.nota).filter(
        tables.ExamQuestion.Exam_id == exame.id,
        tables.ExamQuestion.Question_id == tables.Question.id
    ).all()

    return render_template("responder_prova.html", questoes=questoes, exame=exame)


@app.route("/procurar_exames")  # Lista todos os exames do Usuário atual
def procurar_exames():
    current_time = datetime.now()
    exames_feitos = tables.FinalizedExam.query.filter_by(user_id=current_user.id).all()
    exames_feitos_ids = [exame.exam_id for exame in exames_feitos]
    exames = tables.Exam.query.all()

    
    exames_info = []
    for exame in exames:
        status = ""
        if exame.id in exames_feitos_ids:
            status = "Exame Feito"
        elif exame.start_time > current_time:
            status = "Exame ainda não abriu"
        elif exame.end_time < current_time:
            status = "Exame expirou"

        exames_info.append({
            "id": exame.id,
            "start_time": exame.start_time,
            "end_time": exame.end_time,
            "comment": exame.comment,
            "status": status
        })

    return render_template("procurar_exames.html", exames_info=exames_info)

@app.route("/exames_feitos", methods=["GET"])
def exames_feitos():
    finalized_exams = tables.FinalizedExam.query.all()

    for exame_feito in finalized_exams:
        user_id = exame_feito.user_id
        exam_id = exame_feito.exam_id
        exame_feito.exam = tables.Exam.query.get(exam_id)
        exame_feito.nota_total = calcular_nota_exame(exam_id, user_id)

    return render_template("exames_feitos.html", finalized_exams=finalized_exams)





@app.route("/view_finalized_exam/<int:exam_id>/<int:user_id>")
def view_finalized_exam(exam_id, user_id):
    exam = tables.Exam.query.get(exam_id)
    user = tables.User.query.get(user_id)

    if exam is None or user is None:
        flash("Exame ou usuário não encontrado", "error")
        return redirect(url_for('procurar_exames'))

    nota_maxima = calcular_nota_maxima_exame(exam_id)
    finalized_exam = tables.FinalizedExam.query.filter_by(user_id=user_id, exam_id=exam_id).first()
    if finalized_exam is None:
        flash(f"O usuário {user.username} não finalizou o exame {exam_id}", "error")
        return redirect(url_for('procurar_exames'))

    # Consulta todas as questões do exame
    exam_questions = tables.ExamQuestion.query.filter_by(Exam_id=exam_id).all()

    # Criar um dicionário para mapear o ID da questão para a resposta do aluno
    answers_by_question_id = {int(answer.split('_')[0]): answer.split('_')[1] for answer in finalized_exam.answers_replied.split(", ")}

    questoes_com_resposta = []
    nota_total = 0.0

    for exam_question in exam_questions:
        questao = exam_question.question
        questao_id = questao.id
        resposta_aluno = answers_by_question_id.get(questao_id, None)  # Obtém a resposta do aluno para essa questão (se existir)

        nota = exam_question.nota
        resposta_correta = ""
        status_resposta = ""
        soma_nota = 0.0

        if questao.question_type == 1:
            resposta_correta = "Verdadeiro" if questao.answer_VouF else "Falso"
            resposta_aluno_bool = True if resposta_aluno == "V" else False
            if resposta_aluno_bool == questao.answer_VouF:
                status_resposta = "correta"
                soma_nota = nota
            else:
                status_resposta = "incorreta"
                soma_nota = 0.0

        elif questao.question_type == 2:
            resposta_correta = questao.answer_Mult
            if resposta_aluno == questao.answer_Mult:
                status_resposta = "correta"
                soma_nota = nota
            else:
                status_resposta = "incorreta"
                soma_nota = 0.0

        elif questao.question_type == 3:
            resposta_correta = str(questao.answer_ValNum)
            if resposta_aluno == resposta_correta:
                status_resposta = "correta"
                soma_nota = nota
            else:
                status_resposta = "incorreta"
                soma_nota = 0.0

        questoes_com_resposta.append((questao, nota, resposta_aluno, resposta_correta, status_resposta))
        nota_total += soma_nota

    return render_template("view_finalized_exam.html", exam=exam, user=user, questoes=questoes_com_resposta, nota_total=nota_total, nota_maxima=nota_maxima)




@app.route("/view_finalized_exam/<int:exam_id>")
def view_finalized_exams(exam_id):
    exam = tables.Exam.query.get(exam_id)

    if exam is None:
        flash("Exame não encontrado", "error")
        return redirect(url_for('procurar_exames'))

    finalized_exams = tables.FinalizedExam.query.filter_by(exam_id=exam_id).all()
    users_info = []

    for finalized_exam in finalized_exams:
        user_id = finalized_exam.user_id
        user = tables.User.query.get(user_id)
        nota_total =  calcular_nota_exame(exam_id, user_id)

        users_info.append((user_id, user.name, nota_total))
    nota_maxima= calcular_nota_maxima_exame(exam_id)

    return render_template("users_that_finalized_exams.html", exam=exam, nota_maxima = nota_maxima, users_info=users_info)

def concluir_exame(exame_id, questoes, user_id):
    # Formate as respostas em um dicionário, incluindo as questões não respondidas.
    respostas = {}
    for questao, _ in questoes:
        questao_id = str(questao.id)
        resposta = request.form.get(f"respostas[{questao_id}]")
        respostas[questao_id] = resposta if resposta else "Não Respondida"

    # Converta as respostas em uma string para armazenar no banco de dados.
    Respostas_formatadas = ", ".join(f"{questao_id}_{resposta}" for questao_id, resposta in respostas.items())

    # Crie um novo registro na tabela FinalizedExam para armazenar as respostas do aluno.
    Exame_finalizado = tables.FinalizedExam(user_id, exame_id, Respostas_formatadas)
    db.session.add(Exame_finalizado)
    db.session.commit()

    flash("Exame concluído automaticamente.", "info")
    return redirect(url_for('pag_aluno'))


@app.route('/delete_exam/<int:exam_id>', methods=['GET', 'POST'])
def delete_exam(exam_id):
    exam = Exam.query.get(exam_id)

    if not exam:
        flash("Exame não encontrado", "error")
        return redirect(url_for('listar_exames'))

    if request.method == 'POST':
        # Excluir todas as ExamQuestion associadas ao exame
        exam_questions = tables.ExamQuestion.query.filter_by(Exam_id=exam_id).all()
        finalized_exam = tables.FinalizedExam.query.filter_by(exam_id=exam_id).all()
        for exam_question in exam_questions:
            db.session.delete(exam_question)
        for finalized_exam in finalized_exam:
            db.session.delete(finalized_exam)


        # Excluir o exame após remover todas as ExamQuestion associadas
        db.session.delete(exam)
        db.session.commit()

        # Após a exclusão bem-sucedida, redirecionar para a página de listagem de exames.
        return redirect(url_for('listar_exames'))

    # Renderizar a página de confirmação de exclusão para solicitações GET.
    return render_template('confirm_delete.html', exam=exam)

def buscar_questao_por_id(questao_id):
    try:
        questao = tables.Question.query.get(questao_id)
        return questao
    except Exception as e:
        # Trate qualquer exceção que possa ocorrer durante a busca
        print("Erro ao buscar questão:", e)
        return None



@app.route('/buscar_questao', methods=['GET'])
def buscar_questao():
    questao_id = request.args.get('questao_id')
    if questao_id:

        if questao_id.isdigit():
            questao = buscar_questao_por_id(int(questao_id))
            if questao:
                # Se a questão for encontrada, renderize a página de detalhes da questão
                return render_template('detalhes_questao.html', questao=questao)
            else:
                # Se a questão não for encontrada, retorne uma mensagem ou redirecione para a página de listagem de questões
                return render_template('questao_nao_encontrada.html')
        else:
            # Se o ID fornecido não for um número válido, retorne uma mensagem de erro
            flash("ID inválido", "error")
            return render_template('busca_id_invalido.html')
    else:
        return render_template('listar_questoes.html')


def buscar_exame_por_id(exame_id):
    try:
        exame = Exam.query.get(exame_id)
        return exame
    except Exception as e:
        # Trate qualquer exceção que possa ocorrer durante a busca
        print("Erro ao buscar exame:", e)
        return None

@app.route('/buscar_exame', methods=['GET'])
def buscar_exame():
    exame_id = request.args.get('exame_id')
    if exame_id:
        if exame_id.isdigit():
            exame = buscar_exame_por_id(int(exame_id))
            if exame:
                # Se a prova for encontrada, renderize a página de detalhes da prova
                return render_template('detalhes_prova.html', exame=exame)
            else:
                # Se a prova não for encontrada, redirecione para a página de prova não encontrada
                flash("Prova não encontrada", "error")
                return render_template('prova_nao_encontrada.html')
        else:
            flash("ID inválido", "error")
            return render_template('busca_id_invalido_prova.html')
    else:
        return render_template('procurar_exames.html')

