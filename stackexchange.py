import requests, datetime, pprint
from datetime import timedelta
from datetime import datetime
from pprint import pprint



def get_questions(days, tag):
  
    end_date = int(datetime.timestamp(datetime.now()))
    start_date = end_date - days * 86400 
    
    PARAMS = {
        'fromdate' : start_date,
        'todate' : end_date,
        'tagged' : tag,
        'site' : 'stackoverflow'
    }
    
    resp = requests.get('https://api.stackexchange.com/2.2/questions', params = PARAMS)
    pprint(resp)   
    for question in resp.json().get('items'):
        print(('Question: ' + question['title']).upper())
        print('Tags: ' + str(question['tags']))
        print('-------------------------')

get_questions(4, 'python')