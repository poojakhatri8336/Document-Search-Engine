# DocumentSearchEngineWebApplication

**Instructions to run the code**

As the data is huge it will take more than 10 hours to generate a word Tfidf and Bigram Tfidf by running preprocess.py and to collect data from  cnn api it will take more than 6 hours by running the datacollection.py. 

So, to save that time import the collections from cnndata folder into mongodb database name CNNProxy.

Cnn folder can be downloaded from the below link.

https://drive.google.com/file/d/1Prcc3ktlUdJjm_molXU6lsW3O5qIQpqj/view?usp=sharing


  

Download the program files from https://github.com/meghasravani95/DocumentSearchEngineWebApplication

Enter the following Commands: (Windows)
$ set Flask_app=hello.py
$ set Flask_env=development

This command updates the changes into the flask server directly with out typing the flask run command every time when we have made any change.

$ flask  run

After this command, the debugger, server, reloader will be started at local host server.

 ![image](https://user-images.githubusercontent.com/56423729/117167005-e2fe1700-ad94-11eb-965a-30200bfa68ed.png)


Type http://127.0.0.1:5000/ in the browser then the homepage will be displayed as below.

 ![image](https://user-images.githubusercontent.com/56423729/117166958-d974af00-ad94-11eb-9eee-65de7c76d6cc.png)


Topic Categorization results:

Click on the respective category in the navigation bar. Below are the screen shots that will show the respective page.

World:

 
![image](https://user-images.githubusercontent.com/56423729/117166926-d1b50a80-ad94-11eb-80a0-4e29fd362847.png)



Travel:

 ![image](https://user-images.githubusercontent.com/56423729/117166892-c9f56600-ad94-11eb-9d79-bfc159ab0253.png)



Politics:

 
![image](https://user-images.githubusercontent.com/56423729/117166866-c4981b80-ad94-11eb-8810-e9e629eb6024.png)




Sports:
![image](https://user-images.githubusercontent.com/56423729/117166831-bb0eb380-ad94-11eb-9ea9-e6bca7e7e887.png)


Document Search Engine results:

For a word like food:

 

![image](https://user-images.githubusercontent.com/56423729/117166796-b4803c00-ad94-11eb-8d9b-f6c25aedbecc.png)



For a bigram like joe biden:

 
![image](https://user-images.githubusercontent.com/56423729/117166779-ae8a5b00-ad94-11eb-9bad-79b6aeb304f8.png)


For details of the article, Click on for Quick reference of article

![image](https://user-images.githubusercontent.com/56423729/117166705-9e727b80-ad94-11eb-898d-6bc939b097fa.png)

 
If you click on image or the headline, it will be redirected to CNN page which contains this article. Also, the visited url’s are distinguished from the unvisited ones.



