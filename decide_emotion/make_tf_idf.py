import numpy as np
import pandas as pd
from math import log10
import csv

num_doc = 11 

temp = open("allemotion.csv",'r',encoding='utf-8-sig')
readercsv = pd.read_csv('allemotion.csv', names = ['word','tf','emotion'],encoding='CP949')
tf_idf_file = open('tf_idf_emotion.csv','w',encoding='utf-8',newline='')
rdr = csv.reader(temp)
wr = csv.writer(tf_idf_file,delimiter=',')

for line in rdr:
    find_row = readercsv.loc[(readercsv['word'] == line[0])]
    data=[]
    data.append(line[0])
    tf = int(line[1])
    df = len(find_row)
    idf = log10(num_doc / (df + 1))
    tf_idf = tf * idf
    data.append(tf_idf)
    data.append(line[2])
    wr.writerow(data)


temp.close()
tf_idf_file.close()

fd = pd.read_csv('tf_idf_emotion.csv', names = ['word','tf_idf','emotion'],encoding='CP949')

df = fd.loc[fd.groupby(['word'])['tf_idf'].idxmax()]
df.to_csv('final_tf_idf.csv',mode='a',header=False)
