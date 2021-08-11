from datetime import datetime
from mongoengine import Document, StringField, DateTimeField

class User(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)

    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now, onupdate=datetime.now)
    deleted_at = DateTimeField(default=None)