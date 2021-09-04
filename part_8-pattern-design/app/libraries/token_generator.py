from flask_jwt_extended.utils import create_refresh_token
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token

from app.transformer.UserTransformer import UserTransformer

class TokenGenerator(object):
    def __init__(self, user):
        self.user = user

    def generate_access_token(self):
        payload = {
            "id": str(self.user.id),
        }

        access_token = create_access_token(
            identity=payload,
            fresh=True,
            expires_delta=timedelta(days=3)
        )


        refresh_token = create_refresh_token(
            identity=payload,
            expires_delta=timedelta(days=30)
        )

        self.user = UserTransformer.single_transform(self.user)

        self.user['token'] = {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

        return self.user