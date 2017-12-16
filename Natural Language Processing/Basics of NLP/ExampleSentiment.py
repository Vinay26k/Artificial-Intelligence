import sentiment_mod as s

##print(s.sentiment(r"This movie was awesome, acting was great, plot was wonderful and there\
## were pythons."))
##print(s.sentiment(r"This movie was utter junk. There were absolutely \
##0 pythons. I don't see what the point was at all. Horrible movie 0/10"))

#pos
data = open('WonderStruck.txt', 'r',encoding="utf8").read()
data = data.replace('Advertisement','')
print(s.sentiment(data))

data = open('BadMomsChristMas.txt', 'r',encoding="utf8").read()
data = data.replace('Advertisement','')
print(s.sentiment(data))

data = open('SavingChristmas.txt', 'r',encoding="utf8").read()
data = data.replace('Advertisement','')
print(s.sentiment(data))

#pos
data = open('BalladOfNarayama.txt', 'r',encoding="utf8").read()
data = data.replace('Advertisement','')
print(s.sentiment(data))


#medium neg>pos
data = open('BladeOfImmortal.txt', 'r',encoding="utf8").read()
data = data.replace('Advertisement','')
print(s.sentiment(data))
