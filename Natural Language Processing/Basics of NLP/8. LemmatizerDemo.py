from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

#output will be singular form of following words
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))

#better not plural returns same
print(lemmatizer.lemmatize("better"))

#pos used for saying that better is adjective
print(lemmatizer.lemmatize("better",pos='a'))
print(lemmatizer.lemmatize("watched",pos='a'))
