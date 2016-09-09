from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import string


#URL to the first page of the restaurent names we want to scrape
BASE_URL = "http://www.tripadvisor.com/Restaurants-g29556-Ann_Arbor_Michigan.html"
TOWN_NAME = "Ann_Arbor_Michigan"
NUM_PER_PAGE = 30 

def getNumRestaurents():
    """
    Gets the number of restaurents from the base URL
    """
    html = urlopen(BASE_URL).read()
    soup = BeautifulSoup(html, "lxml")

    rest = soup.find(class_="popIndex popIndexDefault")
    #rest = rest.splice()
    rest = (rest.string).split()
    return int(rest[2])


def generatePageUrl(pageNum):
    """
    Returns the URL specific to the page number specified
    Pages are 0 indexd
    """
    pageStarterNum = (pageNum * NUM_PER_PAGE) + 1
    splitIndex = string.find(BASE_URL, TOWN_NAME)
    newURL = BASE_URL[0:splitIndex] + "oa" + str(pageStarterNum) + "-" + BASE_URL[splitIndex:len(BASE_URL)]
    return newURL


def getEateryNamesAndURLs(section_url):
    """
    Gets the data on one page of the url (page specified by section url)
    Returns a list of all NUM_PER_PAGE restaurent names on the page specified
    Each name is paired with the url stub of the restaurent
    """
    html = urlopen(section_url).read()
    soup = BeautifulSoup(html, "lxml")
    #Gets the raw data
    search_results = soup.find_all(class_="property_title")
    #Formats what I need
    return [(i.string.replace('\n', ''), i.get('href')) for i in search_results]


def addDomainToURLStub(rest):
    """
    Takes in a list of the restaurents in the form [("restaurentName", urlstub)]
    And adds in the domain name specified by the BASE_URL
    """

    for i in range(len(rest)):
        rest[i] = (rest[i][0],  "http://tripadvisor.com" +  rest[i][1])
    return rest        

def getAllCityEateryNames():
    """
    returns a list of all of the eartery names in the city with their
    corresponding url stubs
    """
    numRestaurents = getNumRestaurents()
    restaurents = []
    for pageNum in range(0, numRestaurents / NUM_PER_PAGE + 1):
        section_url = generatePageUrl(pageNum)
        restaurents.extend(getEateryNamesAndURLs(section_url))
    restaurents = addDomainToURLStub(restaurents)
    return restaurents


def main():

    #Gets a list of all restaurents tripadvisor has in the city specified up top
    restaurents = getAllCityEateryNames()
    for i in restaurents:
        print i[0], i[1]


if __name__ == "__main__":
    main()
    
