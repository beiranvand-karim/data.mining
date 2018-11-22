from random import randint
from time import sleep
from mongoengine import connect, connection
from selenium.common.exceptions import NoSuchElementException
from calculatereviewrecency import parsedate
from crawling.trimming import trim_rating, make_url
from driver import driver
from models.gansevoortreview import GansevoortReview

db_name = "user-all-reviews"
connect(db_name)
GansevoortReview.drop_collection()

def checkdaterange(date):
    startdate = parsedate('January 1, 2012')
    enddate = parsedate('March 31, 2013')
    print(date)
    if startdate <= date <= enddate:
        return True
    return False


for i in range(218, 261):
    url = make_url(i)
    print(i)
    print(url)
    driver.get(url)
    link = driver.find_element_by_css_selector('.taLnk.ulBlueLinks')
    link.click()
    sleep(randint(5, 7))

    reviews = driver.find_elements_by_css_selector('.review-container')

    for review in reviews:

        try:
            rating = review.find_element_by_css_selector('div.ui_column.is-9 > span.ui_bubble_rating')
        except NoSuchElementException:
            rating = None

        description = review.find_element_by_css_selector('div.ui_column.is-9 > div.prw_rup > div.entry > p.partial_entry')
        date = review.find_element_by_css_selector('.ratingDate')

        parseddate = parsedate(date.get_attribute('title'))
        if checkdaterange(parseddate):
            gansevoortreview = GansevoortReview(
                date=date.get_attribute('title'),
                rating=trim_rating(rating),
                description=description.text
            )
            gansevoortreview.save()

    sleep(randint(8, 15))

connection.disconnect(db_name)
driver.close()
