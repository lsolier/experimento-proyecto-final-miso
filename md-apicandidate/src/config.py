import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_USERS", "sqlite:///test-md-apicandidate.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = os.getenv("SECRET_KEY", "test_key")
    DEBUG = True
