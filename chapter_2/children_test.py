from urllib.request import urlopen,HTTPError
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,'html.parser')

for child in bsObj.find("table",{'id':'giftList'}).tr.next_siblings:
    print(child)