from random import randint
from time import sleep
from models.user_profiles import UserProfile
from models.user_reviews import UserReviews, HotelsRatings
from mongoengine import *
from all_user_reviews import get_user_all_reviews_and_ratings

connect("user-all-reviews")
UserReviews.drop_collection()
HotelsRatings.drop_collection()

url = 'https://www.tripadvisor.com/Profile/' \
      'rethot?fid=fc096feb-9bc1-4b8c-8186-46de8a3770f6'

for profile in UserProfile.objects:
    print(profile.url)
    response = get_user_all_reviews_and_ratings(profile.url)
    sleep(randint(3, 4))

connection.disconnect("user-all-reviews")
