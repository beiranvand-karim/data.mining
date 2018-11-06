from session import session
from gansevoortreview import GansevoortReview
from nltk.tokenize import PunktSentenceTokenizer
import nltk

review = session.query(GansevoortReview).first()
custom_sent_tokenizer = PunktSentenceTokenizer(review.review)
tokenized = custom_sent_tokenizer.tokenize(review.review)

print(review.review)


def process_content():
    tagged = []
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

        print(tagged)
    except Exception as e:
        print(str(e))


process_content()
