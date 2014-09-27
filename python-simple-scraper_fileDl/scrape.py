# simple scraper to batch download a file type (in this case, a bunch of jpegs)


import requests
import bs4
import wget

# set web page from which to select urls of interest
root_url = 'http://www.noobslab.com'
index_url = root_url + '/2011/06/beautiful-nature-wallpapers-hd-hq.html'


def get_page_urls():
    """ select urls of interest from web page and store in a list """
    page = requests.get(index_url)
    soup = bs4.BeautifulSoup(page.text)
    # list comprehension to get list of urls
    return [a.attrs.get('href') for a in soup.select('div.post-body a[href$=".jpg"]')]

# Confirm successful grab of urls
print(get_page_urls()) 

def list_of_links():
    """ loop through list urls of interest and download associated files """
    for links in get_page_urls():
        dl = wget.download(links)
        # print(links)
        # return links
        

