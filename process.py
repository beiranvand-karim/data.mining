import nltk
from nltk.corpus import stopwords
from mongo_gansevoort_reviews import MongoGansevoortReview
import mongoengine as me

stop_words = stopwords.words("english")


def process_sentence(description):
    words = nltk.word_tokenize(description)
    tagged = nltk.pos_tag(words)
    tag_filters = ['NN', 'JJ']

    filter_sentence = []

    for t in tagged:
        if t[0] not in stop_words and t[1] in tag_filters:
            filter_sentence.append(t[0])

    concatenated_sentence = ' '.join(filter_sentence)
    return concatenated_sentence


def tagger(sentence):
    return sentence


def remove_stop_words(sentence):
    return sentence


def filter_pos_tags(sentence):
    return sentence


def review_description_sentence_list(sentences):
    sent_list = []
    for sen in sentences:
        sent_list.append(process_sentence(sen))
    return sent_list


def process_al_reviews(reviews):
    me.connect("data-mining")
    for review in reviews:
        custom_sent_tokenizer = nltk.PunktSentenceTokenizer(review.review)
        sentences = custom_sent_tokenizer.tokenize(review.review)
        sent_list = review_description_sentence_list(sentences)

        item = MongoGansevoortReview(corresponding_id=review.id,
                                     paragraph=sent_list,
                                     description=review.review,
                                     date=review.date)
        item.save()
