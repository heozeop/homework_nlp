import nltk
import pickle
from nltk.corpus import stopwords
import re
from collections import Counter

input_sentence = input("write your sentence in english :  ")

only_english = re.sub('[^a-zA-Z]', ' ',input_sentence)
no_capitals = only_english.lower().split()

# 불용어 제거
stops = set(stopwords.words('english'))
no_stops = [word for word in no_capitals if not word in stops]

# 어간 추출
stemmer = nltk.stem.SnowballStemmer('english')
stemmer_words = [stemmer.stem(word) for word in no_stops]

print(stemmer_words)