from sklearn.feature_extraction.text import TfidfVectorizer
doxyDonkeyPosts = list(set(open("BlogPosts.txt",'r').read().split("\n")))


vectorizer = TfidfVectorizer(max_df=0.5,min_df=2,stop_words='english')
x = vectorizer.fit_transform(doxyDonkeyPosts)
#print(x[1])

from sklearn.cluster import KMeans
km = KMeans(n_clusters = 3, init='k-means++', max_iter=100, n_init =1, verbose=True)
km.fit(x)

import numpy as np
arr = np.unique(km.labels_,return_counts=True)
print(arr)

text ={}
for i,cluster in enumerate(km.labels_):
    oneDocument = doxyDonkeyPosts[i]
    if cluster not in text.keys():
        text[cluster] = oneDocument
    else:
        text[cluster] += oneDocument

from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict
from string import punctuation
from heapq import nlargest
import nltk

customSW = set(stopwords.words('english')+list(punctuation))

keywords ={}
counts= {}
for cluster in range(3):
    word_sent = word_tokenize(text[cluster].lower())
    word_sent = [ x for x in word_sent if x not in customSW ]
    freq = FreqDist(word_sent)
    keywords[cluster] = nlargest(100,freq,key=freq.get)
    counts[cluster] = freq



unique_keys={}
for cluster in range(3):
    other_clusters = list(set(range(3))-set([cluster]))
    key_other_clusters = set(keywords[other_clusters[0]]).union(set(keywords[other_clusters[1]]))
    unique = set(keywords[cluster])-key_other_clusters
    unique_keys[cluster] = nlargest(10,unique,key=counts[cluster].get)

import pprint as p
p.pprint(unique_keys,width=1)


article ='''Snapdeal receives Rs113 crore from Nexus, founders in surprise funding: Struggling online marketplace Snapdeal has received Rs113 crore in an emergency financing round from existing investor Nexus Venture Partners and the company’s founders. The funding will not affect Snapdeal’s proposed sale to Flipkart, three people familiar with the matter said, on condition of anonymity. Snapdeal (Jasper Infotech Ltd) has been in talks to sell itself to bigger rival Flipkart amid a boardroom battle involving its three most powerful investors and its co-founders Kunal Bahl and Rohit Bansal. Japanese technology and telecoms conglomerate SoftBank Group Corp, Snapdeal’s largest investor, is trying to engineer the sale after giving up on the online marketplace, which has lost out to Flipkart and Amazon India in the e-commerce battle. At the other corner are Nexus, Kalaari Capital and the Snapdeal co-founders, all of whom were initially opposed to the sale.'''
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(x,km.labels_)

test = vectorizer.transform([article])
print(classifier.predict(test))



