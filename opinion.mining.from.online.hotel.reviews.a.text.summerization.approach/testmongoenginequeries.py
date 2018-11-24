from mongoengine import connect, EmbeddedDocument, StringField, ListField, Document, EmbeddedDocumentField
from models.reviewsentences import ReviewSentences

dbname = "data-mining"
connect(dbname)
ReviewSentences.drop_collection()


class Comment(EmbeddedDocument):
    content = StringField()


class Page(Document):
    comments = ListField(EmbeddedDocumentField(Comment))


comment1 = Comment(content='Good work!')
comment2 = Comment(content='Nice article!')
page = Page(comments=[comment1, comment2])

page.save()
