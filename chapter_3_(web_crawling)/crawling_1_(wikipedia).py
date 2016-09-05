from urllib.request import urlopen,HTTPError
from bs4 import BeautifulSoup
import re
# Things wikipedia page redirects:
# • They reside within the div with the id set to bodyContent
# • The URLs do not contain semicolons
# • The URLs begin with /wiki/
html=urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj=BeautifulSoup(html,'html.parser')
for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])