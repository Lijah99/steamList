import json
import requests
from requests.exceptions import HTTPError
#API Key: 40C4A06852CCC51C4B062714DA4478C5
#joey - 76561198045755215
#me - 76561198031865653

try: 
    dataFetch = requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=40C4A06852CCC51C4B062714DA4478C5&steamids=76561198045755215')
    dataFetch.raise_for_status()
    
    #access json for user summary
    fetchedJson = json.dumps(json.loads(dataFetch.content), indent=2)
    diction = json.loads(fetchedJson)
    userName = diction['response']['players'][0]['personaname']
    userId = diction['response']['players'][0]['steamid']
    print("Entire JSON retrieval for " + userName)
    print(fetchedJson)

    #access json for user owned games
    dataFetch = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=40C4A06852CCC51C4B062714DA4478C5&include_played_free_games=1&include_appinfo=1&format=json&steamid=' + userId)
    fetchedJson = json.dumps(json.loads(dataFetch.content), indent=2)
    print("Entire JSON retrieval for " + userName + "'s games")
    print(fetchedJson)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')