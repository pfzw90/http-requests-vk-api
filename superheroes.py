import requests

namesearch_url = "https://superheroapi.com/api/2619421814940190/search/"
superheroes = [{'name' : 'Hulk'}, {'name' : 'Captain America'}, {'name' : 'Thanos'}]

for hero in superheroes:
    hero_r = requests.get(namesearch_url + hero['name'])
    hero['intelligence'] = int(hero_r.json()['results'][0]['powerstats']['intelligence'])
    
print(sorted(superheroes, key=lambda hero: -hero['intelligence'])[0]['name'])
