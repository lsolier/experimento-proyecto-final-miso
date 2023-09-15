from flask_restful import Resource
from src.main.modelos import db

# '/users/ping' Path
class HealthView(Resource):
    def get(self):
        return "pong"
