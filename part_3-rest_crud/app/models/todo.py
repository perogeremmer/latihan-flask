from datetime import datetime
from mongoengine import Document, StringField, BooleanField, DateTimeField, ListField, IntField

class Todo(Document):
    title = StringField(required=True)
    description = StringField(max_length=100)
    done = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    deleted_at = DateTimeField(default=None)