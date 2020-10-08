import datetime
import requests
import time


def get_questions():
        last_2day = datetime.datetime.now() - datetime.timedelta(days=2)
        now = datetime.datetime.now()
        unixtime_last_2day = time.mktime(last_2day.timetuple())
        unixtime_now = time.mktime(now.timetuple())

        response = requests.get(
                "https://api.stackexchange.com/2.2/questions",
                params={"fromdate": int(unixtime_last_2day), "todate": int(unixtime_now), "order": "desc", "sort": "creation",
                        "tagged": "python", "site": "stackoverflow"},
        )
        count = len(response.json()['items'])
        print(f'Количество вопросов на странице: {count}\n')
        for question in response.json()['items']:
                print(question['link'])
                print(question['title'])
                print()


get_questions()