import requests


with open('disadvantages.txt', 'a') as f:
    next_page = 'https://skillhub.ru/reviews/'

    while next_page:
        r = requests.get(next_page)
        data = r.json()
        next_page = data.get('next')
        reviews = data.get('results', [])

        for review in reviews:
            disadvantages = review.get('disadvantages')

            if disadvantages:
                f.write(f'{disadvantages}\n')
