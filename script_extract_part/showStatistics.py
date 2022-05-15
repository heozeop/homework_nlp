#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import math, json
import re
from IPython.display import clear_output
import numpy as np
import math


# In[2]:



genres = ['Action','Comedy', 'Crime', 'Musical', 'Horror']
colors = {'Action':'limegreen', 'Comedy':'violet','Crime':'dodgerblue','Musical':'darkgreen','Horror':'deepskyblue'}


# In[3]:



result = {}

key_list = []
key_dicts = []
merged_keys = set()
counts = {}

for genre in genres:
    f = open(f"{genre}.json", "r")
    data = json.loads(f.read())
    f.close()
    index = 0
    for (local_key_list, key_dict) in data:
        if len(local_key_list) == 0:
            continue
        merged_keys.update(local_key_list)
        key_list.append(local_key_list)
        local_max = max(key_dict.values())
#         print(type(key_dict))
        index += 1
        for key in local_key_list:
            key_dict.update({key: key_dict[key]/local_max})
        key_dicts.append(key_dict)
    print(f"edited {index}")
    counts[genre] = index



# In[4]:



dfi={key: 0 for key in list(merged_keys)}
doc_len = len(key_list)
for doc_key in key_list:
    for key in doc_key:
        dfi.update({key: dfi[key] + 1})

        
    
        


# In[6]:


a = 0
for doc_keys in key_list:
    for key in doc_keys:
        key_dicts[a].update({key:key_dicts[a][key] * dfi[key]})
    a+=1


# In[7]:


genre_dicts = {}
prev = 0
action = key_dicts[:262]
comedy = key_dicts[262:612]
crime = key_dicts[612:825]
musical = key_dicts[825: 850]
horror = key_dicts[850:]


# In[8]:


top_action = set()
for ac in action:
    curd = [f for (f,_) in sorted(ac.items(), key = lambda item: item[1], reverse = True)]
    if len(top_action) == 0:
        top_action.update(curd)
    else:
        top_action.intersection(curd)


# In[19]:


def calcTop(dict_list):
    top_action = set()
    for ac in dict_list:
        curd = [f for (f,_) in sorted(ac.items(), key = lambda item: item[1], reverse = True)[:1000]]
        if len(top_action) == 0:
            top_action.update(curd)
        else:
            top_action.intersection(curd)
    return top_action


# In[20]:


top_action = calcTop(action)
top_commedy = calcTop(comedy)
top_crime = calcTop(crime)
top_musical = calcTop(musical)
top_horror = calcTop(horror)
    


# In[21]:


tops=[top_action.difference(top_commedy),
top_action.difference(top_crime),
top_action.difference(top_musical),
top_action.difference(top_horror)]
print("actions",[len(x) for x in tops])
comedies = [
    
top_commedy.difference(top_action),
top_commedy.difference(top_crime),
top_commedy.difference(top_musical),
top_commedy.difference(top_horror)
]

print("comedies",[len(x) for x in comedies])

crimes = [
    
top_crime.difference(top_action),
top_crime.difference(top_commedy),
top_crime.difference(top_musical),
top_crime.difference(top_horror)
]

print("crimes",[len(x) for x in crimes])

musicals = [
    
top_musical.difference(top_action),
top_musical.difference(top_commedy),
top_musical.difference(top_crime),
top_musical.difference(top_horror)
]

print("musicals",[len(x) for x in musicals])


# In[22]:


def printCount(ts):
    a = set();
    for t in ts:
        if len(a) == 0:
            a.update(t)
        else:
            a.difference(t)
    print(len(a))


# In[18]:


printCount(tops)
printCount(comedies)
printCount(crimes)
printCount(musicals)


# In[3]:


pip install matplotlib.font_manager

