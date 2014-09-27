#  Purpose of this script:
# To fetch hydro data from the internet, parse, and visualize it

import urllib3
import json
import datetime

def printResults(data):
    """ Use the json module to load the string data into a dictionary """
    
    theJSON = json.loads(data)
    #print(theJSON)
    
    # access contents of json object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    else: 
        print("That element does not exist")

def main():
     """ Get the content of interest for parsing and printing """
     
    #date checks
    now = datetime.datetime.now()
    print("Our current date and time is ") + str(datetime.datetime.now())
    print(now.strftime("%Y%m%d"))
    
    # open PoolManager to manage connections
    http = urllib3.PoolManager()

    # set url to json or geojson
    # note, i need to figure out how to make a 7d date object in %Y%m%d format
#     url = "http://waterdata.usgs.gov/nwis/dv/?dd_cd=04_00060_00003&format=img_stats&site_no=06730200&begin_date=" + now.strftime("%Y%m%d") + "&end_date=" + now.strftime("%Y%m%d")
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_day.geojson"
    print(url)
    
    # open a connection to the json or geojson URL using urllib3
    weburl = http.request("GET", url)
#     print(weburl)
    
    # fetch and print status code to confirm success
    status_code = weburl.status
    print("result code: " + str(status_code))
 
    # now that url open, read some data and print it 
    # if status code indicates success, print the data. Otherwise, print error message.
    data = weburl.data
    if (status_code == 200):
        print("data: \n\n") + str(data)
    else:
        print("Received an error from server. Can't print results.")



if __name__ == "__main__" :
    main()