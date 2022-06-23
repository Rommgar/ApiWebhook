
PREFIX_URL = '/api/v1'


def test_get_senders(client):
    """
    Test that the GET /api/v1/senders endpoint returns a list of senders.
    """
    response = client.get(f'{PREFIX_URL}/senders')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


def test_get_sender(client):
    """
    Test that the GET /api/v1/senders/<sender_id> endpoint returns a sender.
    """
    response = client.get(f'{PREFIX_URL}/senders/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


def test_delete_sender(client):
    """
    Test that the DELETE /senders/<sender_id> endpoint deletes a sender.
    """
    response = client.delete(f'{PREFIX_URL}/senders/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


def test_create_sender(client):
    """
    Test that the POST /senders endpoint creates a sender.
    """
    response = client.post(f'{PREFIX_URL}/senders')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


def test_update_sender(client):
    """
    Test that the PUT /senders/<sender_id> endpoint updates a sender.
    """
    response = client.put(f'{PREFIX_URL}/senders/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


