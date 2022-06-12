import nltk
from nltk.corpus import stopwords
import re
import pandas as pd
import numpy as np
from pandas import DataFrame

class EmotionDecider:
    emo_genre = {'anger': 'Horror', 'boredom': 'Adventure', 'enthusiam': 'Action', 'fun': 'Comedy',
                 'happiness': 'Family',
                 'hate': 'Crime', 'love': 'Romance', 'relief': 'Musical', 'sadness': 'Drama', 'surpirse': 'Thriller',
                 'worry': 'Mystery'}
    df: DataFrame

    def __init__(self, df):
        self.df = df

    def decide(self, text: str) -> str:
        only_english = re.sub('[^a-zA-Z]', ' ', text)
        no_capitals = only_english.lower().split()

        # 불용어 제거
        stops = set(stopwords.words('english'))
        no_stops = [word for word in no_capitals if not word in stops]

        # 어간 추출
        stemmer = nltk.stem.SnowballStemmer('english')
        stemmer_words = [stemmer.stem(word) for word in no_stops]

        word_df = pd.DataFrame(index=range(0, len(stemmer_words)), columns={'tf_idf', 'emotion'})
        temp = 0

        for pre_word in stemmer_words:
            find_row = self.df.loc[(self.df['word'] == pre_word)]
            if len(find_row) != 0:
                word_df.loc[temp, 'tf_idf'] = find_row.iloc[0, 1]
                word_df.loc[temp, 'emotion'] = find_row.iloc[0, 2]
                temp += 1

        word_df = word_df.dropna()

        if len(word_df) == 0:
            print("input sentence has no meaningful word Or can't find emotion")
            return "any"
        else:
            word_df = word_df.astype({'tf_idf': np.float})
            target_index = word_df['tf_idf'].argmax()
            print(word_df)
            emotion = word_df.loc[target_index, 'emotion']
            emotion = str(emotion)
            print(self.emo_genre[emotion])  # 출력값 (장르로 나옴)
            return self.emo_genre[emotion]



