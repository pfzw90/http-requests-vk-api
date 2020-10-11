import requests, datetime, pprint
from datetime import timedelta
from datetime import datetime
from pprint import pprint



def get_questions(days, tag):
  
    end_date = int((datetime.now() - datetime(1970, 1, 1)) / timedelta(seconds=1))
    start_date = int((datetime.now() - timedelta(days = days) - datetime(1970, 1, 1)) / timedelta(seconds=1)) 
    
    PARAMS = {
        'fromdate' : start_date,
        'todate' : end_date,
        'tagged' : tag,
        'site' : 'stackoverflow'
    }
    
    resp = requests.get('https://api.stackexchange.com/2.2/questions', params = PARAMS)
   
    for question in resp.json()['items']:
        print(('Question: ' + question['title']).upper())
        print('Tags: ' + str(question['tags']))
        print('-------------------------')

get_questions(4, 'python')