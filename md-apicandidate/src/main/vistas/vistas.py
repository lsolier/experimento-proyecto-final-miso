from flask_restful import Resource
from flask import request
from src.main.modelos import db
from src.main.vistas.token_validator import TokenValidator

# '/users/ping' Path
class HealthView(Resource):
    def get(self):
        return "pong"

# '/candidates/me' Path
class CandidatesView(Resource):

    @TokenValidator.check_token
    def get(self):
        print('TOKEN VALIDADO')
        #Agregar logica para llamar al servicio persona
        return {"message": "Obtuviste tu info"}, 200
