from app.transformer.TodoTransformer import TodoTransformer
from app.models.todo import Todo
from flask_restful import Resource
from datetime import datetime
from flask import render_template, make_response, request, redirect, url_for, flash


class WebTodoController(Resource):
    def get(self, id=None):
        try:
            if not id:
                todos = Todo.objects(deleted_at=None).all()
                todos = TodoTransformer.transform(todos)

                view = render_template('index.html', todo=todos)
            else:
                todo = Todo.objects(id=id).first()

                if not todo:
                    raise Exception('Todo not found')

                view = render_template('edit.html', todo=todo)

            return make_response(view)
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)

    def post(self):
        try:
            todo = Todo()
            todo.title = request.form['title']
            todo.description = request.form['description']
            todo.save()

            msg = 'Successfully create to-do!'
            flash(msg, 'success')

            return redirect('/todo')
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)


class WebTodoCreateController(Resource):
    def get(self):
        view = render_template('create.html')
        return make_response(view)


class WebTodoFinishController(Resource):
    def get(self, id):
        try:
            todo = Todo.objects(id=id).first()

            if not todo:
                raise Exception('Todo not found')

            todo.done = True
            todo.save()

            msg = 'Successfully finish to-do!'
            flash(msg, 'success')

            return redirect('/todo')
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)


class WebTodoUpdateController(Resource):
    def post(self, id):
        try:
            todo = Todo.objects(id=id).first()

            if not todo:
                raise Exception('Todo not found')

            todo.title = request.form['title']
            todo.description = request.form['description']
            todo.save()

            msg = 'Successfully update to-do!'
            flash(msg, 'success')

            return redirect('/todo')
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)


class WebTodoDeleteController(Resource):
    def post(self, id):
        try:
            todo = Todo.objects(id=id).first()

            if not todo:
                raise Exception('Todo not found')

            todo.deleted_at = datetime.now()
            todo.save()

            msg = 'Successfully delete to-do!'
            flash(msg, 'success')

            return redirect('/todo')
        except Exception as e:
            flash(f"{e}", 'danger')
            return redirect(request.referrer)
