##run revised vader sentiment on shakespeare

from decimal import *
from vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

midsummerFile = open("macbeth.txt", "r")
midsummer = midsummerFile.readlines()
count = 0
compound = 0
for line in midsummer:
    vs = analyzer.polarity_scores(line)
    print(vs["compound"])
    compound += vs["compound"]
    if compound != 0:
        count += 1
compound = compound/count
print(compound)