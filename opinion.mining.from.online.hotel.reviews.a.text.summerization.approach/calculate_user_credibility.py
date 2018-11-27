from mongoengine import connect, connection
from models.authorcredibility import AuthorCredibility
from models.user_reviews import UserReviews

dbname = "data-mining"
connect(dbname)
AuthorCredibility.drop_collection()


def calculate_author_credibility(user_reviews):
    total = user_reviews.hotels_ratings.__len__()
    sigma = 0
    if total > 0:
        for r in user_reviews.hotels_ratings:
            if r.user_given_rating == -1 or r.over_all_rating == -1:
                continue
            sigma = sigma + abs(r.user_given_rating - r.over_all_rating) / 5

        return 1 - sigma / total
    return None


review = UserReviews.objects.first()

for rev in UserReviews.objects:
    print(rev.username)
    credibility = calculate_author_credibility(rev)
    print(credibility)
    authorCredibility = AuthorCredibility(measure=calculate_author_credibility(rev), authorId=rev.id)
    authorCredibility.save()

connection.disconnect(dbname)


