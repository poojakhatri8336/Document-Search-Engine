import pprint

from flask import Flask, render_template, request
from pymongo import MongoClient


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results')
def results():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.CNNProxy
    result = []

    word=(request.args['Search'])
    if ' ' in word:
        print("you entered bigram")

        chunks = word.split(' ')
        for r in db.BigramTFIDFnew.find(
                {'$query': {'Bi-gram': [chunks[0], chunks[1]]}, '$orderby': {'frequency': -1}}).limit(20):
            lst1=[]
            lst1.append(r['URL'])
            lst1.append(r['Headline'])
            for i in db.CNN_collectionProxy.find({'$query': {'URL': lst1[0]}}):
                #print(i['Body'])
                #print(type(i['Body']))
                lst1.append(str(i['Body']))
            for i in db.CNN_images.find({'$query': {'URL': lst1[0]}}):
                print(i['thumbnail'])
                lst1.append(i['thumbnail'])
            print(lst1)
            print(len(lst1))
            result.append(lst1)

    else:
        print("you entered single word")

        # for result in db.WordTFIDF.find({'$query': {'term': word}, '$orderby': {'frequency': -1}}).limit(20):
        #     print(result)
        for r in db.WordTFIDFnew.find({'$query': {'term':  {"$regex": "^"+word}},'$orderby': {'frequency': -1}}).limit(20):
            # print(r)
            lst1 = []
            lst1.append( r['URL'])
            lst1.append( r['Headline'])
            for i in db.CNN_collectionProxy.find({'$query': {'URL': lst1[0]}}):
                #print(i['Body'])
                #print(type(i['Body']))
                lst1.append(str(i['Body']))
            for i in db.CNN_images.find({'$query': {'URL': lst1[0]}}):
                print(i['thumbnail'])
                lst1.append(i['thumbnail'])
            print(lst1)
            print(len(lst1))
            result.append(lst1)
    return render_template('results.html', search=request.args['Search'],result=result)

@app.route('/travel')
def travel():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.CNNProxy
    result = []
    for r in db.travel.find().limit(db.travel.count()):
        dict1={}
        dict1['url']=r['URL']
        dict1['headline']=r['Headline']
        dict1['body']=r['Body']
        for i in db.CNN_images.find({'$query': {'URL': dict1['url']}}):
            print(i['thumbnail'])
            dict1['thumbnail']=i['thumbnail']
        result.append(dict1)

    return render_template('travel.html', result=result)

@app.route('/world')
def world():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.CNNProxy
    result = []
    for r in db.world.find().limit(db.world.count()):
        dict1={}
        dict1['url']=r['URL']
        dict1['headline']=r['Headline']
        dict1['body']=r['Body']
        for i in db.CNN_images.find({'$query': {'URL': dict1['url']}}):
            print(i['thumbnail'])
            dict1['thumbnail']=i['thumbnail']
        result.append(dict1)

    return render_template('world.html', result=result)

@app.route('/politics')
def politics():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.CNNProxy
    result = []
    for r in db.politics.find().limit(db.politics.count()):
        dict1={}
        dict1['url']=r['URL']
        dict1['headline']=r['Headline']
        dict1['body']=r['Body']
        for i in db.CNN_images.find({'$query': {'URL': dict1['url']}}):
            print(i['thumbnail'])
            dict1['thumbnail']=i['thumbnail']
        result.append(dict1)

    return render_template('politics.html', result=result)

@app.route('/sports')
def sports():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.CNNProxy
    result = []
    for r in db.sports.find().limit(db.sports.count()):
        dict1={}
        dict1['url']=r['URL']
        dict1['headline']=r['Headline']
        dict1['body']=r['Body']
        for i in db.CNN_images.find({'$query': {'URL': dict1['url']}}):
            print(i['thumbnail'])
            dict1['thumbnail']=i['thumbnail']
        result.append(dict1)

    return render_template('sports.html', result=result)


