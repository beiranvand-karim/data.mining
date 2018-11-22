from mongoengine import connect, connection
from models.gansevoortreview import GansevoortReview
from models.reviewhelpfulness import ReviewHelpfulness


def calculatereviewhelpfulness(value):
    return value / 5


dbname = "data-mining"
connect(dbname)

for review in GansevoortReview.objects:
    reviewhelpfulness = ReviewHelpfulness(
        reviewId=review.id,
        value=calculatereviewhelpfulness(review.rating)
    )
    reviewhelpfulness.save()


print(ReviewHelpfulness.objects.count())
connection.disconnect(dbname)
