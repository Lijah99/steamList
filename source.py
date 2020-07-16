import json
import requests
from requests.exceptions import HTTPError
#API Key: 40C4A06852CCC51C4B062714DA4478C5

try: 
    dataFetch = requests.get(' http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=40C4A06852CCC51C4B062714DA4478C5&steamids=76561198045755215')
    dataFetch.raise_for_status()
    #access json
    fetchedJson = dataFetch.json()
    print("Entire JSON retrieval")
    print(fetchedJson)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')