from flask_restful import Resource
from flask import request
from datetime import datetime
from app.models.todo import Todo

from app.response import Response
from app.transformer.TodoTransformer import TodoTransformer

class TodoController(Resource):
    def get(self):
        todos = Todo.objects(deleted_at=None).all()
        todos = TodoTransformer.transform(todos)

        return Response.ok('', todos)

    def post(self):
        try:
            todo = Todo()
            todo.title = request.json['title']
            todo.description = request.json['description']
            todo.save()

            return Response.ok('Todo Created!', TodoTransformer.single_transform(todo))
        except Exception as e:
            return Response.bad_request(e, '')


    def put(self, id):
        todo = Todo.objects(id=id).first()

        if not todo:
            return Response.not_found('Todo not found!', '')

        todo.title = request.json['title']
        todo.description = request.json['description']
        todo.done = request.json['done']
        todo.save()

        return Response.ok('Todo Updated!', TodoTransformer.single_transform(todo))

    def delete(self, id):
        todo = Todo.objects(id=id).first()

        if not todo:
            return Response.not_found('Todo not found!', '')

        todo.deleted_at = datetime.now()
        todo.save()

        return Response.ok('Todo Deleted!', TodoTransformer.single_transform(todo))