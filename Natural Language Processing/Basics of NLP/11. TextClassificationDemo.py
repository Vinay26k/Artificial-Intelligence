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
print(documents[1])

all_words =[]
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))
print(all_words["stupid"])
