import json
import urllib3
import pprint

def checkNSW():
    #poll the API and collect results for the states
    
    url = 'https://projectzerothree.info/api.php?format=json'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    fuel = json.loads(r.data)
    NSW = 2
    return fuel["regions"][NSW]["prices"]

def suburb():
    #call CheckNSW to check for single store to test logic
    suburb = checkNSW()
    #iterate over list using known values
    for i in suburb:
        if i["suburb"] == "Revesby":
            return i
        

pprint.pprint(suburb())