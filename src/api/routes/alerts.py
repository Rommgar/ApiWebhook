from flask import jsonify, Blueprint, request
from api.models.alert import Alert
from api.schemas.alert import AlertSchema
from api.ext import response

blueprint = Blueprint('alerts', __name__)
alert_schema = AlertSchema()


@blueprint.route('alerts', methods=['GET'])
def get_alerts():
    alerts = Alert.query.all()
    alerts_list = alert_schema.dump(alerts, many=True)
    return response(request.url, request.method, alerts_list)


@blueprint.route('alerts/<alert_id>', methods=['GET'])
def get_alert(alert_id):
    alert = Alert.query.get(alert_id)
    alert_dict = alert_schema.dump(alert)
    return response(request.url, request.method, alert_dict)


@blueprint.route('alerts/name/<name>', methods=['GET'])
def get_alert_by_name(name):
    alert = Alert.query.filter(Alert.name.like(f'%{name}%')).all()
    alerts_list = alert_schema.dump(alert, many=True)
    return response(request.url, request.method, alerts_list)


@blueprint.route('alerts/<alert_id>', methods=['DELETE'])
def delete_alert(alert_id):
    alert = Alert.query.get(alert_id)
    alert.delete()
    return response(request.url, request.method, alert_schema.dump(alert))


@blueprint.route('alerts', methods=['POST'])
def create_alert():
    data = request.get_json()
    alert_dict = alert_schema.load(data)
    alert = Alert(
        name=alert_dict['name'],
        description=alert_dict['description'],
    )
    alert.save()
    alert = alert_schema.dump(alert)
    return response(request.url, request.method, alert, status_code=201)


@blueprint.route('alerts/<alert_id>', methods=['PUT'])
def update_alert(alert_id):
    response = jsonify({'message': 'Not implemented'}), 404
    return response
