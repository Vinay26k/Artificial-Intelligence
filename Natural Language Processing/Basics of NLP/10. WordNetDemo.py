from nltk.corpus import wordnet

'''
synonyms = wordnet.synsets("program")
#synset
print()
print(synonyms)
#only synonyms
print()
print([x.lemmas()[0].name() for x in synonyms])

#definitions
print()
print([x.definition() for x in synonyms])

#examples
print()
print([x.examples() for x in synonyms])
'''

synonyms = []
antonyms = []
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#Wu and Palmer method to check similarity real life example plagiarism

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")

print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("aeroplane.n.01")

print(w1.wup_similarity(w2))
