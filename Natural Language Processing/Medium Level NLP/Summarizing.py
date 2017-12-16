from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

text,sents,words = None, None, None

articleUrl = r'https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?utm_term=.edab3111d8dc'
    

import urllib.request as ul
from bs4 import BeautifulSoup as bs

def getArticle(url=None):
    #articleUrl = r'https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?utm_term=.edab3111d8dc'
    if url!=None:
        articleUrl = url
    page = ul.urlopen(articleUrl).read().decode('utf8','ignore')
    soup = bs(page,'html.parser')
    text = ' '.join(map(lambda p: p.text,soup.find_all('article')))
    #text = open('Pentagon1.txt','r').read()
    return text

def preProcess(text):
    #text = open('Pentagon1.txt','r').read()
    sents = sent_tokenize(text)
    #print(sents)

    word_sent = word_tokenize(text.lower())
    #print(word_sent)

    customStopWords = set(stopwords.words('english')+ list(punctuation))
    #print(customStopWords)

    wordsWOStopWords = [x for x in word_sent if x not in customStopWords]
    #print(wordsWOStopWords)

    return (wordsWOStopWords,sents)




from nltk.probability import FreqDist
from heapq import nlargest

def ImportanceLogic(words):
    #words,sents = ppreProcess()
    #print(words)
    freq = FreqDist(words)
    #print(dict(freq))
    #get top 10 important words
    ImportantWords = (nlargest(10,freq,key=freq.get))
    return freq,ImportantWords

from collections import defaultdict


def Summarize(text,n):
    words,sents = preProcess(text)
    assert n<=len(sents)
    
    freq,ImportantWords = ImportanceLogic(words)

    #print(freq)
    ranking = defaultdict(int)
    #print(sents)
    for i,sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                #print(sent,w,freq)
                ranking[i] += freq[w]
    #print(ranking)
    sents_idx = nlargest(4,ranking,key=ranking.get)
    #print(sents_idx)
    sorted_sents_idx = [sents[j] for j in sorted(sents_idx)]
    #print(sorted_sents_idx)
    return sorted_sents_idx

import sys

def main():
    #for x in sys.argv:
    #    print(x)
    '''
    if len(sys.argv)!=2: #if command prompt two
        print("Usage: python Summarizing.py url")
        sys.exit(1)
    else:
        url = sys.argv[1]
        #print(url)
    '''
    print("="*136)
    #for x in (Summarize(getArticle(url),3)):
    text = open('output.txt','r').read()
    for x in (Summarize(text,5)):
        print(x)
    print("="*136)
    
if __name__ == '__main__':
    main()

