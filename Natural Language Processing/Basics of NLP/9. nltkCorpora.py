import nltk
print(nltk.__file__)

##import subprocess
##subprocess.Popen(r'explorer "C:\Users\lenovo\AppData\Local\Programs\Python\Python36-32\lib\site-packages\nltk"')#+nltk.__file__)

from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)

print([print(line) for line in tok[5:15]])
