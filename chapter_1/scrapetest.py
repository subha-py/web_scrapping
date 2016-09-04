from urllib.request import urlopen,HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        print(e)
    try:
        bs_obj=BeautifulSoup(html.read(),'html.parser')
        title=bs_obj.body.h1
    except AttributeError as e:
        return None
    return title

title=getTitle("http://www.pythonscraping.com/pages/page1.html")

if title==None:
    print("Title could not be found")
else:
    print(title)