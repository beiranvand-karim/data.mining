from mongoengine import Document, StringField, EmbeddedDocument, FloatField, ObjectIdField, \
    ListField, EmbeddedDocumentField


class Sentence(EmbeddedDocument):
    value = StringField(required=True)
    score = FloatField(required=True)


class ReviewSentences(Document):
    reviewId = ObjectIdField(required=True)
    # todo convert this to reference field
    sentences = ListField(EmbeddedDocumentField(Sentence))
    maximal = FloatField()
