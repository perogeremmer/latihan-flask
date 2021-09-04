from werkzeug.security import check_password_hash, generate_password_hash
from app.libraries.token_generator import TokenGenerator
from app.core.interface.user_interface import UserInterface
from app.models.user import User

class UserService(UserInterface):
    """User Service"""

    def __init__(self):
        """User Service constructor"""
        self.model = User

    def create(self, **kwargs):
        """Create a new user"""

        if not kwargs['email']:
            raise Exception('Email is required')

        if kwargs['password'] != kwargs['confirmation_password']:
            raise Exception('Password and confirmation password do not match')

        check_user = User.objects(email=kwargs['email']).first()
        if check_user:
            raise Exception('User already exists!')

        user = self.model()
        user.name = kwargs['name']
        user.email = kwargs['email']
        user.password = generate_password_hash(kwargs['password'])
        user.save()

        payload = TokenGenerator(user).generate_access_token()

        return payload

    def auth(self, **kwargs):
        """Authenticate a user"""
        user = self.model.objects(email=kwargs['email']).first()

        if not user:
            raise Exception('Email or password is invalid!')
            

        if not check_password_hash(user.password, kwargs['password']):
            raise Exception(
                'Email or password is invalid!'
        )

        payload = TokenGenerator(user).generate_access_token()

        return payload

    