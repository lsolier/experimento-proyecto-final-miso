import requests
import os

from functools import wraps
from flask import request

from src.config import Config

API_SECURITY_URL = os.environ.get("API_SECURITY_URL")

class TokenValidator:

    def check_token(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if Config.DENY_ACCESS:
                print('ACCESS DENIED, API_SECURITY_URL DOES NOT EXIST')
                return '', 401
            token_header = request.headers['authorization']
            auth_token = token_header.split(maxsplit=1)[1]
            print('TOKEN: ' + auth_token)
            __url = "url_for_token_validation"
            __payload = {'token': auth_token}
            response = requests.get(API_SECURITY_URL, params=__payload, verify=False)
            #response = json.loads('{"status_code": 200}',  object_hook=lambda d: SimpleNamespace(**d))
            if response.status_code != requests.codes.ok:
                print('ACCESS DENIED, TOKEN IS INVALID')
                return '', 401
            return f(*args, **kwargs)
        return decorated