import datetime
import mongoengine


class Snake(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    length = mongoengine.FloatField(required=True)
    name = mongoengine.StringField(required=True)
    species = mongoengine.StringField(required=True)
    is_venomous = mongoengine.BooleanField(required=True)


mongoengine.connect("test_project")

snake = Snake(length=12.6, name="karim", species="test", is_venomous=True)

snake.save()

for s in Snake.objects:
    print(s.name)
