from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
example_sentence = "This is an example of stop word filtration."
example_sentence = "Mr.John went to the buy a brown shoe."

words = word_tokenize(example_sentence)

filtered_sentence =[]

'''
for x in words:
    if x in stop_words:
        print(x)
    else:
        filtered_sentence.append(x)
'''
filtered_sentence =[w for w in words if w not in stop_words]
print(filtered_sentence)


#program removes all the connectors like is,an,of whatever but still sententce
#is useful
