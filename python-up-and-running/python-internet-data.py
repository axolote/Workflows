##  Purpose of this script:
## To fetch hydro data from the internet, parse, and visualize it

import urllib3

def main():

    # open PoolManager to automatically manage connections
    http = urllib3.PoolManager()

    # open a connection a URL using urllib3 
    weburl = http.request("GET", "http://waterdata.usgs.gov/nwis/dv?referred_module=sw&cb_00060=on&format=gif_default&site_no=06730200")

    # fetch and print status code to confirm success
    status_code = weburl.status
    print("result code: " + str(status_code))

    # now that url open, read some data and print it 
    data = weburl.data
    print(data)

    # 

if __name__ == "__main__" :
    main()