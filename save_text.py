import requests


with open('text.txt', 'a') as f:
    next_page = 'https://skillhub.ru/reviews/'

    while next_page:
        r = requests.get(next_page)
        data = r.json()
        next_page = data.get('next')
        reviews = data.get('results', [])

        for review in reviews:
            text = review.get('text')

            if text:
                f.write(f'{text}\n')
