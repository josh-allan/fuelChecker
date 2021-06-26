import json
import urllib3
import pprint

def check_NSW():
    #poll the API and collect results for the states
    
    url = 'https://projectzerothree.info/api.php?format=json'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    fuel = json.loads(r.data)
    for region in fuel["regions"]:
        if region["region"] == "NSW":
            return region


def get_NSW_suburb_list():
    #call CheckNSW to check for single store to test logic
    suburb_list = check_NSW()
    #iterate over list using known values
    # if suburb_list == ["Revesby"] or ["Mayfield"] or ["Lurnea"]:
    #     return suburb_list
    for suburb in suburb_list:
        return suburb
        
def get_store_prices():
    
    store_prices = get_NSW_suburb_list()
    for store in store_prices["prices"]:
        print(store["price"])

get_store_prices()