from math import exp
from mongoengine import connect, connection
from models.gansevoortreview import GansevoortReview
from datetime import datetime
from models.reviewrecency import ReviewRecency


def parsedate(date):
    return datetime.strptime(date, '%B %d, %Y')


def calculatereviewrecency(date):
    lastreviewdate = parsedate('November 21, 2018')
    firstreviewdate = parsedate('December 15, 2003')
    dm = (lastreviewdate - firstreviewdate).total_seconds()
    t = (datetime.now() - date).total_seconds()
    return exp(-t / dm)


dbname = "data-mining"
connect(dbname)
ReviewRecency.drop_collection()


for review in GansevoortReview.objects:
    reviewrecency = ReviewRecency(
        reviewId=review.id,
        value=calculatereviewrecency(parsedate(review.date))
    )
    reviewrecency.save()


print(ReviewRecency.objects.count())
connection.disconnect(dbname)
