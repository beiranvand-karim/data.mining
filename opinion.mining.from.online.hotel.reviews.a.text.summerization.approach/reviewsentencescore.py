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


def nw(length, maximum):
    return length / maximum


def reviewsentencescore(_loc, _nw, _ip):
    return w1 * _loc + w2 * _nw + w3 * _ip

# todo for now I am using the length of processed sentence check that later


dbname = "data-mining"
connect(dbname)
ReviewSentences.drop_collection()

for review in GansevoortReview.objects:
    custom_sent_tokenizer = nltk.PunktSentenceTokenizer(review.description)
    sentences = custom_sent_tokenizer.tokenize(review.description)
    sent_list = review_description_sentence_list(sentences)
    maximal = maximalsentencenumber(sent_list)

    sentencelist = []
    for index, sen in enumerate(sent_list):
        sen_length = sentencenumber(sen)

        loc_ = location(index)
        nw_ = nw(sen_length, maximal)
        ip_ = phraseindicator(sen)

        css = reviewsentencescore(loc_, nw_, ip_)

        sentence = Sentence(
            value=sen,
            score=css
        )
        sentencelist.append(sentence)

    reviewsentences = ReviewSentences(
        reviewId=review.id,
        sentences=sentencelist,
        maximal=maximal
    )
    reviewsentences.save()

    sentencelist.clear()

connection.disconnect(dbname)
