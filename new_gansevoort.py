from time import sleep
from random import randint
from time import time
from crawling.trimming import trim_ratings, make_url
from driver import driver
from session import session, db
from models.gansevoortreview import GansevoortReview

# https://www.tripadvisor.com/Hotel_Review-g60763-d287626-Reviews-or5-Gansevoort_Meatpacking_NYC-New_York_City_New_York.html

start_time = time()
requests = 0

GansevoortReview.__table__.drop(db)

# for i in range(218, 261):
for i in range(218, 219):

    url = make_url(i)

    driver.get(url)
    link = driver.find_element_by_class_name('ulBlueLinks')
    link.click()
    sleep(randint(8, 15))

    reviews = driver.find_elements_by_css_selector('div.ui_column.is-9 > div.prw_rup > div.entry > p.partial_entry')
    dates = driver.find_elements_by_class_name('ratingDate')

    ratings = driver.find_elements_by_css_selector('div.ui_column.is-9 > span.ui_bubble_rating')
    ratings = trim_ratings(ratings)

    names = driver.find_elements_by_css_selector('.memberOverlayLink .info_text > div:nth-child(1)')

    addresses = driver.find_elements_by_css_selector('.memberOverlayLink .info_text > div > strong')

    contributions = driver.find_elements_by_css_selector('.memberBadgingNoText > span:nth-child(2)')
    likes = driver.find_elements_by_css_selector('.memberBadgingNoText > span:nth-child(4)')

    for j in range(0, len(reviews)):
        rev = GansevoortReview(
            id=i * 10 + j,
            date=dates[j].get_attribute('title'),
            description=reviews[j].text,
            # address=addresses[j].text,
            rating=ratings[j],
            contributions=contributions[j].text,
            # likes=likes[j].text,
            name=names[j].text
            )
        session.add(rev)
        session.commit()

    sleep(randint(8, 15))

    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))

driver.close()
session.close()