import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_USERS", "sqlite:///test-md-apicandidate.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    JWT_SECRET_KEY = os.getenv("SECRET_KEY", "test_key")
    DEBUG = True

    DENY_ACCESS = False
    API_SECURITY_URL = os.environ.get("API_SECURITY_URL")
    if not os.environ.get('API_SECURITY_URL'):
        DENY_ACCESS = True
        print('API_SECURITY_URL environment variable does not exist, you will not be able to validate your identity.')
    else:
        print("API_SECURITY_URL: {0}".format(API_SECURITY_URL))

    API_PERSON_URL = os.environ.get("API_PERSON_URL")
    if not os.environ.get('API_PERSON_URL'):
        DENY_ACCESS = True
        print('API_PERSON_URL environment variable does not exist, you will not be able to validate your identity.')
    else:
        print("API_PERSON_URL: {0}".format(API_PERSON_URL))
