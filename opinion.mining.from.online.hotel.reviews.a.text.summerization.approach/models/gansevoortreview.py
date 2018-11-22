from mongoengine import Document, StringField, FloatField


class GansevoortReview(Document):
    date = StringField(required=True)
    rating = FloatField()
    description = StringField(required=True)
