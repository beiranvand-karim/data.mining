from session import session
from gansevoortreview import GansevoortReview
from nltk.tokenize import PunktSentenceTokenizer
import nltk

review = session.query(GansevoortReview).first()
custom_sent_tokenizer = PunktSentenceTokenizer(review.review)
tokenized = custom_sent_tokenizer.tokenize(review.review)

print(review.review)
print(tokenized[0])

words = nltk.word_tokenize(tokenized[0])
tagged = nltk.pos_tag(words)
print(str(tagged))

# def process_content():
#     try:
#         for i in tokenized:
#             words = nltk.word_tokenize(i)
#             tagged = nltk.pos_tag(words)
#             print(tagged)
#
#     except Exception as e:
#         print(str(e))


# process_content()
