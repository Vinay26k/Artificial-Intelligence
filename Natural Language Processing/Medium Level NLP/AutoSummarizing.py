from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

text = open('Pentagon1.txt','r').read()
sents = sent_tokenize(text)
#print(sents)

word_sent = word_tokenize(text.lower())
#print(word_sent)

customStopWords = set(stopwords.words('english')+ list(punctuation))
#print(customStopWords)

wordsWOStopWords = [x for x in word_sent if x not in customStopWords]
print(wordsWOStopWords)
