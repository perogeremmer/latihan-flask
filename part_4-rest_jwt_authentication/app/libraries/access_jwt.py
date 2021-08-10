from functools import wraps
from app.response import response
from flask_jwt_extended import verify_jwt_in_request

def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception as e:
            return response.un_authorized('Unauthorized!', '')
        return fn(*args, **kwargs)
    return wrapper