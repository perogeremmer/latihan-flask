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


            todos = Todo.objects(title__contains=q, deleted_at=None, user_id=user_id).all()
            todos = TodoTransformer.transform(todos)
        else:
            todos = Todo.objects(id=id, deleted_at=None, user_id=user_id).first()
            
            if not todos:
                return response.bad_request('Todo not found!', '')

            todos = TodoTransformer.single_transform(todos)

        return response.ok('', todos)

    @jwt_required
    def post(self):
        try:
            user_id = get_identity()['id']

            if not request.json['title']:
                raise Exception('Title is required')

            todo = Todo()
            todo.title = request.json['title']
            todo.description = request.json['description']
            todo.user_id = user_id
            todo.save()

            return response.ok('Todo Created!', TodoTransformer.single_transform(todo))
        except Exception as e:
            return response.bad_request("{}".format(e), '')


    @jwt_required
    def put(self, id):
        try:
            user_id = get_identity()['id']

            if not request.json['title']:
                raise Exception('Title is required!')

            todo = Todo.objects(id=id).first()

            if not todo:
                return response.not_found('Todo not found!', '')

            if str(todo.user_id.id) != user_id:
                raise Exception("The owner is invalid!")

            todo.title = request.json['title']
            todo.description = request.json['description']
            todo.done = request.json['done']
            todo.updated_at = datetime.now()
            todo.save()

            return response.ok('Todo Updated!', TodoTransformer.single_transform(todo))
        except Exception as e:
            return response.bad_request("{}".format(e), '')

    @jwt_required
    def delete(self, id):
        try:
            user_id = get_identity()['id']
            
            todo = Todo.objects(id=id).first()

            if not todo:
                return response.not_found('Todo not found!', '')

            if str(todo.user_id.id) != user_id:
                raise Exception("The owner is invalid!")

            if todo.deleted_at:
                return response.bad_request('Todo already deleted!', '')


            todo.deleted_at = datetime.now()
            todo.save()

            return response.ok('Todo Deleted!', TodoTransformer.single_transform(todo))
        except Exception as e:
            return response.bad_request("{}".format(e), '')