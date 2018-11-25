from mongoengine import connection, connect
from models.user_profiles import UserProfile

urls = [
    "https://www.tripadvisor.com/Profile/littleswallow",
    "https://www.tripadvisor.com/Profile/OliviaF_12"
    ]
dbname = 'data-mining'
connect(dbname)


for url in urls:
    user_profile = UserProfile(url=url)
    user_profile.save()


connection.disconnect(dbname)
