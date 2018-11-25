from mongoengine import Document, StringField, FloatField


class GansevoortReview(Document):
    name = StringField()
    date = StringField(required=True)
    rating = FloatField()
    title = StringField()
    description = StringField(required=True)
