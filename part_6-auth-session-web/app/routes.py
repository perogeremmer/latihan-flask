from app import api, web
from app.controllers import MyController, MyViewController, TodoController, AuthController
from app.controllers.api import ApiTodoController, ApiAuthController

api.add_resource(ApiAuthController.RegisterController, '/register')
api.add_resource(ApiAuthController.AuthController, '/login')
api.add_resource(ApiAuthController.RefreshTokenController, '/token/refresh')

web.add_resource(AuthController.WebRegisterController, '/register')
web.add_resource(AuthController.WebAuthController, '/sign-in')
web.add_resource(AuthController.WebLogoutController, '/logout')


api.add_resource(ApiTodoController.TodoController, '/todo', '/todo/<string:id>')
web.add_resource(TodoController.WebTodoController, '/todo', '/todo/<string:id>')
web.add_resource(TodoController.WebTodoFinishController, '/todo/<string:id>/finish')
web.add_resource(TodoController.WebTodoUpdateController, '/todo/<string:id>/update')
web.add_resource(TodoController.WebTodoDeleteController, '/todo/<string:id>/delete')
web.add_resource(TodoController.WebTodoCreateController, '/todo/create')

api.add_resource(MyController.MyController, '/')
web.add_resource(MyViewController.MyViewController, '/')
web.add_resource(MyViewController.MySecondViewController, '/say-my-name')
