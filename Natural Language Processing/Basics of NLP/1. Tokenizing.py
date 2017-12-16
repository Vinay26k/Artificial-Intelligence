from nltk.tokenize import word_tokenize, sent_tokenize

'''
f = open('story.txt','r')
data = f.read()
print(sent_tokenize(data))
print(word_tokenize(data))
'''

EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."
print(sent_tokenize(EXAMPLE_TEXT))
print([x for x in word_tokenize(EXAMPLE_TEXT)])


