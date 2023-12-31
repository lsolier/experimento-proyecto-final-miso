import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    PROPAGATE_EXCEPTIONS = True
    DEBUG = True

    DENY_ACCESS = False
    MOCK_MODE = False
    API_SECURITY_URL = os.environ.get("API_SECURITY_URL")
    if not os.environ.get('API_SECURITY_URL'):
        MOCK_MODE = True
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
