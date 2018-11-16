from mongoengine import *

connect("test_embedded")


class User(Document):
    name = StringField()


class Page(Document):
    content = StringField()
    authors = ListField(ReferenceField(User))


bob = User(name="Bob Jones").save()
john = User(name="John Smith").save()

Page(content="Test Page", authors=[bob, john]).save()
Page(content="Another Page", authors=[john]).save()


for p in Page.objects:
    for a in p.authors:
        print(a.name)

