import nltk
from nltk.corpus import stopwords
from models.mongo_gansevoort_reviews import MongoGansevoortReview
import mongoengine as me


def removetags(sentence):
    filtered_sentence = list(map(lambda item: item[0], sentence))
    return filtered_sentence


def buildsentence(wordlist):
    concatenated_sentence = ' '.join(wordlist)
    return concatenated_sentence


def process_sentence(description):
    tagged_sentence = tagger(description)
    filtered_sentence = remove_stop_words(tagged_sentence)
    filtered_sentence = filter_pos_tags(filtered_sentence)
    filtered_sentence = removetags(filtered_sentence)
    concatenated_sentence = buildsentence(filtered_sentence)
    return concatenated_sentence


def tagger(sentence):
    words = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(words)
    return tagged


def remove_stop_words(tagged_sentence):
    stop_words = stopwords.words("english")
    filtered_tagged_sentence = []
    for item in tagged_sentence:
        if item[0] not in stop_words:
            filtered_tagged_sentence.append(item)
    return filtered_tagged_sentence


def filter_pos_tags(tagged_sentence):
    tag_filters = ['NN', 'JJ']
    filtered_tagged_sentence = []
    for item in tagged_sentence:
        if item[1] in tag_filters:
            filtered_tagged_sentence.append(item)
    return filtered_tagged_sentence


def review_description_sentence_list(sentences):
    sent_list = []
    for sen in sentences:
        sent_list.append(process_sentence(sen))
    return sent_list


def process_all_reviews(reviews):
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
