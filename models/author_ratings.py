import mongoengine as me


class AuthorRatings(me.Document):
    author = me.StringField(required=True)
    rating = me.IntField(required=True)
    date = me.StringField(required=True)
