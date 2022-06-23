from flask import blueprints, jsonify

blueprint = blueprints.Blueprint('sender', __name__)


@blueprint.route('senders', methods=['GET'])
def get_senders():
    response = {'message': 'Not implemented'}
    return jsonify(response)


@blueprint.route('senders/<sender_id>', methods=['GET'])
def get_sender(sender_id):
    response = {'message': 'Not implemented'}
    return jsonify(response)


@blueprint.route('senders/<sender_id>', methods=['DELETE'])
def delete_sender(sender_id):
    response = {'message': 'Not implemented'}
    return jsonify(response)


@blueprint.route('senders', methods=['POST'])
def create_sender():
    response = {'message': 'Not implemented'}
    return jsonify(response)


@blueprint.route('senders/<sender_id>', methods=['PUT'])
def update_sender(sender_id):
    response = {'message': 'Not implemented'}
    return jsonify(response)
