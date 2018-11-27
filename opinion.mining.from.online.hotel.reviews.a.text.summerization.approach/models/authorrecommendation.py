from mongoengine import *


class AuthorRecommendation(Document):
    authorId = ObjectIdField(required=True)
    average_recommendation = FloatField()
    average_recommendation_score = FloatField()
