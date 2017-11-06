from decimal import *
from vaderSentiment import SentimentIntensityAnalyzer

shakespeareDict = open("dictionary.txt", "r")

shakespearePolarity = {}

analyzer = SentimentIntensityAnalyzer()

for line in shakespeareDict:
    wordAndDef = line.split(",", 1)
    word = wordAndDef[0]
    word = word.lower()
    definition = wordAndDef[1]
    shakespearePolarity[word] = 0
    vs = analyzer.polarity_scores(definition)
    shakespearePolarity[word] = 4 * vs["compound"]
    
idioms = ''
##find "special case idioms" aka multiple words
for word in shakespearePolarity:
    if " " in word:
        newIdiom = '"' + word + '": ' + str(shakespearePolarity[word]) + ", "
        idioms += newIdiom
print(idioms)


##iterate through dictionary and change existing words in lexicon
##add unknown words to lexicon

#print(shakespearePolarity)