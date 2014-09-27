# Purpose of this script:
# To fetch hydro data from the internet, parse, and visualize it

import urllib3
import json


def printResults(data):
    """ Use the json module to load the string data into a dictionary """
    theJSON = json.loads(data)
#     print(theJSON)

    # access contents of json object
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    else: 
        print("That element does not exist")
    
    # output number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print str(count) + " events recorded"
    
    # for each event, print the place where it occurred
    # inside the features array in the json data, print the place property which is within the properties collection
    for i in theJSON["features"]:
        print i["properties"]["place"]
    # print mag and place for earthquakes with mags >= 4.0
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            # string formatting meaning print 2 digits and 1 decimal place of a floating point number
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"]
#           print("{}, {}").format(i["properties"]["mag"], i["properties"]["place"])

    # print events where at least one person reported feeling the earthquake
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None) & (feltReports > 0):
           print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], "reported", str(feltReports), "times." 
    
    # print events where Colorado is in the place name
    for i in theJSON["features"]:
        place = i["properties"]["place"]
        if "Alaska" in place:
            print "\n %2.1f" % i["properties"]["mag"], "earthquake reported", i["properties"]["place"]
        
   
def main():
    """ Get the content of interest for parsing and printing """
    # open PoolManager to manage connections
    http = urllib3.PoolManager()

    # set url to json or geojson
    # for geojson output description, see http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    print(url)
    
    # open a connection to the json or geojson URL using urllib3
    weburl = http.request("GET", url)
    # print(weburl)
    
    # fetch and print status code to confirm success
    status_code = weburl.status
    print("result code: " + str(status_code))
 
    # now that url open, read some data and print it 
    # if status code indicates success, print the data. Otherwise, print error message.
    data = str(weburl.data)
    if (status_code == 200):
#         print("data: \n\n") + data
        printResults(data)  # note the printResults function called here exists outside of main()
    else:
        print("Received an error from server. Can't print results.")



if __name__ == "__main__" :
    main()

