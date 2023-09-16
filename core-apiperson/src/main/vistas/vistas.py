import requests
from flask_restful import Resource
from flask import request
from marshmallow import ValidationError

from src.main.modelos import db, Person, PersonSchema, GetPersonByIdSchemaValidation, PersonBaseSchemaValidation

person_schema = PersonSchema()

# '/users/ping' Path
class HealthView(Resource):
    def get(self):
        return "pong"

# '/persons' Path
class PersonsView(Resource):

    def post(self):
        schema = PersonBaseSchemaValidation()
        try:
            schema.load(request.json)
        except ValidationError as err:
            print("Schema error: {0}".format(err))
            return "", requests.codes.not_found
        try:
            new_person = Person(name=request.json['name'], email=request.json['email'])
            db.session.add(new_person)
            db.session.commit()
        except Exception as err:
            print("DB error: {0}".format(err))
            return '', requests.codes.conflict
        return {"id": new_person.id, "name": new_person.name, "email": new_person.email, "createdAt": str(new_person.createdAt.isoformat())}, requests.codes.created

# '/persons/{id}' Path
class PersonView(Resource):

    def get(self, id):
        schema = GetPersonByIdSchemaValidation()
        try:
            schema.load({"id": id})
        except ValidationError as err:
            print("Schema error: {0}".format(err))
            return "", requests.codes.not_found

        retrieved_person = Person.query.filter_by(id=id).first()
        if retrieved_person is None:
            return '', requests.codes.not_found
        return person_schema.dump(retrieved_person), requests.codes.ok
