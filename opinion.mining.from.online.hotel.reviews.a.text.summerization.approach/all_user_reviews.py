from random import randint
from time import sleep
from crawling.trimming import trim_rating
from driver import driver
from selenium.common.exceptions import NoSuchElementException
from models.user_reviews import UserReviews, HotelsRatings


def get_user_all_reviews_and_ratings(url, profileid):

    try:
        js = 'var body = document.body,' \
             'html = document.documentElement;' \
             'var height = Math.max( body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight );' \
             'window.scrollTo(0, height);'

        at_bottom = 'function xxx() {if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) ' \
                    '{return true;} return false;} return xxx()'

        driver.get(url)
        sleep(2)

        try:
            see_more = driver.find_element_by_css_selector('.ui_button.primary.large')
            # if see_more.text:
            see_more.click()

            sleep(5)

            while True:
                condition = driver.execute_script(at_bottom)
                if condition:
                    break
                driver.execute_script(js)
                sleep(randint(5, 6))

        except NoSuchElementException:
            print("see more not found. skipping over it")

        reviews = driver.find_elements_by_css_selector('.social-sections-CardSection__card_section--20Wxe.ui_card.section')
        name = driver.find_element_by_css_selector('.social-common-MemberName__display_name--1HCDW.social-common-MemberBlock__display_name--2a02z').text
        username = driver.find_element_by_css_selector('.social-common-MemberName__user_name--2ljTA').text
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

            hotel_name = review.find_element_by_css_selector('.social-common-POIObject__poi_name--39wh4.ui_link').text

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

        _user_reviews = UserReviews(name=name, username=username, userprofileid=profileid, hotels_ratings=_hotels_ratings_list)
        _user_reviews.save()

        # driver.close()
        return True

    except Exception as e:
        print(e)
        # if driver.title:
        #     driver.close()
        return False
