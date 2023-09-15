import responses
import requests
from flask_jwt_extended import decode_token
from flask_restful import Resource
from flask import request

from src.config import Config
from src.main.modelos import db
from src.main.vistas.token_validator import TokenValidator

# '/users/ping' Path
class HealthView(Resource):
    def get(self):
        return "pong"

# '/candidates/me' Path
class CandidatesView(Resource):

    @responses.activate
    @TokenValidator.check_token
    def get(self):
        print('TOKEN VALIDADO')
        token_header = request.headers['authorization']
        auth_token = token_header.split(maxsplit=1)[1]
        try:
            #token_info = decode_token(encoded_token=auth_token, csrf_value=None, allow_expired=True)
            token_info = "token-test"
        except Exception as err:
            print("Error decoding token: {0}".format(err))
            return '', requests.codes.unauthorized

        #Esto es un mock temporal
        self._mockResponse()

        __payload = {'id_candidato': 123}
        response = requests.get(Config.API_PERSON_URL, params=__payload, verify=False)
        if response.status_code != requests.codes.ok:
            print('Error reading person: {0}'.format(response.status_code))
            return '', requests.codes.service_unavailable

        candidate_found = response.json()
        return {"username": candidate_found["username"], "email": candidate_found["email"]}, requests.codes.ok

    def _mockResponse(self):
        mock_response = responses.Response(
            method="GET",
            url="http://api-person-url-mock",
            json={"username": "l.solier", "email": "l.solier@uniandes.edu.co"},
            status=200,
        )
        responses.add(mock_response)
