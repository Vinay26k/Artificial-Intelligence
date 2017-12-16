import requests
from bs4 import BeautifulSoup as bs

url = r'https://www.rogerebert.com/reviews/blade-of-the-immortal-2017'

data = requests.get(url).text
soup = bs(data,'html.parser')
#print(soup)
f = open('BladeOfImmortal.txt','w+')
for x in soup.find_all('div',attrs={'itemprop':'reviewBody'}):
   # print x.get_text()
    for y in x.find_all('p'):
        #print(y.get_text())')
        f.write(y.get_text().strip().encode('utf-8'))
f.close()
print("Done!")
