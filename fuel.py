import json
import urllib3
import pprint

def check_NSW():
    #poll the API and collect results for the states
    
    url = 'https://projectzerothree.info/api.php?format=json'
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    fuel = json.loads(r.data)
    NSW = fuel["regions"]["prices"]
    for state in NSW:
        if state["region"] == "NSW":
            return state    

    # return fuel["regions"][NSW]["prices"]

def get_NSW_Suburb_List():
    #call CheckNSW to check for single store to test logic
    suburb_list = check_NSW()
    #iterate over list using known values
    if suburb_list == ["Revesby"] or ["Mayfield"] or ["Lurnea"]:
        return suburb_list
        
def get_Store_Prices():
    store_prices = get_NSW_Suburb_List()
    for store in store_prices:
        print(store["price"])
    
# print(get_NSW_Suburb_List(), get_Store_Prices())
print(get_Store_Prices())
