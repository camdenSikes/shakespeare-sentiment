##run revised vader sentiment on shakespeare

from decimal import *
from vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

midsummerFile = open("midsummer.txt", "r")
midsummer = midsummerFile.readlines()

for line in midsummer:
    vs = analyzer.polarity_scores(line)
    polarity = vs["compound"]
    print(polarity)