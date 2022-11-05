""" Crawl the italki API to get all Russian teachers. """

import requests
import json

def get_page(page=1):

    payload = {
        "teach_language": {
            "language": "russian",
        },
        "page": page,
        "page_size": 20,
        "user_timezone": "Asia/Shanghai",
    }
    url = 'https://api.italki.com/api/v2/teachers'
    headers = {
        'authority': 'api.italki.com',
        'accept-language': 'en-us',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'content-type': 'application/json',
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://www.italki.com',
        'referer': 'https://www.italki.com/',
    }
    response = requests.post(url, json=payload, headers=headers)
    response = response.json()
    return response

def has_next(data):

    return bool(data.get('paging').get('has_next'))


if __name__ == "__main__":
    page = 1
    while True:
        print(f'Fetching page {page}')

        data = get_page(page)

        with open(f'pages/page_{page}.json', 'w') as outfile:
            json.dump(data, outfile)

        if not has_next(data):
            break

        page += 1
