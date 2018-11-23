import nltk
from mongoengine import connect, connection
from constants.indicatorphrases import indicatorphrases
from models.gansevoortreview import GansevoortReview
from models.reviewsentences import Sentence, ReviewSentences
from process import review_description_sentence_list

w1 = 0.3
w2 = 0.1
w3 = 0.6


def location(index):
    if index == 0:
        return 1
    return 0


def phraseindicator(sentence):
    for phrase in indicatorphrases:
        if phrase in sentence:
            return 1
    return 0


def maximalsentencenumber(sentences):
    maximum = 0
    for sentence in sentences:
        length = len(sentence.split())
        if length > maximum:
            maximum = length
    return maximum


def sentencenumber(sentence):
    return len(sentence.split())


# todo for now I am using the length of processed sentence check that later


dbname = "data-mining"
connect(dbname)
Sentence.drop_collection()

for review in GansevoortReview.objects[:1]:
    custom_sent_tokenizer = nltk.PunktSentenceTokenizer(review.description)
    sentences = custom_sent_tokenizer.tokenize(review.description)
    sent_list = review_description_sentence_list(sentences)
    maximal = maximalsentencenumber(sent_list)
    print(maximal)

    sentencelist = []
    for sen in sent_list:
        sen_length = sentencenumber(sen)
        score = sen_length / maximal
        sentence = Sentence(
            value=sen,
            score=score
        )
        sentence.save()
        sentencelist.append(sen)

    reviewsentences = ReviewSentences(
        reviewId=review.id,
        sentences=sentencelist
    )
    reviewsentences.save()

    sentencelist.clear()

for rev in ReviewSentences.objects(sentences__in=["5bf7f92d66fc14522adeb351", "5bf7f92d66fc14522adeb352"]):
    print(len(rev))
connection.disconnect(dbname)
