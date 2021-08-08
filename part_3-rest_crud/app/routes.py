from app import api, web
from app.controllers import MyController, MyViewController
from app.controllers.api import ApiTodoController

api.add_resource(ApiTodoController.TodoController, '/todo', '/todo/<string:id>')

api.add_resource(MyController.MyController, '/')
web.add_resource(MyViewController.MyViewController, '/')
web.add_resource(MyViewController.MySecondViewController, '/say-my-name')
