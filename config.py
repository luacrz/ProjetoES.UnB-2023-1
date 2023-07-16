#import os.path
#basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True


SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

#SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db' + os.path.join(basedir, 'storage.tb')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'chave_qualquer'
