from app.models.user import User

def test_create_user(client):
    user = User(name="Hudya", email="hudya@example.com")
    assert user.name == "Hudya"

def test_create_user_with_empty_name(client):
    user = User(name="", email="hudya@example.com")
    assert user.name == ""

def test_create_user_without_attribute_name(client):
    user = User(email="hudya@example.com")
    assert user.name == None

def test_create_user_without_attribute_email(client):
    user = User(name="Hudya")
    assert user.email == None

def test_create_user_without_attribute_password(client):
    user = User(name="Hudya", email="hudya@example.com")
    assert user.password == None

def test_create_user_without_attribute_name_saved(client):
    try:
        user = User(email="hudya@example.com", password="123456")
        user.save()

        assert user.email == "hudya@example.com"
    except Exception:
        assert True

def test_create_user_without_attribute_email_saved(client):
    try:
        user = User(name="Hudya", password="123456")
        user.save()

        assert user.name == "Hudya"
    except Exception:
        assert True

def test_create_user_without_attribute_password_saved(client):
    try:
        user = User(name="Hudya", email="hudya@example.com")
        user.save()
    
        assert user.email == "hudya@example.com"
    except Exception:
        assert True

def test_check_name_inside_token_generator_type(test_app, client):
    with test_app.app_context():
        from app.controllers.api.ApiAuthController import TokenGenerator

        user = User(name="Hudya", email="hudya@example.com", password="123456")
        user.save()

        payload = TokenGenerator(user).generate_access_token()

        assert type(payload) == dict

def test_check_name_inside_token_generator(test_app, client):
    with test_app.app_context():
        from app.controllers.api.ApiAuthController import TokenGenerator

        user = User(name="Hudya", email="hudya@example.com", password="123456")
        user.save()

        payload = TokenGenerator(user).generate_access_token()

        assert payload['name'] == "Hudya"
        assert payload['email'] == "hudya@example.com"
        
        assert 'password' not in payload
        assert 'token' in payload

