import requests, pprint, urllib
from urllib.parse import urljoin
from pprint import pprint

class VK_user:

    BASE_URL = "https://api.vk.com/method/"
   
    def __init__(self, id, token, version):
        self.id = id
        self.token = token
        self.version = version
        self.link = urljoin('http://vk.com/id', str(self.id))

    def __str__(self):
        return self.link

    def __repr__(self):
        return self.link

    def __and__(self, other):
        get_mutual_url = urljoin(self.BASE_URL, 'friends.getMutual')
        resp = requests.get(get_mutual_url, params = {
            'access_token' : self.token,
            'v' : self.version,
            'source_uid' : self.id,
            'target_uid' : other.id
        })

        return [VK_user(mutual_friend, self.token, self.version) for mutual_friend in resp.json().get('response')]


def init():
   
    TOKEN = 'XXX'
    VERSION = '5.124'
    user1 = VK_user('1145567', TOKEN, VERSION)
    user2 = VK_user('14102295', TOKEN, VERSION)
    return print(user1 & user2)

init()
