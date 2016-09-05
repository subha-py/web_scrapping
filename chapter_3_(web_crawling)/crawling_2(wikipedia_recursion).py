from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
# Things wikipedia page redirects:
# • They reside within the div with the id set to bodyContent
# • The URLs do not contain semicolons
# • The URLs begin with /wiki/
def getLinks(articleUrl):
    html=urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    return bsObj.find('div',{'id':'bodyContent'})\
        .findAll('a',href=re.compile('^(/wiki/)((?!;).)*$'))

links=getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle=links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links=getLinks(newArticle)