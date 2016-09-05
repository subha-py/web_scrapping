from urllib.request import urlopen,HTTPError
from bs4 import BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj=BeautifulSoup(html,'html.parser')
nameList=bsObj.find_all('span',{'class':'green'})
for name in nameList:
    print(name.get_text())