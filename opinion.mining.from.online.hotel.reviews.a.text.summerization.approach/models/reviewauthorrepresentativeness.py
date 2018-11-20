from mongoengine import Document, FloatField, ObjectIdField


class ReviewAuthorRepresentativeness(Document):
    authorId = ObjectIdField(required=True)
    value = FloatField(required=True)
