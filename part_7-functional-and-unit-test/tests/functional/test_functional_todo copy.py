import json

def test_create_todo(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

def test_create_todo_with_empty_title(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 400

def test_create_todo_with_empty_description(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

def test_create_todo_with_empty_headers(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    payload = {
        "title": "Mencuci motor",
        "description": "",
    }
    response = client.post('/api/todo', json=payload)

    assert response.status_code == 401

def test_create_todo_with_empty_token(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    token = ""

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }

    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 401

def test_update_todo(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "title": "Mencuci motor baru",
        "description": "Mencuci Motor supra",
        "done": False
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor baru"
    assert data['values']['done'] == False


def test_update_todo_done_status(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "title": "Mencuci motor baru",
        "description": "Mencuci Motor supra",
        "done": True
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor baru"
    assert data['values']['done'] == True


def test_update_todo_with_empty_description(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "title": "Mencuci motor baru",
        "description": "",
        "done": False
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor baru"
    assert data['values']['description'] == ""
    assert data['values']['done'] == False

def test_update_todo_empty_title(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "title": "",
        "description": "Mencuci Motor supra",
        "done": False
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 400

def test_update_todo_without_title_object(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "description": "Mencuci Motor supra",
        "done": False
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 400


def test_update_todo_without_description_object(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "title": "Mencuci Motor supra",
        "done": False
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 400


def test_update_todo_without_done_object(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "title": "Mencuci Motor supra",
        "description": "Mencuci Motor supra",
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 400


def test_update_todo_with_different_user(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload_user = {
        "name": "Hudya",
        "email": "perogeremmer@mail.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response_user = client.post('/api/register', json=payload_user)
    data = json.loads(response_user.get_data(as_text=True))
    token_user = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
        "done": False
    }
    response = client.put(f'/api/todo/{id}', json=payload, headers={'Authorization': token_user})
    assert response.status_code == 400

def test_delete_todo(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {}
    response = client.delete(f'/api/todo/{id}', json=payload, headers={'Authorization': token})
    assert response.status_code == 200


def test_delete_todo_with_different_user(client, database):
    payload = {
        "name": "John",
        "email": "john@example.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response = client.post('/api/register', json=payload)

    data = json.loads(response.get_data(as_text=True))
    token = "Bearer {}".format(data['values']['token']['access_token'])

    payload_user = {
        "name": "Hudya",
        "email": "perogeremmer@mail.com",
        "password": "12345678",
        "confirmation_password": "12345678",
    }
    response_user = client.post('/api/register', json=payload_user)
    data = json.loads(response_user.get_data(as_text=True))
    token_user = "Bearer {}".format(data['values']['token']['access_token'])

    payload = {
        "title": "Mencuci motor",
        "description": "Mencuci Motor supra",
    }
    response = client.post('/api/todo', json=payload, headers={'Authorization': token})
    assert response.status_code == 200

    data = json.loads(response.get_data(as_text=True))
    assert data['values']['title'] == "Mencuci motor"
    assert data['values']['done'] == False

    id = data['values']['id']

    payload = {}
    response = client.delete(f'/api/todo/{id}', json=payload, headers={'Authorization': token_user})
    assert response.status_code == 400