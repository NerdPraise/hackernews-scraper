import requests
from concurrent import futures


def getData(url):
    res = requests.get(url)
    return res.json()


def scrape_news(query_type):
    '''
    Scrape news of different query_types
    '''

    # Newest Stories
    query_url = f"https://hacker-news.firebaseio.com/v0/{query_type}stories.json?print=pretty"
    r = requests.get(query_url)
    ids = r.json()

    # we only need latest 100
    items = []
    recent = ids[:100]
    for item in recent:
        items.append(
            f"https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty")
    with futures.ThreadPoolExecutor(max_workers=8) as executor:
        res = executor.map(getData, items)
    responses = list(res)

    return responses

def add_to_db():
    pass
print(scrape_news('job'))
