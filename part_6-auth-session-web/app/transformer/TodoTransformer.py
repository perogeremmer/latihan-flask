from app.transformer.BaseTransformer import BaseTransformer
from app.transformer.UserTransformer import UserTransformer


class TodoTransformer(BaseTransformer):
    @staticmethod
    def single_transform(value):
        return {
            'id': str(value.id),
            'title': value.title,
            'user_id': str(value.user_id.id) if value.user_id else "",
            'description': value.description,
            'done': value.done,
            'created_at': str(value.created_at),
            'updated_at': str(value.updated_at),
            'user_detail': UserTransformer.single_transform(value.user_id.fetch()) if value.user_id else {},
        }

"""
Return expected:
{
    "created_at": "2021-08-10 21:34:43.718532",
    "description": "Mencuci Motor supra",
    "done": false,
    "id": "61128e830a8dcf8df341b6c2",
    "title": "Mencuci motor",
    "updated_at": "2021-08-10 21:34:43.718541",
    "user_detail": {
        "created_at": "2021-08-09 21:25:15.970000",
        "email": "hudya@mail.com",
        "id": "61113acccc2e1c2b5b8d2288",
        "name": "Hudya",
        "updated_at": "2021-08-09 21:25:15.970000"
    },
    "user_id": "61113acccc2e1c2b5b8d2288"
}
"""
