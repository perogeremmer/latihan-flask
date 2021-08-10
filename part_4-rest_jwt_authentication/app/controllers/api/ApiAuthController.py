from flask_jwt_extended.utils import create_refresh_token
from flask_restful import Resource
from flask import request
from datetime import timedelta
from app.models.user import User
from flask_jwt_extended import create_access_token, create_refresh_token

from app.response import response
from app.transformer.UserTransformer import UserTransformer
from werkzeug.security import generate_password_hash, check_password_hash


class RegisterController(Resource):
    def post(self):
        try:
            password = request.json['password']
            confirmation_password = request.json['confirmation_password']

            if password != confirmation_password:
                raise Exception(
                    'Password and confirmation password do not match')

            check_user = User.objects(email=request.json['email']).first()
            if check_user:
                raise Exception('User already exists!')

            user = User()
            user.name = request.json['name']
            user.email = request.json['email']
            user.password = generate_password_hash(password)
            user.save()

            payload = TokenGenerator(user).generate_access_token()

            return response.ok('User Registered!', payload)
        except Exception as e:
            return response.bad_request("{}".format(e), '')


class AuthController(Resource):
    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']
            
            user = User.objects(email=email).first()

            if not user:
                raise Exception('Email or password is invalid!')
            

            if not check_password_hash(user.password, password):
                raise Exception(
                    'Email or password is invalid!'
                )

            payload = TokenGenerator(user).generate_access_token()
    
            return response.ok(f'Succesfully logged in, welcome {user.name}!', payload)
        except Exception as e:
            return response.bad_request("{}".format(e), '')


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

