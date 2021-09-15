from flask import Blueprint, jsonify

router = Blueprint('calculator', __name__, url_prefix='/calculator')

@router.route('/', methods=['GET'])
def simulate():
    data = {
        'message': 'Este metodo aun no esta implementado'
    }
    return jsonify(data)