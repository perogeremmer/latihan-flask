from app.libraries.token_generator import TokenGenerator
from flask_jwt_extended.internal_utils import verify_token_type
from flask_jwt_extended.utils import get_jwt, get_jwt_identity
from flask_restful import Resource
from flask import request
from app.models.user import User

from app.response import response

from app.libraries.access_jwt import refresh_jwt_required

from app.core.service.user_service import UserService

class RegisterController(Resource):
    def post(self):
        try:
            user = UserService()
            user = user.create(
                name=request.json['name'],
                email=request.json['email'], 
                password=request.json['password'],
                confirmation_password=request.json['confirmation_password']
            )

            return response.ok('User Registered!', user)
        except Exception as e:
            return response.bad_request("{}".format(e), '')


class AuthController(Resource):
    def post(self):
        try:
            email = request.json['email']
            password = request.json['password']
            
            user = UserService().auth(email=email, password=password)
    
            return response.ok(f'Succesfully logged in, welcome {user["email"]}!', user)
        except Exception as e:
            return response.bad_request("{}".format(e), '')


class RefreshTokenController(Resource):
    @refresh_jwt_required
    def post(self):
        try:

            token = get_jwt()
            
            if 'type' not in token and token['type'] != "refresh":
                return response.un_authorized("Token is not refresh token!", "");

            jwt_identity = get_jwt_identity()
            user = User.objects(id=jwt_identity['id']).first()

            if not user:
                return response.bad_request("Token is not valid", "")

            payload = TokenGenerator(user).generate_access_token()

            return response.ok(f'Token refreshed!', payload)
        except Exception as e:
            return response.bad_request("{}".format(e), '')