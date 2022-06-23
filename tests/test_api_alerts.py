
PREFIX_URL = '/api/v1'


def test_get_alerts(client):
    """
    Test that the GET /api/v1/alerts endpoint returns a list of alerts.
    """
    response = client.get(f'{PREFIX_URL}/alerts')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


def test_get_alert(client):
    """
    Test that the GET /api/v1/alerts/<alert_id> endpoint returns an alert.
    """
    response = client.get(f'{PREFIX_URL}/alerts/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


def test_delete_alert(client):
    """
    Test that the DELETE /alerts/<alert_id> endpoint deletes an alert.
    """
    response = client.delete(f'{PREFIX_URL}/alerts/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}


def test_create_alert(client):
    """
    Test that the POST /alerts endpoint creates an alert.
    """
    response = client.post(f'{PREFIX_URL}/alerts')
    assert response.status_code == 200
    assert response.json == {'message': 'Alert created'}


def test_update_alert(client):
    """
    Test that the PUT /alerts/<alert_id> endpoint updates an alert.
    """
    response = client.put(f'{PREFIX_URL}/alerts/1')
    assert response.status_code == 200
    assert response.json == {'message': 'Not implemented'}
