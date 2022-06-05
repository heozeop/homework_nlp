from attr import asdict
import nltk
from nltk.corpus import stopwords
import re
import pandas as pd
import numpy as np


input_sentence = input("write your sentence in english :  ")

df = pd.read_csv('final_tf_idf.csv', names = ['word','tf_idf','emotion'],encoding='CP949')

only_english = re.sub('[^a-zA-Z]', ' ',input_sentence)
no_capitals = only_english.lower().split()

# 불용어 제거
stops = set(stopwords.words('english'))
no_stops = [word for word in no_capitals if not word in stops]

# 어간 추출
stemmer = nltk.stem.SnowballStemmer('english')
stemmer_words = [stemmer.stem(word) for word in no_stops]

word_df = pd.DataFrame(index=range(0,len(stemmer_words)),columns={'tf_idf','emotion'})
temp = 0



for pre_word in stemmer_words:
    find_row = df.loc[(df['word'] == pre_word)]
    if len(find_row) !=0 :
        word_df.loc[temp,'tf_idf'] = find_row.iloc[0,1]
        word_df.loc[temp,'emotion'] = find_row.iloc[0,2]
        temp += 1
        
word_df = word_df.dropna()

if len(word_df) == 0 :
    print("input sentence has no meaningful word Or can't find emotion")
else :
    word_df = word_df.astype({'tf_idf': np.float })
    target_index = word_df['tf_idf'].argmax()
    print(word_df)
    print(word_df.loc[target_index,'emotion'])


