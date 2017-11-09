from decimal import *
from vaderSentiment import SentimentIntensityAnalyzer

shakespeareDictFile = open("dictionary.txt", "r")
vaderLex = open("vader_lexicon.txt", "r")
vaderShakeLex = open("vaderShakeLex.txt", "w")
vaderLexList = vaderLex.readlines()

shakespeareDict = {}

analyzer = SentimentIntensityAnalyzer()

for line in shakespeareDictFile:
    wordAndDef = line.split(",", 1)
    word = wordAndDef[0]
    word = word.lower()
    definition = wordAndDef[1]
    shakespeareDict[word] = 0
    vs = analyzer.polarity_scores(definition)
    shakespeareDict[word] = 4 * vs["compound"]
    
idioms = ''
idiomsList = []
##find "special case idioms" aka multiple words
for word in shakespeareDict:
    if " " in word:
        newIdiom = '"' + word + '": ' + str(shakespeareDict[word]) + ", "
        idioms += newIdiom
        idiomsList.append(word)
for word in idiomsList:    
    del shakespeareDict[word]
#print(idioms)

for item in vaderLexList:
    word = item.split("\t")
    word = str(word[0])
    if word not in shakespeareDict: #maybe shakespeareDict.values()?
        vaderShakeLex.write(item)
for item in shakespeareDict:
    newItem = "\n" + item + "\t" + str(shakespeareDict[item])
    vaderShakeLex.write(newItem)


##iterate through dictionary and change existing words in lexicon
##add unknown words to lexicon

#print(shakespearePolarity)