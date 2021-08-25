import pymongo
import requests
from pymongo import MongoClient
import time

'''

url = 'https://search.api.cnn.io/content?q=coronavirus&size=10&from=20&page=3'
json_data = requests.get(url).json()
data = json_data['result']
for i in range(0,10):                       #bcoz one page has 10 records
    print((data[i]['url']))
    '''
try:
    conn = MongoClient("mongodb://localhost:27017/")
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# database
db = conn.CNNProxy

# Created or Switched to collection name: CNN_collection
collection = db.CNN_images
collection.create_index('URL', unique=True)

searchlist = [#'india', 'weather', 'world', 'business', 'entertainment', 'style', 'sports', 'food', 'design', 'opinion',
              #'success', 'shooting', 'culture', 'media',
    'china','Europe', 'Middle East', 'Pandemic', 'Australia',
              'US', 'congress', 'America', 'film', 'crime', 'football', 'Energy']
searchlist3 = ['food']  # luxury and tennis  5000 ,skiing , horse racing and parenting 1100,  dubai 3200, beauty 6800, 'United Kingdom' upto 156 page, drink basketball soccer california apartments transportation beach

proxies = [{"http": 'http://150.129.148.88'}, {"http": 'http://103.250.166.4'}, {"http": 'http://100.26.152.8'},
           {"http": 'http://211.24.95.49'}, {"http": 'http://168.119.137.56'}, {"http": 'http://1.179.148.9'},
           {"http": 'http://103.145.32.98'}, {"http": 'http://46.29.9.46'}, {"http": 'http://104.248.48.211'},
           {"http": 'http://198.50.163.192'}]
k = 0
for word in searchlist3:
    fromsize = 0

    proxy = proxies[k]
    for page in range(1, 201):  # specify how manytotal page from pagination you want to extract
        url = "https://search.api.cnn.io/content?q=" + str(word) + "&size=50&from=" + str(fromsize) + "&page=" + str(
            page)
        print(url)
        fromsize += 50
        # time.sleep(2)
        json_data = requests.get(url, proxies=proxy).json()
        data = json_data['result']  # data has 50 records of one page
        for i in range(0, 50):  # bcoz one page has 50 records
            try:
                mydict = {"URL": data[i]['url'], "thumbnail": data[i]['thumbnail']}
                # print(mydict)
                collection.insert_one(mydict)
                '''print((data[i]['url']))
                print(data[i]['headline'])
                print(data[i]['body'])
                print(data[i]['lastPublishDate'])
                print("\n")'''
            except pymongo.errors.DuplicateKeyError:
                continue
            except IndexError:
                continue
    k = k + 1
    if k == 10:
        k = 0
    time.sleep(200)
