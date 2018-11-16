from mongoengine import *


class HotelsRatings(Document):
    user_given_rating = FloatField(required=True)
    name = StringField(required=True)
    over_all_rating = FloatField(required=True)


class UserReviews(Document):
    username = StringField(required=True)
    name = StringField(required=True)
    hotels_ratings = ListField(ReferenceField(HotelsRatings))
