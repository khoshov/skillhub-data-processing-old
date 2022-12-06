import requests
from dostoevsky.models import FastTextSocialNetworkModel
from dostoevsky.tokenization import RegexTokenizer
from loguru import logger

from constants import REVIEWS_URL

UNKNOWN = 1
NEGATIVE = 2
NEUTRAL = 3
POSITIVE = 4

sentiments = {
    'positive': POSITIVE,
    'negative': NEGATIVE,
}

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

next_page = REVIEWS_URL % {'text_sentiment': UNKNOWN}

while next_page:
    r = requests.get(next_page)
    data = r.json()
    next_page = data.get('next')
    reviews = data.get('results', [])

    for review in reviews:
        text = review.get('text')
        id_ = review.get('id')
        result = list(model.predict([text], k=1)[0].keys())[0]

        if result in sentiments:
            text_sentiment = sentiments[result]
            url = REVIEWS_URL / id_
            try:
                requests.patch(url, data={'text_sentiment': text_sentiment})
                logger.info(f'Successfully updated review #{id_} sentiment to {result}')
            except requests.exceptions.RequestException as e:
                logger.error(f'Error during request to {url}. {e}')
