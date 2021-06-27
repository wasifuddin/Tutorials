# pip install textblob

from textblob import TextBlob
word = TextBlob('cmputr')
print("Corrected Word " + str(word.correct()))