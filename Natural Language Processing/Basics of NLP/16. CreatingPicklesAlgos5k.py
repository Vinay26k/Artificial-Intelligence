import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

from nltk.classify import ClassifierI
from statistics import mode

from nltk.tokenize import word_tokenize


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
        
short_pos = open("positive.txt","r").read()
short_neg = open("negative.txt","r").read()

documents = []
all_words = []
allowed_word_types =["J"]

for r in short_pos.split('\n'):
    documents.append( (r, "pos") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

for r in short_neg.split('\n'):
    documents.append( (r, "neg") )
    words = word_tokenize(r)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())



save_documents = open("pickled/documents.pickle","wb")
pickle.dump(documents,save_documents)
save_documents.close()




all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]
save_word_features = open("pickled/word_features5k.pickle","wb")
pickle.dump(word_features,save_word_features)
save_word_features.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]
save_feature_sets = open("pickled/featuresets.pickle","wb")
pickle.dump(featuresets,save_feature_sets)
save_feature_sets.close()

'''
random.shuffle(featuresets)
print(len(featuresets))

training_set = featuresets[:10000]
testing_set =  featuresets[10000:]



##classifier = nltk.NaiveBayesClassifier.train(training_set)
##print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
##classifier.show_most_informative_features(15)
##
##
##
##save_classifier = open("pickled/originalnaivebayes5k.pickle","wb")
##pickle.dump(classifier, save_classifier)
##save_classifier.close()
##
##
##
##
##MNB_classifier = SklearnClassifier(MultinomialNB())
##MNB_classifier.train(training_set)
##print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)
##
##
##
##save_classifier = open("pickled/MNB_classifier5k.pickle","wb")
##pickle.dump(MNB_classifier, save_classifier)
##save_classifier.close()
##
##
##
##
##BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
##BernoulliNB_classifier.train(training_set)
##print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)
##
##
##
##save_classifier = open("pickled/BernoulliNB_classifier5k.pickle","wb")
##pickle.dump(BernoulliNB_classifier, save_classifier)
##save_classifier.close()
##
##
##
##LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
##LogisticRegression_classifier.train(training_set)
##print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)
##
##
##save_classifier = open("pickled/LogisticRegression_classifier5k.pickle","wb")
##pickle.dump(LogisticRegression_classifier, save_classifier)
##save_classifier.close()
##

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)


save_classifier = open("pickled/SGDC_classifier5k.pickle","wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()



##SVC_classifier = SklearnClassifier(SVC())
##SVC_classifier.train(training_set)
##print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)


save_classifier = open("pickled/LinearSVC_classifier5k.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

save_classifier = open("pickled/NuSVC_classifier5k.pickle","wb")
pickle.dump(NuSVC_classifier, save_classifier)
save_classifier.close()

voted_classifier = VoteClassifier(
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)

print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)


save_classifier = open("pickled/voted_classifier5k.pickle","wb")
pickle.dump(voted_classifier, save_classifier)
save_classifier.close()
'''
