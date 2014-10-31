#! /usr/bin/env python

import urllib3
from xml.dom import minidom
import json

# I'm using libraries that I prefer
# url = "http://api.trulia.com/webservices.php?library=LocationInfo&function=getCitiesInState&state=CO&apikey=[key]"

# Open and read user data config file containing key
with open('data.json') as config_file:    
    config_data = json.load(config_file)
# username = config_data["user"]
key = config_data["key"]

# set index url parts and concat
root_url = "http://api.trulia.com/webservices.php?"
trulia_library = "library=LocationInfo"
functions = "&function=getCitiesInState&state=CO"
# apikey = "&apikey=[key]"
apikey = "&apikey=" + str(key)
url = root_url + trulia_library + functions + apikey
# print(url) # test

http = urllib3.PoolManager()
r = http.request("GET", url)
# print(r.status) # test
# print(r.data) # test

dom = minidom.parseString(r.data)
dom2 = dom.getElementsByTagName("name")

# Grab node of interest
def get_element():
    for node in dom2:  # visit every node <bar />
        print node.toxml()
get_element()


