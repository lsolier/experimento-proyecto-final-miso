import jwt
import requests
from flask_restful import Resource
from flask import request

from src.config import Config
from src.main.vistas.token_validator import TokenValidator

# '/users/ping' Path
class HealthView(Resource):
    def get(self):
        return "pong"

# '/candidates/me' Path
class CandidatesView(Resource):

    @TokenValidator.check_token
    def get(self):
        token_header = request.headers['authorization']
        auth_token = token_header.split(maxsplit=1)[1]
        try:
            token_payload = jwt.decode(auth_token, options={"verify_signature": False})
            print('Token payload: {0}'.format(token_payload))
        except Exception as err:
            print("Error decoding token: {0}".format(err))
            return '', requests.codes.unauthorized

        __payload = {'id_candidate': token_payload['sub']}
        response = requests.get(Config.API_PERSON_URL, params=__payload, verify=False)
        if response.status_code != requests.codes.ok:
            print('Error reading person: {0}'.format(response.status_code))
            return '', requests.codes.service_unavailable

        candidate_found = response.json()
        return {"username": candidate_found["username"], "email": candidate_found["email"]}, requests.codes.ok

