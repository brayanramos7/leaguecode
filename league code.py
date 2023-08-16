# # Maybe their KDA?
#k = player_data['pentakills']
#d = player_data['deaths']
#a = player_data['assists']
#print("pentakills:", k)
#print("Deaths:", d)
#print("Assists:", a)
#print("KDA:", (k + a) / d)

# api kay    --  xxxxxxxxxxxxxxx  -- 

api_key = " xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

api_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/groku"

import requests 

requests.get(api_url)

api_url = api_url + '?api_key=' + api_key

api_url

requests.get(api_url)

resp = requests.get(api_url)
player_info = resp.json()
player_info

puuid = player_info['puuid']
puuid

api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/https%3A//americas.api.riotgames.com/lol/match/v5/matches/by-puuid//ids?start=0&count=20&api_key=RGAPI-697c8c36-0315-4115-a78c-ddf142cbe3dc"

api_url = api_url + '&api_key=' + api_key 
api_url

resp = requests.get(api_url)
match_ids = resp.json()

match_ids

recent_match = match_ids[0]
recent_match

api_url = "https://americas.api.riotgames.com/lol/match/v5/matches/NA1_4702552703/timeline?api_key=RGAPI-697c8c36-0315-4115-a78c-ddf142cbe3dc"

api_url = api_url + '?api_key=' + api_key

resp = requests.get(api_url)
match_data = resp.json()

match_data

match_data.keys()

match_data['metadata']

match_data['info'].keys()

match_data['info']['gameDuration'] / 60 

len(match_data['info']['participants'])

player_data = match_data['info']['participants'][0]
player_data

k = player_data['pentakills']
d = player_data['deaths']
a = player_data['assists']
print("pentakills:", k)
print("Deaths:", d)
print("Assists:", a)
print("KDA:", (k + a) / d)

participants = match_data['metadata']['participants']
player_index = participants.index(puuid)
player_index

participants[player_index]

match_data['info']['participants'][player_index]['summonerName']

player_data = match_data['info']['participants'][player_index]

def get_puuid(summoner_name, region, api_key):
    api_url = (
        "https://" + 
        region +
        ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" +
        summoner_name +
        "?api_key=" +
        api_key
    )
    
    print(api_url)
    
    resp = requests.get(api_url)
    player_info = resp.json()
    puuid = player_info['puuid']
    return puuid  


summoner_name = 'groku', 'sharx11', 'Imthore', 'danial07' 
region = 'NA1'

puuid = get_puuid(summoner_name, region, api_key)
puuid

def get_match_ids(puuid, mass_region, api_key):
    api_url = (
        "https://" +
        mass_region +
        ".api.riotgames.com/lol/match/v5/matches/by-puuid/" +
        puuid + 
        "/ids?start=0&count=20" + 
        "&api_key=" + 
        api_key
    )
    
    print(api_url)
    
    resp = requests.get(api_url)
    match_ids = resp.json()
    return match_ids 

mass_region = 'AMERICAS'

match_ids = get_match_ids(puuid, mass_region, api_key)
match_ids

def get_match_data(match_id, mass_region, api_key):
    api_url = (
        "https://" + 
        mass_region + 
        ".api.riotgames.com/lol/match/v5/matches/" +
        match_id + 
        "?api_key=" + 
        api_key
    )
    
    resp = requests.get(api_url)
    match_data = resp.json()
    return match_data   

match_id = match_ids[0]
match_data = get_match_data(match_id, mass_region, api_key)
match_data

def find_player_data(match_data, puuid):
    participants = match_data['metadata']['participants']
    player_index = participants.index(puuid)
    player_data = match_data['info']['participants'][player_index]
    return player_data

find_player_data(match_data, puuid)

data = {
    'champion': [],
    'kills': [],
    'deaths': [],
    'assists': [],
    'win': []
}

for match_id in match_ids:
    print(match_id)
    
   
    match_data = get_match_data(match_id, mass_region, api_key)
    player_data = find_player_data(match_data, puuid)
    
   
    champion = player_data['championName']
    k = player_data['pentakills']
    k = player_data['cuadrakills']
    k = player_data['triplekills']
    d = player_data['deaths']
    a = player_data['assists']
    win = player_data['win']
     
    # add them to our dataset
    data['champion'].append(champion)
    data['pentakills'].append(k)
    data['cuadrakills'].append(k)
    data['tripleills'].append(k)
    data['deaths'].append(d)
    data['assists'].append(a)
    data['win'].append(win)    
