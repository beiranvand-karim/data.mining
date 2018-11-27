from math import log
from mongoengine import connect, connection
from models.authorrecommendation import AuthorRecommendation
from models.user_reviews import UserReviews

dbname = "data-mining"
connect(dbname)
AuthorRecommendation.drop_collection()


def calculate_author_recommendation(reviews):
    sigma = 0
    count = 0
    if reviews.__len__() > 0:
        for review in reviews.hotels_ratings:
            if review.user_given_rating == -1:
                continue
            sigma = sigma + review.user_given_rating
            count = count + 1
        average = None
        if count > 0:
            average = sigma / count
        return average
    return None


def calculate_author_recommendation_score(average):
    if not average:
        return None
    if average > 3:
        return 1
    return log(average + 1, 2) / 2


for author in UserReviews.objects:
    arn = calculate_author_recommendation(author)
    ars = calculate_author_recommendation_score(arn)
    authorRecommendation = AuthorRecommendation(
        authorId=author.id,
        average_recommendation=arn,
        average_recommendation_score=ars
    )
    authorRecommendation.save()


connection.disconnect(dbname)
