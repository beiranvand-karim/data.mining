from random import randint
from time import time, sleep
import mongoengine as me
from crawling.trimming import make_url, trim_ratings
from driver import driver
from models.author_ratings import AuthorRatings

me.connect("author-ratings")
AuthorRatings.drop_collection()

start_time = time()
requests = 0

for i in range(218, 220):
    url = make_url(i)
    driver.get(url)
    dates = driver.find_elements_by_class_name('ratingDate')
    ratings = trim_ratings(driver.find_elements_by_css_selector('div.ui_column.is-9 > span.ui_bubble_rating'))
    names = driver.find_elements_by_css_selector('.memberOverlayLink .info_text > div:nth-child(1)')

    pics = driver.find_elements_by_class_name("basicImg")

    for j in range(0, len(names)):
        print(pics[j].get_attribute("src"))
        record = AuthorRatings(date=dates[j].get_attribute("title"), author=names[j].text, rating=ratings[j], profile=pics[j].get_attribute("src"))
        record.save()

    sleep(randint(8, 15))

    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))

driver.close()
