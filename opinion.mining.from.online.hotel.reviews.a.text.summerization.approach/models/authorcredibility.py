from mongoengine import *


class AuthorCredibility(Document):
    authorId = ObjectIdField(required=True)
    measure = FloatField(required=True)
