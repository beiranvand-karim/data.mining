from selenium import webdriver
from time import sleep
from random import randint
from time import time
from IPython.core.display import clear_output
from session import session
from review import Review

# https://www.tripadvisor.com/Hotel_Review-g60763-d287626-Reviews-or5-Gansevoort_Meatpacking_NYC-New_York_City_New_York.html

start_time = time()
requests = 0

driver = webdriver.Chrome()

for i in range(0, 10):
    if i == 0:
        phrase = ''
    else:
        phrase = 'or' + str(i * 5)

    url = 'https://www.tripadvisor.com/Hotel_Review-g60763-d287626' \
          '-Reviews-' + phrase + '-Gansevoort_Meatpacking_NYC-New_York_City_New_York.html'

    driver.get(url)
    link = driver.find_element_by_class_name('ulBlueLinks')
    link.click()
    sleep(randint(8, 15))

    reviews = driver.find_elements_by_css_selector('div.ui_column.is-9 > div.prw_rup > div.entry > p.partial_entry')
    dates = driver.find_elements_by_class_name('ratingDate')
    for j in range(0, len(reviews)):
        rev = Review(id=str(i * 10 + j), date=dates[j].get_attribute('title'), review=reviews[j].text)
        session.add(rev)
        session.commit()

    sleep(randint(8, 15))

    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))
    clear_output(wait=True)

driver.close()
session.close()

