from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
    
db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False, unique=True)
    createdAt = db.Column(db.DateTime, nullable = False, default = datetime.now)

class PersonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        include_relationships = True
        load_instance = True

class GetPersonByIdSchemaValidation(Schema):
    id = fields.Integer(required=True)

class PersonBaseSchemaValidation(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)