from news_scrape.models import News
from news_scrape.utils import unix_to_datetime
import requests
from concurrent import futures
from celery import shared_task


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
    # since this will run every 5 minutes
    # To ensure that the ids are not repeated
    # multiple numbers should be removed from recent,
    # and then rearranged in decreasing order
    # since the biggest id is always the latest

    # 
    for item in recent:
        items.append(
            f"https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty")
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        res = executor.map(getData, items)
    responses = list(res)

    return responses


@shared_task(name="add_news_to_db")
def add_to_db():
    # For story items
    story_items = scrape_news('new')
    print(story_items)
    
    for item in story_items:
        type = item.get('type')
        author = item.get('by')
        kids = item.get('kids')
        descendants = item.get('descendants')
        score = item.get('score')
        url = item.get('url')
        title = item.get('title')

        date_created = unix_to_datetime(item['time'])
        news_object = News.objects.create(
            type=type,
            author=author,
            date_created=date_created,
            kids=kids,
            descendants=descendants,
            score=score,
            url=url,
            title=title

        )

    # For jobs items
    job_items = scrape_news('job')
    for item in job_items:
        type = item.get('type')
        author = item.get('by')
        kids = item.get('kids')
        descendants = item.get('descendants')
        score = item.get('score')
        url = item.get('url')
        title = item.get('title')

        date_created = unix_to_datetime(item['time'])
        news_object = News.objects.create(
            type=type,
            author=author,
            date_created=date_created,
            kids=kids,
            descendants=descendants,
            score=score,
            url=url,
            title=title

        )
    news_object.save()
add_to_db()
