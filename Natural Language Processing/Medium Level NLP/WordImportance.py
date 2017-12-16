from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.probability import FreqDist
import PreProcessing as pp #custom module

words,sents = pp.preProcess()
#print(words)

freq = FreqDist(words)
#print(dict(freq))


from heapq import nlargest
#get top 10 important words
print(nlargest(10,freq,key=freq.get))

from collections import defaultdict
ranking = defaultdict(int)

for i,sent in enumerate(sents):
    for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i] += freq[w]

print(ranking)
sents_idx = nlargest(4,ranking,key=ranking.get)
print(sents_idx)
sorted_sents_idx = [sents[j] for j in sorted(sents_idx)]
print(sorted_sents_idx)
