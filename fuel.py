import json
import urllib3
import pprint

def checkState():
    #poll the API and collect results for the states
    
    url = 'https://projectzerothree.info/api.php?format=json'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    fuel = json.loads(r.data)
    NSW = 2
    return fuel["regions"][NSW]["prices"]


# def checkPrice():
#     location = checkNSW()
#     price = location
#     return price

pprint.pprint(checkState())