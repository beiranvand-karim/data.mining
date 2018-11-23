from mongoengine import Document, StringField, ListField, ReferenceField, FloatField, ObjectIdField


class Sentence(Document):
    value = StringField(required=True)
    score = FloatField(required=True)


class ReviewSentences(Document):
    reviewId = ObjectIdField(required=True)
    sentences = ListField(ReferenceField(Sentence))
