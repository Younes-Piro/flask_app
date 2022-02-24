from mongoengine import Document
from mongoengine.fields import (
    StringField,
)

class User(Document):
    meta = {'collection': 'users'}
    name = StringField()
    lastname = StringField()
