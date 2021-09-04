from app.core.service.todo_service import TodoService
from flask_restful import Resource
from flask import request
from datetime import datetime
from app.models.todo import Todo

from app.response import response
from app.transformer.TodoTransformer import TodoTransformer
from app.libraries.access_jwt import jwt_required, get_identity

class TodoController(Resource):

    @jwt_required
    def get(self, id=None):
        user_id = get_identity()['id']

        if not id:
            q = request.args.get('q')

            todos = TodoService()
            todos = todos.get(q=q, user_id=user_id)
        else:
            todos = TodoService()
            todos = todos.get_by_id(id, user_id=user_id)

        return response.ok('', todos)

    @jwt_required
    def post(self):
        try:
            user_id = get_identity()['id']

            if not request.json['title']:
                raise Exception('Title is required')

            todo = TodoService()
            todo = todo.create(
                user_id=user_id,
                title=request.json['title'], 
                description=request.json['description']
            )

            return response.ok('Todo Created!', todo)
        except Exception as e:
            return response.bad_request("{}".format(e), '')


    @jwt_required
    def put(self, id):
        try:
            user_id = get_identity()['id']

            if not request.json['title']:
                raise Exception('Title is required!')

            todo = TodoService()
            todo = todo.update(id, 
                user_id=user_id, 
                title=request.json['title'], 
                description=request.json['description'],
                done=request.json['done']
            )

            return response.ok('Todo Updated!', todo)
        except Exception as e:
            return response.bad_request("{}".format(e), '')

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_identity()['id']
            
            todo = TodoService()
            todo = todo.delete(id, user_id=user_id)

            return response.ok('Todo Deleted!', todo)
        except Exception as e:
            return response.bad_request("{}".format(e), '')