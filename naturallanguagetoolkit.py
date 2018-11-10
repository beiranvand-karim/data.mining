from models.mongo_gansevoort_reviews import MongoGansevoortReview
from process import process_all_reviews
from session import session
from models.gansevoortreview import GansevoortReview
import mongoengine as me


me.connect("data-mining")
MongoGansevoortReview.drop_collection()
print("collection dropped")
process_all_reviews(session.query(GansevoortReview).all())

print("data items count: " + MongoGansevoortReview.objects.count().__str__())
print("data pre processed")

first_review = MongoGansevoortReview.objects.first()
print(first_review.paragraph)
