from mongoengine import Document, StringField, FloatField, ObjectIdField, \
    ListField, ReferenceField


class Sentence(Document):
    value = StringField(required=True)
    score = FloatField(required=True)
    importance = FloatField()


class ReviewSentences(Document):
    reviewId = ObjectIdField(required=True)
    sentences = ListField(ReferenceField(Sentence))
    maximal = FloatField()
    scorecoefficient = FloatField()
