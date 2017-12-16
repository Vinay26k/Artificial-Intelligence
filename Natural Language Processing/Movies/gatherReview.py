import urllib.request as ul
from bs4 import BeautifulSoup as bs



#r = requests.get(url).text
#print(r)
#burl = r'https://timesofindia.indiatimes.com/entertainment/telugu/movie-reviews/malli-raava/movie-review/61979091.cms'
#runUrl(burl)

def runUrl(url):
    #print('here')
    baseUrl =r'https://timesofindia.indiatimes.com'
    url = baseUrl+url
    r = ul.urlopen(url).read().decode('utf8','ignore')
    soup = bs(r,'html.parser')
    for x in soup.find_all('div',attrs={'class':'Normal'}):
        text = (''.join(x.getText().strip()))
    return text

links = []
def funCore():
    url = r'https://timesofindia.indiatimes.com/entertainment/telugu/movie-reviews'
    r = ul.urlopen(url).read().decode('utf8','ignore')
    soup = bs(r,'html.parser')

    for x in soup.find_all('h2'):
        #,attrs={'
        for y in x.find_all('a'):
            #print(y['href'])#,y.getText())
            #print(y.getText())
            links.append((y['href'],y.getText()))
    return links
            
def core(links):
    for x in links:
        print(x[1])
        runUrl(x[0])
        
#core(funCore())
