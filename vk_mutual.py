import requests, pprint, urllib
from urllib.parse import urljoin
from pprint import pprint


TOKEN = 'XXX'

class VK_API:
    BASE_URL = "https://api.vk.com/method/"

    class VK_user:
        def __init__(self, id):
            self.id = id
        def __str__(self):
            return urljoin('http://vk.com/id', str(self.id))
    
    def __init__(self, token, version):
        self.token = token
        self.version = version

    def get_mutual_friends(self, user1, user2):
        get_mutual_url = urljoin(self.BASE_URL, 'friends.getMutual')
        resp = requests.get(get_mutual_url, params = {
            'access_token' : self.token,
            'v' : self.version,
            'source_uid' : user1.id,
            'target_uid' : user2.id
        })

        mutual_friends = []
        for mutual_friend in resp.json().get('response'):
            user = self.VK_user(mutual_friend)
            mutual_friends.append(user)
            print(user)

        return mutual_friends
    




my_api = VK_API(TOKEN, '5.124')
my_api.get_mutual_friends(user1 = VK_API.VK_user('1145567'), user2 = VK_API.VK_user('14102295'))
