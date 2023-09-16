from src import create_app
import logging
from flask_restful import Api
from flask_cors import CORS
from src.main.vistas import HealthView, PersonsView, PersonView
from src.main.modelos import db


# app setup
app = create_app(__name__)
logging.basicConfig(level=logging.DEBUG)
app_context = app.app_context()
app_context.push()
# db setup
db.init_app(app)
db.create_all()
# Cors
cors = CORS(app)

# endpoints definition
api = Api(app)
api.add_resource(PersonsView,'/persons')
api.add_resource(HealthView,'/persons/ping')
api.add_resource(PersonView,'/persons/<id>')

