import random
import nltk
from nltk.corpus import movie_reviews

documents =[(list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
'''

Basically, in plain English, the above code is translated to:
In each category (we have pos or neg), take all of the file IDs
(each review has its own ID), then store the word_tokenized version
(a list of words)for the file ID, followed by
the positive or negative label in one big list.

'''
##documents =[]
##for category in movie_reviews.categories():
##    for fileid in movie_reviews.fileids(category):
##        documents.append(list(movie_reviews.words(fileid)),category)

random.shuffle(documents)
#print(documents[1])

##for (rev,cat) in documents:
##    print(rev,cat)

all_words =[]
for w in movie_reviews.words(): #all doc words
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))
#print(all_words["stupid"])

word_features = list(all_words.keys())[:3000]
print(word_features)

def find_features(document): #single doc i.e, sample
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features


print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev), category) for (rev, category) in documents]

