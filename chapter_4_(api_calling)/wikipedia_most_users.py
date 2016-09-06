from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
from parsing_json import getCountry
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html=urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    return bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile(r'^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    #Format of revision history pages is:
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl=pageUrl.replace('/wiki/','')
    historyUrl='http://en.wikipedia.org/w/index.php?title='+pageUrl+'&action=history'
    print('history url is: '+historyUrl)
    html=urlopen(historyUrl)
    bsObj=BeautifulSoup(html,'html.parser')
    #finds only the link with class 'mw-anonuserlink' which has IP addresses
    #instead of usernames
    ipAdresses=bsObj.findAll('a',{'class':'mw-anonuserlink'})
    addressList=set()
    for ipAdress in ipAdresses:
        addressList.add((ipAdress.get_text(),getCountry(ipAdress.get_text())))
    return addressList

links=getLinks('/wiki/Python_(programming_language)')

while(len(links)>0):
    for link in links:
        print('--------------------')
        historyIPs=getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            print(historyIP)
    newLink=random.choice(links).attrs['href']
    links=getLinks(newLink)