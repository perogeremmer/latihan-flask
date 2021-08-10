from app.transformer.BaseTransformer import BaseTransformer

class TodoTransformer(BaseTransformer):     
    @staticmethod
    def single_transform(value):
        return {
            'id': str(value.id),
            'title': value.title,
            'description': value.description,
            'done': value.done,
            'created_at': str(value.created_at),
            'updated_at': str(value.updated_at)
        }