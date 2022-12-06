import requests


with open('advantages.txt', 'a') as f:
    next_page = 'https://skillhub.ru/reviews/'

    while next_page:
        r = requests.get(next_page)
        data = r.json()
        next_page = data.get('next')
        reviews = data.get('results', [])

        for review in reviews:
            advantages = review.get('advantages')

            if advantages:
                f.write(f'{advantages}\n')
