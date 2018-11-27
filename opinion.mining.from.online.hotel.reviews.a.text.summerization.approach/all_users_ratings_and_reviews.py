from random import randint
from time import sleep
from models.user_profiles import UserProfile
from models.user_reviews import UserReviews, HotelsRatings
from mongoengine import connection, connect
from all_user_reviews import get_user_all_reviews_and_ratings

connect("data-mining")
UserReviews.drop_collection()
HotelsRatings.drop_collection()

url = 'https://www.tripadvisor.com/Profile/' \
      'rethot?fid=fc096feb-9bc1-4b8c-8186-46de8a3770f6'
head = 1
for profile in UserProfile.objects[:50]:
    print(profile.url)
    response = get_user_all_reviews_and_ratings(profile.url, profile.id)
    sleep(randint(3, 4))
    print(head)
    head = head + 1
for profile in UserProfile.objects[50:100]:
    print(profile.url)
    response = get_user_all_reviews_and_ratings(profile.url, profile.id)
    sleep(randint(3, 4))
    print(head)
    head = head + 1

for profile in UserProfile.objects[100:150]:
    print(profile.url)
    response = get_user_all_reviews_and_ratings(profile.url, profile.id)
    sleep(randint(3, 4))
    print(head)
    head = head + 1

for profile in UserProfile.objects[150:]:
    print(profile.url)
    response = get_user_all_reviews_and_ratings(profile.url, profile.id)
    sleep(randint(3, 4))
    print(head)
    head = head + 1

print(head)

connection.disconnect("user-all-reviews")
