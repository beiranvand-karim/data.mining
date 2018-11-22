import re


def trim_ratings(ratings):
    new_ratings = []
    for r in ratings:
        rate = re.findall(r'\d+', r.get_attribute('class'))[0]
        pure_rate = float(rate)/10
        new_ratings.append(pure_rate)

    return new_ratings


def trim_rating(rating):
    if rating is not None:
        rate = re.findall(r'\d+', rating.get_attribute('class'))[0]
        pure_rate = float(rate) / 10
        return pure_rate
    else:
        return None


def make_url(index):
    if index == 0:
        phrase = ''
    else:
        phrase = 'or' + str(index * 5)

    url = 'https://www.tripadvisor.com/Hotel_Review-g60763-d287626' \
          '-Reviews-' + phrase + '-Gansevoort_Meatpacking_NYC-New_York_City_New_York.html'
    return url
