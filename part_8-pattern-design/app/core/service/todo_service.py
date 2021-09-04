from datetime import datetime
from app.transformer.TodoTransformer import TodoTransformer
from app.core.interface.todo_interface import TodoInterface
from app.models.todo import Todo

class TodoService(TodoInterface):
    """Todo Service"""

    def __init__(self):
        """Todo Service constructor"""
        self.model = Todo

    def get(self, **kwargs):
        """Get a todo"""
        todos = Todo.objects(
            title__contains=kwargs['q'], 
            deleted_at=None, 
            user_id=kwargs['user_id']
        ).all()
        
        todos = TodoTransformer.transform(todos)

    def get_by_id(self, id, **kwargs):
        """Get todo By ID"""
        todos = Todo.objects(
            id=id, 
            deleted_at=None, 
            user_id=kwargs['user_id']
        ).first()
            
        if not todos:
            raise Exception('Todo not found!')

        todos = TodoTransformer.single_transform(todos)

    def create(self, **kwargs):
        """Create a new todo"""

        if not kwargs['title']:
            raise Exception('Title is required!')

        todo = self.model()
        todo.title = kwargs['title']
        todo.description = kwargs['description']
        todo.user_id = kwargs['user_id']
        todo.save()

        payload = TodoTransformer.single_transform(todo)
        return payload
    
    def update(self, id, **kwargs):
        """Update a todo"""
        if not kwargs['title']:
            raise Exception('Title is required!')

        todo = self.model.objects(id=id).first()

        if not todo:
            raise Exception('Todo is not found!')

        if str(todo.user_id.id) != kwargs['user_id']:
            raise Exception("The owner is invalid!")

        todo.title = kwargs['title']
        todo.description = kwargs['description']
        todo.done = kwargs['done']
        todo.updated_at = datetime.now()
        todo.save()

        payload = TodoTransformer.single_transform(todo)

        return payload

    def delete(self, id, **kwargs):
        """Delete a todo"""
        todo = self.model.objects(id=id).first()

        
        if not todo:
            raise Exception('Todo not found!')

        if str(todo.user_id.id) != kwargs['user_id']:
            raise Exception("The owner is invalid!")

        if todo.deleted_at:
            raise Exception('Todo already deleted!')


        todo.deleted_at = datetime.now()
        todo.save()

        payload = TodoTransformer.single_transform(todo)

        return payload