import requests
from functools import wraps
from flask import request

from src.config import Config

class TokenValidator:

    def check_token(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if Config.DENY_ACCESS:
                print('Access denied, API_SECURITY_URL does not exist')
                return '', requests.codes.unauthorized
            try:
                token_header = request.headers['authorization']
                auth_token = token_header.split(maxsplit=1)[1]
            except:
                print("Access denied, an exception occurred reading the token, verify authorization header")
                return '', requests.codes.unauthorized
            print('TOKEN: ' + auth_token)
            __payload = {'token': auth_token}
            response = requests.get(Config.API_SECURITY_URL, params=__payload, verify=False)
            if response.status_code != requests.codes.ok:
                print('Access denied, token is invalid')
                return '', requests.codes.unauthorized
            return f(*args, **kwargs)
        return decorated