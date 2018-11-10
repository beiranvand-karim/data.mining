import mongoengine as me


class MongoGansevoortReview(me.Document):
    corresponding_id = me.IntField(required=True)
    paragraph = me.ListField(required=True)
    description = me.StringField(required=True)
    date = me.StringField(required=True)
