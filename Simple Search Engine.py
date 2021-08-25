#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import nltk
#nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import string
import re
import json


# In[3]:


df = pd.read_json("CNN_collectionProxy.json")


# In[4]:


df = df[:120000]


# In[5]:


Headline_clean = []
for d in df["Headline"]:
    d = str(d)
    # Remove Unicode
    document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
    # Remove Mentions
    document_test = re.sub(r'@\w+', '', document_test)
    # Lowercase the document
    document_test = document_test.lower()
    # Remove punctuations
    document_test = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', document_test)
    # Lowercase the numbers
    document_test = re.sub(r'[0-9]', '', document_test)
    # Remove the doubled space
    document_test = re.sub(r'\s{2,}', ' ', document_test)
    Headline_clean.append(document_test)


# In[6]:


df.shape


# In[7]:


pd.DataFrame(Headline_clean)


# In[8]:


df["Headline_clean"] = pd.DataFrame(Headline_clean)


# In[ ]:





# In[9]:


df.head()


# In[10]:


from sklearn.feature_extraction.text import TfidfVectorizer
# Instantiate a TfidfVectorizer object
vectorizer = TfidfVectorizer()
# It fits the data and transform it as a vector
X = vectorizer.fit_transform(Headline_clean)
# Convert the X as transposed matrix
X = X.T.toarray()
# Create a DataFrame and set the vocabulary as the index
df_vec = pd.DataFrame(X, index=vectorizer.get_feature_names())


# In[11]:


df_vec


# In[12]:


columns = ['URL', 'Headline','Body']


# In[13]:


def get_similar_news(q):
    df_text = pd.DataFrame()
    q = [q]
    q_vec = vectorizer.transform(q).toarray().reshape(df_vec.shape[0],)
    sim = {}
    for i in range(df_vec.shape[1]):
        sim[i] = np.dot(df_vec.loc[:, i].values, q_vec) / np.linalg.norm(df_vec.loc[:, i]) * np.linalg.norm(q_vec)
        sim_sorted = sorted(sim.items(), key=lambda x: x[1], reverse=True)  
    for k, v in sim_sorted:
        if v != 0.0:
            df_text = df_text.append(df.iloc[k], ignore_index = True)
            #print(df.iloc[k]["URL"])    
    #df_text[columns].to_json(str(q[0])+".json",orient="records",force_ascii=True)
    json_object = json.dumps(json.loads(df_text[columns].to_json(orient="index")))
    with open(str(q[0])+".json", "w") as outfile:
        outfile.write(json_object)


# In[19]:


q1 = 'world'
get_similar_news(q1)


# In[20]:


q1 = 'sports'
get_similar_news(q1)


# In[21]:


q1 = 'travel'
get_similar_news(q1)


# In[22]:


q1 = 'politics'
get_similar_news(q1)


# In[ ]:




