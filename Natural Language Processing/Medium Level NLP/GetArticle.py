import urllib2 as ul
from bs4 import BeautifulSoup as bs

articleUrl = r'https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?utm_term=.edab3111d8dc'

page = ul.urlopen(articleUrl).read().decode('utf8','ignore')
soup = bs(page,'html.parser')
text = ' '.join(map(lambda p: p.text,soup.find_all('article')))
print(text)
f = open("Pentagon1.txt",'w')
f.write(text.encode('ascii',errors='replace').replace("?"," "))
#f.write(text.encode('utf8'))
f.close()
