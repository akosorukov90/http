import requests

TOKEN = ''


def most_intelligence(list_name):
    most_intelligence = 0
    most_intelligence_name = ''
    for name in list_name:
        response = requests.get("https://superheroapi.com/api/" + TOKEN + "/search/" + name)
        intelligence = response.json()['results'][0]['powerstats']['intelligence']
        if int(intelligence) > most_intelligence:
            most_intelligence = int(intelligence)
            most_intelligence_name = name
    print(f'Самый умный: {most_intelligence_name}')


name_super = ['Hulk', 'Captain America', 'Thanos']
most_intelligence(name_super)