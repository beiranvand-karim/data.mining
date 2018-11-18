from mongoengine import *


class UserProfile(Document):
    url = StringField(required=True)
