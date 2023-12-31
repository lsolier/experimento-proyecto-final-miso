from src import create_app
import logging
from flask_restful import Api
from flask_cors import CORS
from src.main.vistas import HealthView, CandidatesView

app = create_app(__name__)
logging.basicConfig(level=logging.DEBUG)
app_context = app.app_context()
app_context.push()
cors = CORS(app)

api = Api(app)
api.add_resource(HealthView,'/candidates/ping')
api.add_resource(CandidatesView,'/candidates/me')

