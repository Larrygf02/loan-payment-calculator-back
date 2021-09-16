from flask import Flask
from flask_cors import CORS
#from .routes import configure_routes

def initialize_server():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    #configure_routes(app)
    #configure_error_handlers(app) pendiente
    return app