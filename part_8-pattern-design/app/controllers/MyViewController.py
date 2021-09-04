from flask_restful import Resource
from flask import render_template, make_response, request

class MyViewController(Resource):
    def get(self):
        view = render_template('index.html')
        return make_response(view)

class MySecondViewController(Resource):
    def get(self):
        name = request.args.get('name')

        if not name:
            name = "Hudya"

        view = render_template('say-my-name.html', name=name)
        return make_response(view)
