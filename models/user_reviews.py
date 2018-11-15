import mongoengine as me


class HotelsRatings(me.Document):
    user_given_rating = me.StringField(required=True)
    name = me.StringField(required=True)
    over_all_rating = me.IntField(required=True)


class UserReviews(me.Document):
    username = me.StringField(required=True)
    name = me.StringField(required=True)
    hotels_ratings = me.EmbeddedDocumentListField(HotelsRatings)
