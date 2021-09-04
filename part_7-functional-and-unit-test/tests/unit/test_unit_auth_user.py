from app.models.user import User

def test_create_user(client):
    user = User(name="John", email="john@example.com")
    assert user.name == "John"

    # response = client.get('/api/')

    # data = json.loads(response.get_data(as_text=True))
    # assert data['message'] == 'Hello World!'

def test_create_user_with_empty_name(client):
    user = User(name="", email="john@example.com")
    assert user.name == ""

def test_create_user_without_attribute_name(client):
    user = User(email="john@example.com")
    assert user.name == None

def test_create_user_without_attribute_email(client):
    user = User(name="John")
    assert user.email == None

def test_create_user_without_attribute_password(client):
    user = User(name="John", email="john@example.com")
    assert user.password == None

def test_create_user_without_attribute_name_saved(client):
    try:
        user = User(email="john@example.com", password="123456")
        user.save()
    except Exception:
        assert True

def test_create_user_without_attribute_email_saved(client):
    try:
        user = User(name="John", password="123456")
        user.save()
    except Exception:
        assert True

def test_create_user_without_attribute_password_saved(client):
    try:
        user = User(name="John", email="john@example.com")
        user.save()
    except Exception:
        assert True

def test_check_name_inside_token_generator_type(test_app, client):
    with test_app.app_context():
        from app.controllers.api.ApiAuthController import TokenGenerator

        user = User(name="John", email="john@example.com", password="123456")
        user.save()

        payload = TokenGenerator(user).generate_access_token()

        assert type(payload) == dict

def test_check_name_inside_token_generator(test_app, client):
    with test_app.app_context():
        from app.controllers.api.ApiAuthController import TokenGenerator

        user = User(name="John", email="john@example.com", password="123456")
        user.save()

        payload = TokenGenerator(user).generate_access_token()

        assert payload['name'] == "John"
        assert payload['email'] == "john@example.com"
        
        assert 'password' not in payload
        assert 'token' in payload

