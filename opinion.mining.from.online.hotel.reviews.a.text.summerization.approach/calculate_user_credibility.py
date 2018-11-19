from mongoengine import connect, connection
from models.authorcredibility import AuthorCredibility
from models.user_reviews import UserReviews

connect("user-all-reviews")
AuthorCredibility.drop_collection()


def calculate_author_credibility(user_reviews):
    total = user_reviews.hotels_ratings.__len__()
    sigma = 0
    for r in user_reviews.hotels_ratings:
        if r.user_given_rating == -1 or r.over_all_rating == -1:
            continue
        sigma = sigma + abs(r.user_given_rating - r.over_all_rating) / 5

    return 1 - sigma / total


review = UserReviews.objects.first()

for rev in UserReviews.objects:
    print(calculate_author_credibility(rev))
    print(rev.id)
    authorCredibility = AuthorCredibility(measure=calculate_author_credibility(rev), authorId=rev.id)
    authorCredibility.save()

connection.disconnect("user-all-reviews")


