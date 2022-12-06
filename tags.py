import requests
import spacy
from textacy.extract import basics
from loguru import logger
from constants import MATCH_MIN_SIMILARITY, REVIEWS_URL, TAGS_URL

nlp = spacy.load("ru_core_news_lg")


def get_tags():
    result = {}
    next_page = TAGS_URL
    while next_page:
        r = requests.get(next_page)
        data = r.json()
        next_page = data.get('next')
        tags = data.get('results', [])

        for tag in tags:
            name = tag.get('name')
            options = tag.get('options')
            result[name] = []

            for option in options:
                text = option.get('text')
                result[name].append(text)

    return result


def process_reviews(tags):
    next_page = REVIEWS_URL

    while next_page:
        r = requests.get(next_page)
        data = r.json()
        next_page = data.get('next')
        reviews = data.get('results', [])

        for review in reviews:
            text = review.get('disadvantages')
            id_ = review.get('id')

            for n in range(1, 2):
                if not text:
                    break

                text = nlp(text)
                ngrams = list(basics.ngrams(text, n=n))

                for ngram in ngrams:
                    for tag, options in tags.items():
                        for option in options:
                            option = nlp(option)
                            similarity = ngram.similarity(option)
                            if similarity > MATCH_MIN_SIMILARITY:
                                logger.info(f'{ngram} is similar to {option}')


def main():
    tags = get_tags()
    process_reviews(tags)


if __name__ == '__main__':
    main()
