##  Purpose of this script:
## To fetch hydro data from the internet, parse, and visualize it

import urllib3
import json

def main():
    """ Get the content of interest for parsing and printing """
    # open PoolManager to automatically manage connections
    http = urllib3.PoolManager()

    # open a connection to a URL using urllib3 
    weburl = http.request("GET", "http://waterdata.usgs.gov/nwis/dv?referred_module=sw&cb_00060=on&format=gif_default&site_no=06730200")

    # fetch and print status code to confirm success
    status_code = weburl.status
    print("result code: " + str(status_code))

    # now that url is open, read some data and print it 
    data = weburl.data
    print("data: \n\n") + str(data)
    

if __name__ == "__main__" :
    main()