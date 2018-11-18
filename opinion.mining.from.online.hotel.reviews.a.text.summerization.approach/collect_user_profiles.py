from mongoengine import *
from models.user_profiles import UserProfile

connect("user-all-reviews")
urls = [
    "https://www.tripadvisor.com/Profile/OliviaF_12?fid=3fa10694-cae7-486d-973a-30dee803c43e",
    ]

for url in urls:
    user_profile = UserProfile(url=url)
    user_profile.save()


# 246 is meant to be scraped
