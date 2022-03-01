import requests
from celery import shared_task
from .models import News

# RUN TASKS WITH 'celery -A hackernews worker -l info' AND 'celery -A hackernews beat -l info'

@shared_task(name = "seed_db_task")
def seedDBTask():
    # Create the HttpResponse object with the appropriate CSV header.

    url2 = "https://hacker-news.firebaseio.com/v0/newstories.json"
    response2 = requests.get(url2)
    list_from_api = response2.json()
    

    # GET MOST RECENT 20 IDs
    sort_list_from_api = sorted(list_from_api)
    numb_list = sort_list_from_api[-20:]            # DETERMINE NUMBER OF IDS TO BE SEEDED

    for x in numb_list:
        url_news = "https://hacker-news.firebaseio.com/v0/item/{}.json?.json".format(x)
        response = requests.get(url_news)
        # news_items = response2.json()
        news = News(
        
        type = response.json().get('type'), title = response.json().get('title'), hacker_id = response.json().get('id'), creator = response.json().get('by'),
        score = response.json().get('score'), descendants = response.json().get('descendants'), url = response.json().get('url')
        )
        news.save()
        


# BELOW RUNS EVERY 5 MINUTES. RUN TASKS WITH 'celery -A hackernews beat -l info' IN A NEW TERMINAL

@shared_task(name = "sync_db_task")
def syncTheDB():

    # SYNC MY DATABASE ONLY IF THERE ARE OBJECTS THEREIN (TO MAKE SURE MY DB IS ALREADY SEEDED BEFORE ANY SYNCING IS INITIATED)

    if News.objects.exists():

        # GET MAX ID IN MY DB
        db = News.objects.all()
        id = [x.hacker_id for x in db ]
        max_id = max(id)
        print(max_id)

        # TO SEED THE DATABASE

        url2 = "https://hacker-news.firebaseio.com/v0/newstories.json"
        response2 = requests.get(url2)
        
        numb_list = response2.json()

        for x in numb_list:
            if x > max_id:

                url_news = "https://hacker-news.firebaseio.com/v0/item/{}.json?.json".format(x)
                response = requests.get(url_news)
                
                
                news = News(
                type = response.json().get('type'), title = response.json().get('title'), hacker_id = response.json().get('id'), creator = response.json().get('by'),
                score = response.json().get('score'), descendants = response.json().get('descendants'), url = response.json().get('url')
                )
                
                news.save()
    else:
        pass
