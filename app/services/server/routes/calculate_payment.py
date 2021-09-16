from flask import jsonify, request
from services.process import calculate_payment
from app import app

#router = Blueprint('calculator', __name__, url_prefix='/calculator')

@app.route('/calculator', methods=['POST'])
def simulate():
    data = request.get_json(force=True)
    result = calculate_payment(data)
    return jsonify(result)