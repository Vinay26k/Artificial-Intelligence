import urllib.request as ul
from bs4 import BeautifulSoup as bs


#.encode('ascii',errors='replace').replace("?"," ")
def getDoxyDonkeyText(testUrl):
    request = ul.Request(testUrl)
    response = ul.urlopen(request).read().decode('utf8','ignore')
    soup = bs(response,'html.parser')
    mydivs = soup.find_all('div',{'class':"post-body entry-content"})
    #print(mydivs)
    posts = []
    for div in mydivs:
        posts += map(lambda p: p.text,div.find_all("li"))

    return posts    
for x in getDoxyDonkeyText('http://doxydonkey.blogspot.in/'):
    print(x)
