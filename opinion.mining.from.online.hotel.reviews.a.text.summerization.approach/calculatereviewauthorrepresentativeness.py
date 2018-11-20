from mongoengine import connect, connection
from models.authorcredibility import AuthorCredibility
from models.authorrecommendation import AuthorRecommendation
from models.reviewauthorrepresentativeness import ReviewAuthorRepresentativeness

connect("user-all-reviews")
ReviewAuthorRepresentativeness.drop_collection()


def calculate_review_author_representativeness(credibility, recommendation):
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

connection.disconnect("user-all-reviews")
