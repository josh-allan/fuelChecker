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

def get_NSW_Suburb_List():
    #call CheckNSW to check for single store to test logic
    suburb_list = checkNSW()
    #iterate over list using known values
    for suburb in suburb_list:
        if suburb["suburb"] == "Revesby":
            return suburb



    
pprint.pprint(get_NSW_Suburb_List())