
# Adapted from (http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python)

# Two Main Steps for Scraping a Website
1. Load a web page as a string
2. Parse the HTML from a web page to locate the objects of interest


# Set up virtual environment for scraping
``` python
$ mkdir pycon-scraper
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install requests beautifulsoup4
```

# Load packages
import requests
import beautiful soup

<hr />

# Goal: Get links to all jpeg images files so they can be batch downloaded
## web page: http://www.noobslab.com/2011/06/beautiful-nature-wallpapers-hd-hq.html

# First, peform a manual web page source inspection for html tags (chrome)
view-source:http://www.noobslab.com/2011/06/beautiful-nature-wallpapers-hd-hq.html

# load web page as a string
page = requests.get('http://www.noobslab.com/2011/06/beautiful-nature-wallpapers-hd-hq.html')


# Use CSS selector syntax to target specific <a> tags within parent <div> tags, within the parent <class>  
### Note: [See this site for more on CSS selectors](http://www.w3schools.com/cssref/css_selectors.asp)

soup = bs4.BeautifulSoup(page.text)
links = soup.select('div.post-body entry-content a[href$=".jpg"]')

### List  comprehension will accomplish the same thing as above
links = [a.attrs.get('href') for a in soup.select('div.post-body sa[href$=".jpg"]')]

# Complete scraping script
import requests
import bs4

root_url = 'http://www.noobslab.com'
index_url = root_url + '/2011/06/beautiful-nature-wallpapers-hd-hq.html'

def get_page_urls():
    page = requests.get(index_url)
    soup = bs4.BeautifulSoup(page.text)
    return [a.attrs.get('href') for a in soup.select('div.post-body a[href$=".jpg"]')]

print(get_page_urls())


<hr />

# Now that the page is scraped, next step is to 