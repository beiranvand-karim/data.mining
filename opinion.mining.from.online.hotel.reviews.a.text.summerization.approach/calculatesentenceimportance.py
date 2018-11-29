import nltk
from mongoengine import connect, connection, DoesNotExist, MultipleObjectsReturned
from models.gansevoortreview import GansevoortReview
from models.reviewauthorrepresentativeness import ReviewAuthorRepresentativeness
from models.reviewhelpfulness import ReviewHelpfulness
from models.reviewrecency import ReviewRecency
from models.reviewsentences import ReviewSentences, Sentence
from models.user_reviews import UserReviews
from process import review_description_sentence_list
from reviewsentencescore import maximalsentencenumber, sentencenumber, location, nw, phraseindicator, \
    reviewsentencescore


def sentenceimportance(ch, cr, rca):
    return (ch + cr + rca) / 3


dbname = "data-mining"
connect(dbname)
ReviewSentences.drop_collection()
Sentence.drop_collection()

for index, rev in enumerate(GansevoortReview.objects):

    custom_sent_tokenizer = nltk.PunktSentenceTokenizer(rev.description)
    sentences = custom_sent_tokenizer.tokenize(rev.description)
    sent_list = review_description_sentence_list(sentences)
    maximal = maximalsentencenumber(sent_list)

    CH = ReviewHelpfulness.objects.get(reviewId=rev.id).value
    CR = ReviewRecency.objects.get(reviewId=rev.id).value

    try:
        JOIN = UserReviews.objects.get(name=rev.name).id
        RCA = ReviewAuthorRepresentativeness.objects.get(authorId=JOIN).value
    except DoesNotExist:
        RCA = None
    except MultipleObjectsReturned:
        RCA = None
        print(f"two items were returned")

    scorecoefficient = None
    if CH and CR and RCA:
        scorecoefficient = sentenceimportance(CH, CR, RCA)

    sentencelist = []
    for index, sen in enumerate(sent_list):
        sen_length = sentencenumber(sen)

        loc_ = location(index)
        nw_ = nw(sen_length, maximal)
        ip_ = phraseindicator(sen)

        css = reviewsentencescore(loc_, nw_, ip_)

        importance = None
        if scorecoefficient:
            importance = scorecoefficient * css

        sentence = Sentence(
            value=sen,
            score=css,
            importance=importance
        )
        sentence.save()
        sentencelist.append(sentence)

    reviewsentences = ReviewSentences(
        reviewId=rev.id,
        sentences=sentencelist,
        maximal=maximal,
        scorecoefficient=scorecoefficient
    )
    reviewsentences.save()

    sentencelist.clear()


connection.disconnect(dbname)
