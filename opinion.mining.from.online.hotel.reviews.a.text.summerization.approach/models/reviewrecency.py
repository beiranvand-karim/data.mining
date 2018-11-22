from mongoengine import Document, ObjectIdField, FloatField


class ReviewRecency(Document):
    reviewId = ObjectIdField(required=True)
    value = FloatField(required=True)
