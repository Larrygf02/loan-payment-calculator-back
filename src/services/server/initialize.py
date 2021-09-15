from flask import Flask
from .routes import configure_routes

def initialize_server():
    app = Flask(__name__)
    configure_routes(app)
    #configure_error_handlers(app) pendiente
    return app