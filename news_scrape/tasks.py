from news_scrape.models import Comment, News
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
    ids = []
    for query in query_type:
        query_url = f"https://hacker-news.firebaseio.com/v0/{query}stories.json?print=pretty"
        r = requests.get(query_url)
        ids = ids + r.json()
    # order the list to put the biggest ids first
    ids.sort(reverse=True)
    # we only need latest 100
    items = []
    recent = ids[:100]
    # since this will run every 5 minutes
    # To ensure that the ids are not repeated
    # multiple numbers should be removed from recent,
    # and then rearranged in decreasing order
    # since the biggest id is always the latest

    for item in recent:
        items.append(
            f"https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty")
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        res = executor.map(getData, items)
    responses = list(res)

    return responses


@shared_task(name="add_news_to_db")
def add_news_to_db():
    # Scrape for Items
    story_items = scrape_news(['new', 'job'])

    # Since we dont want repetitions, we need to filter out already
    # saved news in our batch of ids, and since they are not consecutive
    # (comments uses the same base model,) I had to check against stored objects

    latest_item = News.objects.exclude(
        item_id=None).order_by('-item_id').first()
    # Get the last item from the db
    for item in story_items:
        if item:
            item_id = item.get('id')
            if hasattr(latest_item, 'item_id'):
                if item_id <= latest_item.item_id:
                    print(item_id, latest_item.item_id)
                    continue
            type = item.get('type')
            author = item.get('by')
            kids = item.get('kids')
            descendants = item.get('descendants')
            score = item.get('score')
            url = item.get('url')
            title = item.get('title')

            date_created = unix_to_datetime(item['time'])
            news_object = News.objects.create(
                item_id=item_id,
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

            # create comments
            if kids:
                for kid in kids:
                    query_url = f"https://hacker-news.firebaseio.com/v0/item/{kid}.json?print=pretty"
                    data = getData(query_url)
                    text = data.get('text')
                    parent = data.get('parent')
                    type = data.get('type')
                    author = data.get('by')
                    kids = data.get('kids')
                    date_posted = unix_to_datetime(data['time'])
                    comment_object = Comment.objects.create(
                        author=author,
                        text=text,
                        parent=parent,
                        kids=kids,
                        date_posted=date_posted,
                        type=type

                    )
                    comment_object.save()


# TODO
# def get_news_comments(news, kids):
#     news = news
#     item_id = news.item_id
#     comment_ids = kids
#     latest_item = Comment.objects.exclude(item_id=None).order_by('-item_id').first()
#     # get max comment
#     if comment_ids:
#         latest = max(comment_ids)

#         query_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json?print=pretty"
#         data = getData(query_url)
#         new_kids = data.get('kids')

#         # if there is a kid with higher id that previous latest
#         # this kid will be appended to the original comment_ids since its newer

#         for kid in new_kids:
#             if kid <= latest:
#                 pass
#             else:
#                 query_url = f"https://hacker-news.firebaseio.com/v0/item/{kid}.json?print=pretty"
#                 data = getData(query_url)
#                 text = data.get('text')
#                 parent = data.get('parent')
#                 comment_object = Comment.objects.create(
#                     news=news,
#                     text=text,
#                     parent=parent
#                 )
#                 comment_object.save()
#     else:
#         pass

add_news_to_db()
