from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint
from time import time
from IPython.core.display import clear_output


reviews = []

start_time = time()
requests = 0

pages = [i for i in range(0, 10)]

for page in pages:

    if page == 0:
        phrase = ''
    else:
        phrase = 'or' + str(page * 5)

    url = 'https://www.tripadvisor.com/Hotel_Review-g60763-d287626' \
          '-Reviews-' + phrase + '-Gansevoort_Meatpacking_NYC-New_York_City_New_York.html'

    response = get(url)
    sleep(randint(8, 15))

    requests += 1
    elapsed_time = time() - start_time
    print('Request:{}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))
    clear_output(wait=True)

    html_soup = BeautifulSoup(response.text, 'html.parser')

    review_entries = html_soup.find_all('div', class_='review-container')

    for review in review_entries:
        reviews.append(review.find('p', class_='partial_entry').text)

hotel_reviews = pd.DataFrame({'reviews': reviews})
print(hotel_reviews.info())
hotel_reviews.to_csv('hotel_reviews1-10.csv')
