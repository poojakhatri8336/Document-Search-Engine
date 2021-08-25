import nltk as nltk
import pymongo
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import csv



client = pymongo.MongoClient("mongodb://localhost:27017/")

# Database Name
db = client["CNNProxy"]

# Collection Name
col = db["CNN_collectionProxy"]

stop_words=set(stopwords.words("english"))
list_stopwords= list(stop_words)

ps = PorterStemmer()

i=1


def featchandstore():
    df = pd.DataFrame([])
    bigramdf = pd.DataFrame([])
    global i
    for x in col.find({}, {"_id":0, "URL": 1, "Body": 1 ,"Headline" : 1},no_cursor_timeout=True):           #fetching data from mongodb collection , for now only first 50
        d = {}
        print(i)
        Body = x['Body']                                                          #gives data in form of dict datatype so getting body from dict
        Body = Body.replace('\n',' ')

        # remove digits from text
        text = ''.join([i for i in Body if not i.isdigit()])

        # remove unicode characters
        encoded_string = text.encode("ascii", "ignore")
        text = encoded_string.decode()

        # Remove special symbols
        for char in '!\"#$%&()*+.-/:;<=>?@[\]^_`{|}~\n,':
            text=text.replace(char,' ')

        #convert all text to lower case
        text = text.lower()

        # generate tokens
        tokens = word_tokenize(text)

        for token in tokens:
            if token in list_stopwords:
                while token in tokens:
                    tokens.remove(token)

        for token in tokens:
            if "\'" in token:
                tokens.remove(token)

        for token in tokens:
            if token.startswith("\'"):
                tokens.remove(token)

        # stemming of word
        tokens[:] = [ps.stem(token) for token in tokens]

        for token in tokens:
            if token not in d:
                d[token] = 0
            d[token] += 1

        for key, value in d.items():
            collection = db.WordTFIDFNew
            mydict = {"term": key, "doc": i, "frequency": value, "Headline": x['Headline'],
                      'URL': x['URL']}
            collection.insert_one(mydict)
            #df = df.append({"term": key, "doc": i, "frequency": value}, ignore_index=True)

        #bigram work

        bgs = nltk.bigrams(tokens)
        global fdist
        fdist = nltk.FreqDist(bgs)

        for k, v in fdist.most_common():
            collection = db.BigramTFIDFNew

            mydict = {"Bi-gram": k, "doc": i, "frequency": v, "Headline": x['Headline'],
                      'URL': x['URL']}
            collection.insert_one(mydict)
            #bigramdf = bigramdf.append({"term": k, "doc": i, "frequency": v}, ignore_index=True)

        i= i+1
    '''    
    df.sort_values(by=['term'], inplace=True)
    bigramdf.sort_values(by=['term'], inplace=True)
    df.to_csv (r'ProjectTFIDF.csv', index = False, header=True)
    bigramdf.to_csv(r'projectBigramTFIDF.csv', index=False, header=True)
    '''

featchandstore()
