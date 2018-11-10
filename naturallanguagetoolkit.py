from process import process_al_reviews
from session import session
from gansevoortreview import GansevoortReview


process_al_reviews(session.query(GansevoortReview).all())

print("data pre processed")
