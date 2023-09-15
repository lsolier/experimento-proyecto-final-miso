from flask import (
    Flask
)

def create_app(config_name):
    app = Flask(config_name)
    app.config.from_object("src.config.Config")
    return app
