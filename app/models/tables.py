from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
        return User.query.filter_by(id=user_id).first()


class ExamQuestion(db.Model):
    __tablename__ = 'exam_question'
    Exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), primary_key=True)
    Question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), primary_key=True)
    nota = db.Column(db.Float)

    def __init__(self, Exam_id, Question_id, nota):
        self.Exam_id = Exam_id
        self.Question_id = Question_id
        self.nota = nota



class User(db.Model, UserMixin):
        __tablename__ = "users"
        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        username = db.Column(db.String, unique = True)
        email = db.Column(db.String, unique = True)
        password = db.Column(db.String)
        name = db.Column(db.String)
        role = db.Column(db.Boolean, default=False)

        def __init__(self, username, email, password, name, role):
                self.username = username
                self.email = email
                self.password = generate_password_hash(password)
                self.name = name
                self.role = role
        def __repr__(self):
                return "<User %r>" % self.username
        def verify_password(self, pwd):
                return check_password_hash(self.password, pwd)

class Question(db.Model):
        __tablename__ = "questions"
        id = db.Column(db.Integer, primary_key = True, autoincrement = True)
        statement = db.Column(db.Text)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        question_type = db.Column(db.Integer)
        answer_VouF = db.Column(db.Boolean)
        answer_Mult = db.Column(db.String)
        answer_ValNum = db.Column(db.Float)
        answer_Mult_A = db.Column(db.Text)
        answer_Mult_B = db.Column(db.Text)
        answer_Mult_C = db.Column(db.Text)
        answer_Mult_D = db.Column(db.Text)


        user = db.relationship('User', foreign_keys=user_id)

        exam_questions = db.relationship('ExamQuestion', backref='question', lazy='dynamic')



        def __init__(self, statement, question_type,  user_id):
                self.statement = statement
                self.question_type = question_type
                self.user_id = user_id
        
        def __repr__(self):
            return "<Question %r>" % self.id

class Exam(db.Model):
       __tablename__ = "exams"
       id = db.Column(db.Integer, primary_key = True, autoincrement = True)
       start_time = db.Column(db.DateTime)
       end_time = db.Column(db.DateTime)
       user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
       comment = db.Column(db.Text)

       user = db.relationship('User', foreign_keys=user_id)

       exam_questions = db.relationship('ExamQuestion', backref='exam', lazy='dynamic')
       
       def __init__(self, start_time, end_time, user_id, comment):
                self.start_time = start_time
                self.end_time = end_time
                self.user_id = user_id
                self.comment = comment

       def __repr__(self):
               return "<Exam %r>" % self.id
       

       
class FinalizedExam(db.Model):
       __tablename__ = "finalized_exams"
       id = db.Column(db.Integer, primary_key = True, autoincrement = True)
       user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
       exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'))
       answers_replied = db.Column(db.Text)

       def __init__(self, user_id, exam_id, answers_replied):
                self.user_id = user_id
                self.exam_id = exam_id
                self.answers_replied = answers_replied
       def __repr__(self):
               return "<FinalizedExam %r>" % self.id
               





