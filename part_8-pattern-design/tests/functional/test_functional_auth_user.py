import json

def test_create_user(client, database):
    payload = {
        "name": "Hudya",
        "email": "hudya@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['name'] == 'Hudya'

def test_create_user_with_empty_name(client, database):
    payload = {
        "name": "",
        "email": "hudya@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['name'] == ''

def test_create_user_with_empty_email(client, database):
    payload = {
        "name": "Hudya",
        "email": "",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)
    assert response.status_code == 400

def test_create_user_with_empty_password(client, database):
    payload = {
        "name": "Hudya",
        "email": "hudya@example.com",
        "password": "",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)
    assert response.status_code == 400

def test_create_user_with_empty_confirmation_password(client, database):
    payload = {
        "name": "Hudya",
        "email": "hudya@example.com",
        "password": "12345678",
        "confirmation_password": "",
    }
    response = client.post('/api/register', json=payload)
    assert response.status_code == 400

def test_auth_user(client, database):
    payload = {
        "name": "Hudya",
        "email": "hudya@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    client.post('/api/register', json=payload)


    payload = {
        "email": "hudya@example.com",
        "password": "12345678",
    }
    response = client.post('/api/login', json=payload)
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['name'] == "Hudya"
    assert 'token' in data['values']

def test_auth_user_with_wrong_password(client, database):
    payload = {
        "name": "Hudya",
        "email": "hudya@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    client.post('/api/register', json=payload)


    payload = {
        "email": "hudya@example.com",
        "password": "123456789",
    }
    response = client.post('/api/login', json=payload)
    assert response.status_code == 400

def test_auth_user_with_empty_password(client, database):
    payload = {
        "name": "Hudya",
        "email": "hudya@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    client.post('/api/register', json=payload)


    payload = {
        "email": "hudya@example.com",
        "password": "",
    }
    response = client.post('/api/login', json=payload)
    assert response.status_code == 400