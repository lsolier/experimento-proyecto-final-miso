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
            token_header = request.headers['authorization']
            print('TOKEN: ' + token_header)
            response = requests.get(Config.API_SECURITY_URL, headers={"Authorization": token_header, "Content-Type": "application/json"})
            if response.status_code != requests.codes.ok:
                print('Access denied, token is invalid')
                return '', requests.codes.unauthorized
            return f(*args, **kwargs)
        return decorated

