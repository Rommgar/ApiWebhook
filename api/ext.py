from flask import jsonify
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

ma = Marshmallow()
migrate = Migrate()


def response(request_url, request_method, result=None, status_message='succes', status_code=200):
    if result is None:
        result = []
    response_ = {
        'url': request_url,
        'method': request_method,
        'status': status_message,
        'status_code': status_code,
        'result': result if type(result) is list else [result]
    }
    return jsonify(response_), status_code
