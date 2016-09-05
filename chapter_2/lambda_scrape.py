from urllib.request import urlopen,HTTPError
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,'html.parser')
print(bsObj.findAll(lambda tag: len(tag.attrs)==2))