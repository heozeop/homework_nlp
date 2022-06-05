import nltk
import pickle
from nltk.corpus import stopwords
import re
from collections import Counter
import csv

with open('worry.txt','r',encoding='utf-8') as f:
    f2 = open('emotion_worry.csv','w',encoding='utf-8',newline="") # 하나씩 파일명을 바꿔가며 만들어줘야함
    content = f.read()
    
    cleaned_content =  re.sub(r'[^\.\?\!\w\d\s]','',content)
    

    cleaned_content = cleaned_content.lower()
    word_tokens = nltk.word_tokenize(cleaned_content)

    tokens_pos = nltk.pos_tag(word_tokens)
    

    NN_words = []
    for word, pos in tokens_pos:
        if 'NN' in pos:
            NN_words.append(word)
        elif 'RB' in pos:
            NN_words.append(word)
    
    wlem = nltk.WordNetLemmatizer()
    lemmatized_words = []
    for word in NN_words:
        new_word = wlem.lemmatize(word)
        lemmatized_words.append(new_word)

    

    stopwords_list = stopwords.words('english') #nltk에서 제공하는 불용어사전 이용
    #print('stopwords: ', stopwords_list)
    custom_stopwords = ["..","im","haha","lol","yay","yeah","!",".","...","?","wa","....",".....","oh","lt3"]
    
    stopwords_list.extend(custom_stopwords)
    
    
    unique_NN_words = set(lemmatized_words)
    final_NN_words = lemmatized_words

    # 불용어 제거
    for word in unique_NN_words:
        if word in stopwords_list:
            while word in final_NN_words: final_NN_words.remove(word)

    c = Counter(final_NN_words) # input type should be a list of words (or tokens)
   
    k = 100
    wr = csv.writer(f2,delimiter=',')
    wr.writerows(c.most_common(k))
   
          

    f2.close()