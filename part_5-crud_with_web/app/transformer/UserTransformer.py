from app.transformer.BaseTransformer import BaseTransformer

class UserTransformer(BaseTransformer):     
    @staticmethod
    def single_transform(value):
        return {
            'id': str(value.id),
            'name': value.name,
            'email': value.email,
            'created_at': str(value.created_at),
            'updated_at': str(value.updated_at)
        }