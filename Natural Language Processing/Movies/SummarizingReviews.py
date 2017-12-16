from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

text,sents,words = None, None, None
  

import urllib.request as ul
from bs4 import BeautifulSoup as bs

def preProcess(text):
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
import gatherReview as rw 
#gatherReview is local import file

def main():
    links = rw.funCore()
    f = open('Allreviews.txt','w')
    for link in links:
        text = rw.runUrl(link[0])
        print("="*99)
        '''
        #####1#######
        '''
        for x in (Summarize(text,5)):
            print(x)
            '''
            #####2#####
        '''
        print("="*99)
    f.close()
    
if __name__ == '__main__':
    main()




'''
#mySubstitue
####1####
  print("\t"*99)
        print(link[1])
        print("\t"*99)
        print("="*99)
        f.write("="*99)
        f.write("\n")
        f.write("\n")
        f.write(link[1])
        f.write("\n")
        f.write("\n")
#########
####2####
#f.write(link[1].encode('ascii',errors='replace').replace('?',' '))
            #.encode('ascii',errors='replace').replace('?',' ')
            f.write(x)
        f.write("\n")
        f.write("\n")
        f.write("="*99)
        f.write("\n")
#########
'''
