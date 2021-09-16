from flask import jsonify
from app import app

# router = Blueprint('health', __name__, url_prefix='/health')

@app.route('/health', methods=['GET'])
def health():
    data = {
        'status': 'UP'
    }
    return jsonify(data)