from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    # >> > o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
    # >> > o
    # ParseResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
    #             params='', query='', fragment='')
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" or "www" that do
    # not contain the current URL
    for link in bsObj.findAll("a", href=re.compile(
                            "^(http|www|https)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html,'html.parser')
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        try:
            return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        except:
            print('We are done here')
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    if externalLink is not None:
        print("Random external link is: " + externalLink)
        followExternalOnly(externalLink)


followExternalOnly("http://www.nsec.ac.in/")



allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    try:
        html = urlopen(siteUrl)
    except:
        print('Site is not reachable anymore...quitting!')
        return
    bsObj = BeautifulSoup(html,'html.parser')
    internalLinks = getInternalLinks(bsObj,urlparse(siteUrl).netloc)
    externalLinks = getExternalLinks(bsObj,urlparse(siteUrl).netloc)
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
    print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("About to get link: "+link)
    allIntLinks.add(link)
    getAllExternalLinks(link)

getAllExternalLinks("http://www.nsec.ac.in/")