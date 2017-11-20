# shakespeare-sentiment
# By Martha Durrett and Camden Sikes
How to add to the VADER lexicon:
- In lexiconSetup.py, change the dictionary file being used to whatever dictionary you want to add, and the output file to an appropriate filename

- Run lexiconSetup.py

- In vaderSentiment/vaderSentiment/vaderSentiment.py, go to line 197 and change the name of the file being opened to the lexicon you just created

Now, VADER will be using the newly created lexicon. To run it line by line on a text, and also get and average score for the whole text, change the text being opened in vaderShakespeare.py, and run the program.


# File descriptions (* means depreciated):

In this directory:

*cleandict.py - for the old dictionary we were using, to get it into a form we could use

*comparisons.xlsx - comparisons of sentiment scores using our old dictionary compared to the original lexicon

*dictionary.txt - the original dictionary we were using, depreciated

lexiconSetup.py - takes the original vader lexicon and a dictionary of words, adds the sentiments of these words to the lexicon

<play>.txt - the text of <play>, with all line breaks within a single character's dialogue removed

<play>_definitions.txt - the dictionary of Shakespearean words in <play>
sentiment_over_time.xlsx - spreadsheet of the sentiments of the plays over time

topics<play>.csv - topic modeling for <play>

vaderShakespeare.py - Runs sentiment analysis on a file, specified in the code

In vaderSentiment/vaderSentiment/:

vader_lexicon.txt - the original VADER lexicon

vaderAllThreeLex.txt - the VADER lexicon with words from all three considered plays added

vader<play>Lex.txt - The VADER lexicon with words from <play> added

vaderSentiment.txt - the VADER sentiment analysis tool. To change the lexicon being used, change the file mentioned in line 197

*vaderShakeLex.txt - the VADER lexicon with the words from the old dictionary added