import csv

f = open ('allemotion.csv','w',encoding='utf-8',newline='')

wr = csv.writer(f,delimiter=',')

f1 = open("emotion_anger.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('anger')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_boredom.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('boredom')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_enthusiam.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('enthusiam')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_fun.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('fun')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_happiness.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('happiness')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_hate.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('hate')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_love.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('love')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_relief.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('relief')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_sadness.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('sadness')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_surprise.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('surprise')
      
    wr.writerow(data)
    
f1.close()

f1 = open("emotion_worry.csv",'r',encoding='utf-8-sig')
f1rdr = csv.reader(f1)

for line in f1rdr:
    data = []
    data.append(line[0])
    data.append(line[1])
    data.append('worry')
      
    wr.writerow(data)
    
f1.close()

f.close()