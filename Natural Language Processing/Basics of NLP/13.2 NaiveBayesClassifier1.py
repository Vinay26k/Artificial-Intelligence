import nltk
import random
from nltk.corpus import movie_reviews, stopwords
import pickle

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append((list(movie_reviews.words(fileid)),category))
        
random.shuffle(documents)
print(documents[1])

all_words = []

filter_words = set(stopwords.words('english'))

for w in movie_reviews.words():
    if w not in filter_words:
        all_words.append(w.lower())


#print(set(stopwords.words('english')))
all_words = nltk.FreqDist(all_words)
#print(all_words.most_common(15))

word_features = list(all_words.keys())[:3000]
print(word_features)

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w]=(w in words)

    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
featuresets = [(find_features(rev),category) for (rev,category) in documents]


#classifier training and testing

# set that we'll train our classifier with
training_set = featuresets[:1900]

# set that we'll test against.
testing_set = featuresets[1900:]


classifier = nltk.NaiveBayesClassifier.train(training_set)

print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)

save_classifier = open("naivebayesMovies1.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

        
