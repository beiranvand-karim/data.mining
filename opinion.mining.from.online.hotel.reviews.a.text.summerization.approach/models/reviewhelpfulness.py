from mongoengine import Document, ObjectIdField, FloatField


class ReviewHelpfulness(Document):
    reviewId = ObjectIdField(required=True)
    value = FloatField(required=True)
