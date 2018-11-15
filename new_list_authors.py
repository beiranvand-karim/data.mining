from random import randint
from time import time, sleep
import mongoengine as me
from crawling.trimming import make_url, trim_rating
from driver import driver
from models.author_ratings import AuthorRatings

# try:
me.connect("author-ratings")
AuthorRatings.drop_collection()

start_time = time()
requests = 0

for i in range(218, 219):
    url = make_url(i)
    driver.get(url)

    reviews = driver.find_elements_by_css_selector('.review-container')
    for review in reviews:
        name = review.find_element_by_css_selector('.info_text div:nth-child(1)').text
        rating = trim_rating(review.find_element_by_css_selector('div.ui_column.is-9 > span.ui_bubble_rating'))
        date = review.find_element_by_class_name('ratingDate').get_attribute("title")
        record = AuthorRatings(rating=rating, date=date, author=name)
        record.save()
        pic = review.find_element_by_css_selector(".memberOverlayLink.clickable")
        pic.click()
        sleep(5)
        back_drop = driver.find_element_by_css_selector('.memberOverlayRedesign > a').click()
        sleep(randint(8))
        driver.back()

# except Exception as e:
#     print("______________________________________")
#     print(e)
#     print("_________________________________________")
#     status = driver.title
#     if driver.title:
#     driver.close()
