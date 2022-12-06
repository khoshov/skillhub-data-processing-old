from yarl import URL

BASE_URL = URL('https://skillhub.ru/')
TAGS_URL = BASE_URL / 'tags/'
REVIEWS_URL = BASE_URL / 'reviews/'
MATCH_MIN_SIMILARITY = 0.9
MIN_NGRAMS = 2
MAX_NGRAMS = 5
NGRAMS_NUMBER = 1000
