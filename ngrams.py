from collections import Counter

import spacy
from textacy.extract import basics

from constants import MAX_NGRAMS, MIN_NGRAMS

REVIEWS_TYPE = 'disadvantages'

nlp = spacy.load("ru_core_news_lg")
nlp.max_length = 10_000_000

with open(f'{REVIEWS_TYPE}.txt') as f:
    text = f.read()
    doc = nlp(text)

if __name__ == '__main__':
    for n in range(MIN_NGRAMS, MAX_NGRAMS + 1):
        results = []
        ngrams = list(basics.ngrams(doc, n=n))
        results.extend([str(ngram).lower() for ngram in ngrams])

        with open(f'{REVIEWS_TYPE}_ngrams_{n}.txt', 'a') as f:
            for line in Counter(results).most_common(1000):
                f.write(f'{line}\n')
