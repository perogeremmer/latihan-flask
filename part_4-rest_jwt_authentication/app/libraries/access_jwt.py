from functools import wraps
from app.response import response
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request(fresh=True)
        except Exception as e:
            return response.un_authorized('Unauthorized!', '')
        return fn(*args, **kwargs)
    return wrapper

def refresh_jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request(refresh=True)
        except Exception as e:
            return response.un_authorized('Unauthorized!', '')
        return fn(*args, **kwargs)
    return wrapper

def get_identity():
    return get_jwt_identity()