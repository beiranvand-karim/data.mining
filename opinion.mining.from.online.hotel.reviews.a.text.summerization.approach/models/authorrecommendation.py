from mongoengine import *


class AuthorRecommendation(Document):
    authorId = ObjectIdField(required=True)
    average_recommendation = FloatField(required=True)
    average_recommendation_score = IntField(required=True)
