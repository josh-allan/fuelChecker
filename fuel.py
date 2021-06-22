import json
import urllib3
import pprint

<<<<<<< HEAD
def check_NSW():
=======
def checkNSW():
>>>>>>> cb733ef31d7e9962a2c9b12a915eb7a165fa0606
    #poll the API and collect results for the states
    
    url = 'https://projectzerothree.info/api.php?format=json'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    fuel = json.loads(r.data)
    NSW = 2
    return fuel["regions"][NSW]["prices"]

def get_NSW_Suburb_List():
    #call CheckNSW to check for single store to test logic
<<<<<<< HEAD
    suburb_list = check_NSW()
    #iterate over list using known values
    if suburb_list == ["Revesby"] or ["Mayfield"] or ["Lurnea"]:
        return suburb_list
        
def get_Store_Prices():
    store_prices = get_NSW_Suburb_List()
    for store in store_prices:
        print(store["price"])
    
print(get_NSW_Suburb_List(), get_Store_Prices())
=======
    suburb_list = checkNSW()
    #iterate over list using known values
    for suburb in suburb_list:
        if suburb["suburb"] == "Revesby":
            return suburb



    
pprint.pprint(get_NSW_Suburb_List())
>>>>>>> cb733ef31d7e9962a2c9b12a915eb7a165fa0606
