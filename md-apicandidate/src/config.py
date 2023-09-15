import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_USERS", "sqlite:///test-md-apicandidate.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = os.getenv("SECRET_KEY", "test_key")
    DEBUG = True

    DENY_ACCESS = False
    if not os.environ.get('API_SECURITY_URL'):
        DENY_ACCESS = True
        print('API_SECURITY_URL environment variable does not exist, you will not be able to validate your identity.')
