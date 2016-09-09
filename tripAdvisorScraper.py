from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

#URL to the first page of the restaurent names we want to scrape
BASE_URL = "http://www.tripadvisor.com/Restaurants-g29556-Ann_Arbor_Michigan.html"

def getEaterySearchResults(section_url):
    """
    Gets the data on one page of the url (page specified by section url)
    """
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
   # search_results = soup.find_all(id="EATERY_SEARCH_RESULTS")
    search_results = soup.find_all(id=re.compile("eatery"))
    print len(search_results)
    print (search_results[0])

def main():
   getEaterySearchResults(BASE_URL)

main()
