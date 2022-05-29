import csv

with open('tweet_emotions.csv','r',encoding='utf-8') as f:
    rdr = csv.reader(f)
    emotion = ["empty"]
    k=0
    

    for content in rdr:
        for i in range(len(emotion)):
            if not content[1] in emotion:
                emotion.append(content[1])
                
    print(emotion)
    e2 = open('sadness.txt','w',encoding='utf-8')
    e3 = open('enthusiam.txt','w',encoding='utf-8')
    e4 = open('neutral.txt','w',encoding='utf-8')
    e5 = open('worry.txt','w',encoding='utf-8')
    e6 = open('surprise.txt','w',encoding='utf-8')
    e7 = open('love.txt','w',encoding='utf-8')
    e8 = open('fun.txt','w',encoding='utf-8')
    e9 = open('hate.txt','w',encoding='utf-8')
    e10 = open('happiness.txt','w',encoding='utf-8')
    e11 = open('boredom.txt','w',encoding='utf-8')
    e12 = open('relief.txt','w',encoding='utf-8')
    e13 = open('anger.txt','w',encoding='utf-8')

    f.seek(0)
    for content in rdr:
        if content[2][0] == '@':
            index = content[2].find(' ')
            content[2] = content[2][index+1:len(content[2])]   

        if content[1] == emotion[2]:
            e2.write(content[2]+'\n')
        elif content[1] == emotion[3]:
            e3.write(content[2]+'\n')
        elif content[1] == emotion[4]:
            e4.write(content[2]+'\n')
        elif content[1] == emotion[5]:
            e5.write(content[2]+'\n')
        elif content[1] == emotion[6]:
            e6.write(content[2]+'\n')
        elif content[1] == emotion[7]:
            e7.write(content[2]+'\n')
        elif content[1] == emotion[8]:
            e8.write(content[2]+'\n')
        elif content[1] == emotion[9]:
            e9.write(content[2]+'\n')
        elif content[1] == emotion[10]:
            e10.write(content[2]+'\n')
        elif content[1] == emotion[11]:
            e11.write(content[2]+'\n')
        elif content[1] == emotion[12]:
            e12.write(content[2]+'\n')
        elif content[1] == emotion[13]:
            e13.write(content[2]+'\n')
        
    e2.close()
    e3.close()
    e4.close()
    e5.close()
    e6.close()
    e7.close()
    e8.close()
    e9.close()
    e10.close()
    e11.close()
    e12.close()
    e13.close()
