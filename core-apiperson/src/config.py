import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_USERS", "sqlite:///test-core-apiperson.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    DEBUG = True

    if not os.environ.get('DATABASE_URL_USERS'):
        print('DATABASE_URL_USERS environment variable does not exist, you will be using in-memory storage.')
