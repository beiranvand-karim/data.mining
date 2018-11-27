from mongoengine import connect, connection
from models.authorcredibility import AuthorCredibility
from models.authorrecommendation import AuthorRecommendation
from models.reviewauthorrepresentativeness import ReviewAuthorRepresentativeness

dbname = "data-mining"
connect(dbname)
ReviewAuthorRepresentativeness.drop_collection()


def calculate_review_author_representativeness(credibility, recommendation):
    if not credibility or not recommendation:
        return None
    return (credibility + recommendation) / 2


for author in AuthorCredibility.objects:
    ac = author.measure
    authorRecommendation = AuthorRecommendation.objects.get(authorId=author.authorId)
    ars = authorRecommendation.average_recommendation_score
    reviewAuthorRepresentativeness = ReviewAuthorRepresentativeness(
        authorId=author.authorId,
        value=calculate_review_author_representativeness(ac, ars)
    )
    reviewAuthorRepresentativeness.save()

connection.disconnect(dbname)
