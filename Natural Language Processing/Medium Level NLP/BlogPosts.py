import urllib.request as ul
from bs4 import BeautifulSoup as bs

prev = []
try:
    prev = open("DoxyUrls.txt",'r').read().split('\n')

except:
    print("Urls file not found")

f = open("DoxyUrls.txt",'a+')

def getAllDoxyDonkeyPosts(url,links,f):
    #print("Entered")
    request = ul.Request(url)
    response = ul.urlopen(request)
    soup = bs(response,'html.parser')
    for a in soup.find_all('a'):
        #print("In for")
        try:
            #print("Entered")
            url = a['href']
            title = a['title']
            #print(anchor['title'])
            if title == 'Older Posts':
                print(title,url)
                if url not in prev:
                    #f.write(url)
                    print(url,file=f)
                else:
                    print("Present")
                links.append(url)
                getAllDoxyDonkeyPosts(url,links,f)
        except:
            title= " "
    #print("End")
    return

def getDoxyDonkeyText(testUrl):
    request = ul.Request(testUrl)
    response = ul.urlopen(request).read()#.decode('utf8','ignore')
    soup = bs(response,'html.parser')
    mydivs = soup.find_all('div',{'class':"post-body entry-content"})
    #print(mydivs)
    posts = []
    for div in mydivs:
        posts += map(lambda p: p.text,div.find_all("li"))

    return posts    



blogUrl = r'http://doxydonkey.blogspot.in/'
links = []
#getAllDoxyDonkeyPosts(blogUrl,links,f)
f.close()
links = open('DoxyUrls.txt','r').read().split('\n')

doxyDonkeyPosts = []
pst = []
try:
    pst = open("BlogPosts.txt",'r').read().split('\n')
except:
    print("File Not found")

f = open("BlogPosts.txt",'a+')
for link in links[:-1]:
    post = getDoxyDonkeyText(link)
    for x in post:
        if x not in pst:
            print("Adding post")
            try:
                f.write(x)
                f.write("\n")
            except:
                pass 
            
        else:
            print("post already present")
#print([x for x in doxyDonkeyPosts])
f.close()
