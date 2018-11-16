from random import randint
from time import sleep
from crawling.trimming import trim_rating
from driver import driver
from selenium.common.exceptions import NoSuchElementException
from models.user_reviews import UserReviews, HotelsRatings
import mongoengine as me


try:
    url = 'https://www.tripadvisor.com/Profile/' \
          'rethot?fid=fc096feb-9bc1-4b8c-8186-46de8a3770f6'

    js = 'var body = document.body,' \
         'html = document.documentElement;' \
         'var height = Math.max( body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight );' \
         'window.scrollTo(0, height);'

    at_bottom = 'function xxx() {if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) ' \
                '{return true;} return false;} return xxx()'

    me.connect("user-all-reviews")
    UserReviews.drop_collection()

    driver.get(url)
    sleep(2)

    see_more = driver.find_element_by_css_selector('.ui_icon.single-chevron-down.ShowMore__icon--25Enx')
    # if see_more.text:
    see_more.click()

    sleep(5)

    while True:
        condition = driver.execute_script(at_bottom)
        if condition:
            break
        driver.execute_script(js)
        sleep(randint(5, 6))

    reviews = driver.find_elements_by_css_selector('.CardSection__card_section--2FTVG.ui_card.section')
    name = driver.find_element_by_css_selector('.MemberName__display_name--2IbHU.MemberBlock__display_name--30eg_').text
    username = driver.find_element_by_css_selector('.MemberName__user_name--1WqHX').text
    print(name)
    print(username)

    print(reviews.__len__())

    _hotels_ratings_list = []

    for review in reviews:

        try:
            ele = review.find_element_by_css_selector('.ui_bubble_rating')
            user_given_rating = trim_rating(ele)

        except NoSuchElementException:
            user_given_rating = -1

        hotel_name = review.find_element_by_css_selector('.POIObject__poi_name--2ulYO.ui_link').text

        try:
            ele = review.find_element_by_css_selector('.ui_poi_review_rating > .ui_bubble_rating')
            over_all_rating = trim_rating(ele)

        except NoSuchElementException:
            over_all_rating = -1

        _hotels_ratings = HotelsRatings(
            user_given_rating=user_given_rating,
            over_all_rating=over_all_rating,
            name=hotel_name
        ).save()
        _hotels_ratings_list.append(_hotels_ratings)

    _user_reviews = UserReviews(name=name, username=username, hotels_ratings=_hotels_ratings_list)
    _user_reviews.save()

    driver.close()


except Exception as e:
    print(e)
    if driver.title:
        driver.close()
