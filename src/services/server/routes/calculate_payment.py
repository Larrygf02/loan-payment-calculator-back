from flask import Blueprint, jsonify, request
from services.process import calculate_payment

router = Blueprint('calculator', __name__, url_prefix='/calculator')

@router.route('/', methods=['POST'])
def simulate():
    data = request.get_json(force=True)
    result = calculate_payment(data)
    return jsonify(result)